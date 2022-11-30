from git import Repo
import os 

APP_DIR = os.path.dirname(os.path.abspath(__file__))

repo = Repo(APP_DIR)
commit_hash = repo.git.rev_parse("HEAD")
print(commit_hash)


import os
from glob import glob

from setuptools import find_packages, setup


def read(fname):
    """
    Args:
        fname:
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

print(read('README.md'))