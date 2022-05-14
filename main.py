import requests 
from requests import get
import subprocess
import time
import sys
import os


os.system('cls && title YOUR PROGRAM NAME HERE')
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
prefix = "YOUR_PREFIX_HERE."+hwid

database = requests.get('https://pastebin.com/raw/ESDFE') # I put a random link here!

if prefix in database:
  pass
else:
  print(' Your HWID is not in the database')
  time.sleep(20)
  sys.exit()
  
  
  # YOUR CODE HERE
