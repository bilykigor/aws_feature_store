from git import Repo
import os 

APP_DIR = os.path.dirname(os.path.abspath(__file__))

repo = Repo(APP_DIR)
commit_hash = repo.git.rev_parse("HEAD")
print(commit_hash)