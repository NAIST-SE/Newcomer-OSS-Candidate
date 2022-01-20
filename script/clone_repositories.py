#Script to clone the repositories.

import pandas as pd
from git import Repo
import git
import os
from tqdm.auto import tqdm



for x in tqdm(repos_links):
    try:
        head, sep, tail = x.partition('.com/')
        repo_dir= '/Users/xxx/xxxxxx/%s'%tail
        git.Repo.clone_from(x, repo_dir)
    except Exception:
        pass

print("finish")

