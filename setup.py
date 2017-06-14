from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fork-github-repo',
    version='1.0.1',
    packages=['fork_github_repo'],
    url='https://github.com/gene1wood/fork-github-repo',
    license=' GPL-3.0',
    author='Gene Wood',
    author_email='gene_wood@cementhorizon.com',
    description="Fork, clone, add remote and branch a GitHub repo",
    long_description=long_description,
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
