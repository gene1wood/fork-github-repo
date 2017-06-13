Fork a GitHub repo, clone that repo to a local directory, add the
upstream remote, create an optional feature branch and checkout that
branch

Usage
=====

::

    usage: fork-github-repo [-h] [--config CONFIG] url [branch]

    Fork a GitHub repo, clone that repo to a local directory, add the upstream
    remote, create an optional feature branch and checkout that branch

    positional arguments:
      url              GitHub URL of the upstream repo to fork
      branch           Name of the feature branch to create

    optional arguments:
      -h, --help       show this help message and exit
      --config CONFIG  Filename of the yaml config file (default :
                       ~/.github/fork_github_repo.yaml)

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

    $ fork-github-repo https://github.com/octocat/Spoon-Knife.git
    Forked https://github.com/octocat/Spoon-Knife.git to https://github.com/gene1wood/Spoon-Knife.git
    Cloned https://github.com/gene1wood/Spoon-Knife.git to /home/gene/code/github.com/gene1wood/Spoon-Knife
    Remote "upstream" created for https://github.com/octocat/Spoon-Knife.git
    Remote "upstream" fetched

Fork Spoon-Knife and create a feature branch called 'my-feature'

::

    $ fork-github-repo https://github.com/octocat/Spoon-Knife.git my-feature
    Forked https://github.com/octocat/Spoon-Knife.git to https://github.com/gene1wood/Spoon-Knife.git
    Cloned https://github.com/gene1wood/Spoon-Knife.git to /home/gene/code/github.com/gene1wood/Spoon-Knife
    Remote "upstream" created for https://github.com/octocat/Spoon-Knife.git
    Remote "upstream" fetched
    Branch "my-feature" created and checked out

