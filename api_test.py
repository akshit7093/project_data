import requests
import json



def fetch():
    url = "https://github.com/akshit7093/project_data/raw/main/db.json"
    response = requests.get(url)
    print(response.json())
fetch()