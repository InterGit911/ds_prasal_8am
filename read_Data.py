import os
from git import Repo

repo_url = 'https://github.com'
local_path = '/path/to/local/directory'

if not os.path.isdir(local_path):
    repo = Repo.clone_from(repo_url, local_path)
else:
    repo = Repo(local_path)
    repo.remotes.origin.pull() # Pull the latest changes
