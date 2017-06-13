from distutils.core import setup

setup(
    name='fork-github-repo',
    version='1.0',
    packages=['fork_github_repo'],
    url='https://github.com/gene1wood/fork-github-repo',
    license=' GPL-3.0',
    author='Gene Wood',
    author_email='gene_wood@cementhorizon.com',
    description='''Fork a GitHub repo, clone that repo to a local directory,
add the upstream remote, create an optional feature branch and checkout
that branch''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        'giturlparse.py',
        'github3.py',
        'gitpython',
        'PyYAML',
        'retrying'
    ],
    entry_points={
        'console_scripts': [
            'fork-github-repo=fork_github_repo:main',
        ],
    },

)
