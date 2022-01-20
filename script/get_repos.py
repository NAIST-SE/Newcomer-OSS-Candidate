# Script that generates a list of all the repos of a user through Api.



import csv 
import pandas as pd 
import urllib.request
from bs4 import BeautifulSoup 
from tqdm.auto import tqdm
import time
import requests




api_data = []
for url in tqdm(profile):
    request = requests.get(url, headers={'Authorization': 'token'})
    json = request.json()
    for i in range(0,len(json)):
        try:
            ids = json[i]['id']
            urls = json[i]['svn_url']
            name = json[i]['name']
            des = json[i]['description']
            lan = json[i]['language']
            fork = json[i]['fork']
            created_at = json[i]['created_at']
            api_data.append([url,ids,urls,name,des,lan,fork,created_at])
        except:
            print('error',url)
            api_data.append([url,'-','-','-','-','-','-','-'])

