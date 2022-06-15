import requests as re
from bs4 import BeautifulSoup as bs
import json

res = re.get("https://technews.tw/")
sp = bs(res.text,'html.parser')
news = sp.find_all('li',class_="block2014")

newslst = []
sptlst = []
for i in news:
  newsdic = {}
  newsdic['category'] = i.div.text
  newsdic['sum_title'] = i.find_all('div','sum_title')[0].text.strip()
  newsdic['sum_title_url'] = i.a['href'] 
  newsdic['spotlist'] = sptlst
 
  for j in i.find_all('div','itemelse'):
    sptdic = {}
    sptdic['title'] = j.a.text.strip()
    sptdic['url'] = j.a['href']
    sptlst.append(sptdic)
   
  newslst.append(newsdic) 

with open('pj1-1.json','w',encoding = 'utf-8') as f:
  jstnews = json.dumps(newslst,ensure_ascii=False,indent=4)
  f.write(jstnews)
