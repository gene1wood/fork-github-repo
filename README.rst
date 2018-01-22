Fork a GitHub repo, clone that repo to a local directory, add the
upstream remote, create an optional feature branch and checkout that
branch

Usage
=====

::

    usage: fork-github-repo [-h] [-c CONFIG] url [branch]

    Fork a GitHub repo, clone that repo to a local directory, add the upstream
    remote, create an optional feature branch and checkout that branch

    positional arguments:
      url                   GitHub URL of the upstream repo to fork
      branch                Name of the feature branch to create

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Filename of the yaml config file (default :
                            ~/.github/fork_github_repo.yaml)

    The config file with a default location of
    ~/.github/fork_github_repo.yaml contains the following settings:

    -  github_token : The `GitHub personal access token with the public_repo scope
       allowed.
       https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
    -  repo_dir : The directory path to the directory containing all your cloned
        repos. If this isn't defined, /tmp is used.

    The file is YAML formatted and the contents look like this :

    github_token: 0123456789abcdef0123456789abcdef01234567
    repo_dir: ~/Documents/github.com/example/


Config
======

The config file with a default location of
``~/.github/fork_github_repo.yaml`` contains the following settings.

-  ``github_token`` : The `GitHub personal access
   token <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`__
   with the ``public_repo`` scope allowed
-  ``repo_dir`` : The directory path to the directory containing all
   your cloned repos. If this isn't defined, ``/tmp`` is used.

Examples
========

Fork Spoon-Knife

::

    $ fork-github-repo https://github.com/octocat/Spoon-Knife
    Forked https://github.com/octocat/Spoon-Knife to git@github.com:gene1wood/Spoon-Knife.git
    Cloned git@github.com:gene1wood/Spoon-Knife.git to /path/to/gene1wood/Spoon-Knife
    Remote "upstream" created for https://github.com/octocat/Spoon-Knife
    Remote "upstream" fetched

Fork Spoon-Knife and create a feature branch called 'my-feature'

::

    $ fork-github-repo https://github.com/octocat/Spoon-Knife my-feature
    Forked https://github.com/octocat/Spoon-Knife to git@github.com:gene1wood/Spoon-Knife.git
    Cloned git@github.com:gene1wood/Spoon-Knife.git to /path/to/gene1wood/Spoon-Knife
    Remote "upstream" created for https://github.com/octocat/Spoon-Knife
    Remote "upstream" fetched
    Branch "my-feature" created
    Branch "my-feature" pushed to origin
    Tracking branch "origin/my-feature" setup for branch "my-feature"
    Branch "my-feature" checked out

