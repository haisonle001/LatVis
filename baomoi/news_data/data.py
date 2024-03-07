from datasets import load_dataset

import random
import requests
import json
import time 
from tqdm import tqdm
from multiprocessing import Pool

vn = load_dataset("bkai-foundation-models/ViClusterData")
vn=vn['train']

with open("/home/tomorrow/primera_folder/search-customer/src/50serper.txt",'r') as file:
    txt=file.read()
all_key= [i.split(" ")[-1].strip() for i in txt.split('\n')]

class SerperSearch:
  def __init__(self,api_key = None):
    self.api_key = api_key
    self.url = "https://google.serper.dev/search"

  def search(self, query, gl="vn", hl="vi", page=0, num=10):
    payload = json.dumps({
      "q": query,
      "gl": gl,
      "hl": hl,
      "page": page,
      "num": num
    })
    headers = {
      'X-API-KEY': random.choice(self.api_key),
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", self.url, headers=headers, data=payload)
    return response.json()['organic']




def extract_text(temp):
    # Assuming `search` is defined elsewhere
    temp['related_search'] = search.search(temp['title'])
    return temp

def process_item(temp):
    return extract_text(temp)

count=1
while count<=5:
    try:
        ## Search
        search= SerperSearch(api_key=all_key[count:count+1])

        try:
            with open("/home/tomorrow/primera_folder/data/baomoi/news_data/samples_title.json",'r',encoding='utf8') as f:
                title= json.load(f)
        except:
            title=[]


        new_vn=[
            {'id': vn[i]['id'],
            'title': vn[i]['title'],
            'sapo': vn[i]['sapo'],
            'content': vn[i]['content']
            }
            for i in range(len(title),len(title)+2500) 
            if vn[i]['title'] and vn[i]['sapo']
        ]

        # Number of processes to use
        num_processes = 24  # You can adjust this number as needed

        # Create a multiprocessing Pool
        with Pool(num_processes) as pool:
            # Use tqdm for progress bar
            results = list(tqdm(pool.imap(process_item, new_vn), total=len(new_vn)))

        with open("/home/tomorrow/primera_folder/data/baomoi/news_data/samples_title.json",'w',encoding='utf8') as f:
            json.dump(title+results,f,ensure_ascii=False,indent=4)
        count+=1
    except Exception as e:
        print(e)
        count+=1
        continue