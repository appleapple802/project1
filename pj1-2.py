import requests as re
from bs4 import BeautifulSoup as bs
import json

with open("pj1-1.json", "r") as f:
    json_news = json.loads(f.read())


for i in json_news:
    sum_url = i["sum_title_url"]
    res = re.get(sum_url)
    sp = bs(res.text, "html.parser")
    content = sp.find("div",{"class":"indent"},"a")
    m_name = "sum_" + i["category"] + "_" + i["sum_title"][0:4]
    with open(m_name+".txt", "w") as f:
       f.write(content.text.strip())

for j in json_news:
    for k in range(0,3):
        title_url = j["spotlist"][k]["url"]
        
        res2 = re.get(title_url).text
        sp2 = bs(res2, "html.parser")
        
        content = sp2.find("div",{"class":"indent"},"a")
        title_name = "spot_" + j["category"] + "_" + j["spotlist"][k]["title"][0:4] + ".txt"
        with open(title_name, "w") as f:
            f.write(content.text.strip())
