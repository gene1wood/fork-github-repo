from __future__ import print_function
import github3  # pip install github3.py
from git import Repo  # pip install gitpython
from giturlparse import parse  # pip install giturlparse.py
from retrying import retry  # pip install retrying
import yaml
import argparse
import os.path
import time

DEFAULT_CONFIG_FILENAME = '~/.github/fork_github_repo.yaml'


def github_url_argument(url):
    """Validate a url as a GitHub repo url and raise arparse exceptions if
    validation fails

    :param str url: A GitHub repo URL
    :return: The GitHub repo URL passed in
    """
    parsed_url = parse(url)
    if not parsed_url.valid:
        raise argparse.ArgumentTypeError('%s is not a valid git URL'
                                         % url)
    if not parsed_url.github:
        raise argparse.ArgumentTypeError('%s is not a GitHub repo'
                                         % parsed_url.url)
    return url


def get_config():
    """Parse command line arguments, extracting the config file name,
    read the yaml config file and add in the command line arguments,
    returning the union of config file and command line arguments

    :return: dict of config file settings and command line arguments
    """
    parser = argparse.ArgumentParser(description='''Fork a GitHub repo, clone 
    that repo to a local directory, add the upstream remote, create an 
    optional feature branch and checkout that branch''')
    parser.add_argument(
        '-c', '--config',
        help='Filename of the yaml config file (default : %s)'
             % DEFAULT_CONFIG_FILENAME,
        default=argparse.FileType('r')(
            os.path.expanduser(DEFAULT_CONFIG_FILENAME)
        ),
        type=argparse.FileType('r'))
    parser.add_argument('url', help="GitHub URL of the upstream repo to fork",
                        type=github_url_argument)
    parser.add_argument('branch', nargs='?', default=None,
                        help="Name of the feature branch to create")
    args = parser.parse_args()
    config = yaml.safe_load(args.config)
    config.update(dict(args._get_kwargs()))
    return config


def fork_and_clone_repo(
        upstream_url, github_token, repo_dir_root, branch_name=None,
        upstream_name='upstream'):
    """Fork a GitHub repo, clone that repo to a local directory,
    add the upstream remote, create an optional feature branch and checkout
    that branch

    :param str upstream_url: GitHub URL of the upstream repo
    :param str github_token: GitHub auth token
    :param str repo_dir_root: The local directory path under which clones
    should be written
    :param str branch_name: The name of the git feature branch to create
    :param str upstream_name: The name to use for the remote upstream
    :return: github3.Head object representing the new feature branch
    """
    # Scope needed is `public_repo` to fork and clone public repos
    # https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-scopes-for-oauth-apps/
    gh = github3.login(token=github_token)
    parsed_url = parse(upstream_url)

    # Fork the repo
    upstream_repo = gh.repository(parsed_url.owner, parsed_url.repo)
    if upstream_repo is None:
        print("Unable to find repo %s" % upstream_url)
        exit(1)
    forked_repo = upstream_repo.create_fork()
    print("Forked %s to %s" % (upstream_url, forked_repo.clone_url))

    # Wait for the fork to appear
    sleeping = False
    while True:
        forked_repo = gh.repository(gh.user().login, parsed_url.repo)
        if forked_repo is not None:
            if sleeping:
                print()
            break
        else:
            sleeping = True
            print('.', end="")
            time.sleep(1)

    # Clone the repo
    repo_dir = os.path.expanduser(os.path.join(repo_dir_root, parsed_url.repo))
    if os.path.isdir(repo_dir):
        print("Directory %s exists already, assuming it's a clone" % repo_dir)
        cloned_repo = Repo(repo_dir)
    else:
        cloned_repo = retry(
            wait_exponential_multiplier=1000,
            stop_max_delay=15000
        )(Repo.clone_from)(forked_repo.clone_url, repo_dir)
        print("Cloned %s to %s" % (forked_repo.clone_url, repo_dir))

    # Create the remote upstream
    try:
        upstream_remote = cloned_repo.remote(upstream_name)
        print('Remote "%s" already exists in %s' %
              (upstream_name, repo_dir))
    except ValueError:
        upstream_remote = retry(
            wait_exponential_multiplier=1000,
            stop_max_delay=15000
        )(cloned_repo.create_remote)(upstream_name, upstream_url)
        print('Remote "%s" created for %s' % (upstream_name, upstream_url))

    # Fetch the remote upstream
    results = retry(
        wait_exponential_multiplier=1000,
        stop_max_delay=15000
    )(upstream_remote.fetch)()
    print('Remote "%s" fetched' % upstream_name)

    # Create and checkout the branch
    if branch_name is None:
        return cloned_repo
    else:
        branch = cloned_repo.create_head(branch_name)
        branch.checkout()
        print('Branch "%s" created and checked out' % branch_name)
        return branch


def main():
    config = get_config()
    fork_and_clone_repo(
        config['url'],
        config['github_token'],
        config['repo_dir'],
        config['branch']
    )

if __name__ == '__main__':
    main()
