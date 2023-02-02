import csv 
import json 
import os 
from github import *  
import sys 
import re 
from tqdm import tqdm 
from datetime import datetime 
from github import Github 
with open('config.json') as cf:  
     data = json.load(cf) 
g = Github(data['github']['username'], data['github']['token'])
repos = g.search_repositories('vuln') 
