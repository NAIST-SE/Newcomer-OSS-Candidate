#Script that run git-blame and count authors on each file inside of a commit.

import os, glob, csv, subprocess, sys, re, operator
from git import *
from subprocess import Popen, PIPE
from os import path
import pandas as pd
from tqdm.auto import tqdm


def execute_command(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    return out, error
    pipe.wait()
    

    
pattern1 = re.compile(r'(?P<commit_id>[\^]\w+|\w+)\s+(?P<filename>[^\s]+)\s+\((?P<committer>.*?)\s+(?P<date>\d{4}-\d\d-\d\d)\s+(?P<time>\d\d:\d\d:\d\d).*?(?P<line_number>\b\d+\b)\)\s(?P<code>.*)')
pattern2 = re.compile(r'(?P<commit_id>[\^]\w+|\w+)\s+\((?P<committer>.*?)\s+(?P<date>\d{4}-\d\d-\d\d)\s+(?P<time>\d\d:\d\d:\d\d).*?(?P<line_number>\b\d+\b)\)\s(?P<code>.*)')



header1 = ['bugintro_commitid', 'filename', 'committer', 'date', 'time', 'line_number', 'code']
header2 = ['bugintro_commitid', 'committer', 'date', 'time', 'line_number', 'code']



i = 1
data = []
for index,row in tqdm(file1.iterrows()):
    sha = row['sha']
    repository = row['local_repo_path']
    filepath = row['filepath']
    reponame = repository.split("/")[-2:]
    reponame = "_".join(n for n in reponame)
    try:
        fpath = filepath.replace(" ","_").split("/")[-1:][0]
    
        blametxt = '/Users/ifraz-re/data/research_survey/csv/api_work/blametext/' + reponame + fpath + ".txt"
        blame = "git blame " + filepath + " > " + blametxt
        execute_command(blame, repository)

        try:
            b = open(blametxt, encoding="utf8", errors='ignore')
            c = b.read().split('\n')

            authorname = []
            try:
                try:
                    pattern1.match(c[0]).groups()
                    for line in c:
                        authorname.append(pattern1.match(line).groups()[1])
                except:
                    pattern2.match(c[0]).groups()
                    for line in c:
                        authorname.append(pattern2.match(line).groups()[1])

            except:
                pass

            author = list(set(authorname))
            no_author = len(author)
            names = ";".join(au for au in author)
            data.append([repository, filepath, names, no_author])

        except:
            pass
        
    except:
        print(i,index,filepath,fpath)
        i+=1
        pass

