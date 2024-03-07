import trafilatura
import json
from newsplease import NewsPlease
from tqdm import tqdm
from multiprocessing import Pool


with open("/home/tomorrow/primera_folder/data/baomoi/news_data/samples_title.json",'r',encoding='utf8') as f:
    title= json.load(f)
with open("/home/tomorrow/primera_folder/data/baomoi/news_data/samples_sapo.json",'r',encoding='utf8') as f:
    sapo= json.load(f)

all_search_title= [i['related_search'] for i in sapo]

def extract_results_sample(sample):
  downloaded = trafilatura.fetch_url(sample['link'])
  try:
    article=  NewsPlease.from_html(downloaded)
    if article.maintext: 
      t_content= article.maintext 
    else:
      t_content=''
    if article.title:
      t_title = article.title
    else:
      t_title = ''
    if article.description:
      t_description = article.description
    else:
      t_description = ''
    if article.date_publish:
      t_date = str(article.date_publish)
    else:
      t_date = ''
    news = {'title': t_title, 'description': t_description, 'content': t_content, 'date': t_date}
  except Exception as e:
    news = {'title':'', 'description':'','content': '', 'date':''}
    # print(e,news)
  return news

def extract_results(list_urls):
  return [extract_results_sample(list_urls[id]) for id in range(len(list_urls))]



if __name__ == "__main__":
    # Number of processes to use
    num_processes = 2  # You can adjust this number as needed

    # Create a multiprocessing Pool
    with Pool(num_processes) as pool:
        # Use tqdm for progress bar
        results = list(tqdm(pool.imap(extract_results, all_search_title[:2]), total=len(all_search_title[:2])))
    with open("/home/tomorrow/primera_folder/data/baomoi/news_data/samples_content_sapo.json",'w',encoding='utf8') as f:
        json.dump(results,f,ensure_ascii=False,indent=4)
