#Script that generates names of all files inside of a commit.

import os, glob, csv, subprocess, sys, re
from git import *
from subprocess import Popen, PIPE
from os import path
import pandas as pd
from openpyxl import load_workbook


def execute_command(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    return out, error
    pipe.wait()
    
    
data=[]
for index,row in file1.iterrows():
    sha = row['merge_commit_sha']
    repo = row['repository']    
    diff_cmd = "git show --pretty="" --name-only " + sha
    tmp = str(execute_command(diff_cmd, repo))
    tmp = tmp.replace("\\t",",").replace("\\n",",").replace("(b'', b'')","").replace(",', b'')","").replace("(b'","")
    tmp = tmp.split(",")
    print(tmp)
    for file in tmp:
        data.append([sha, repo, file])

