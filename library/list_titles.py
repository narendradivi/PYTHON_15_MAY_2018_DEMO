
import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text,'xml')
items = bs.findAll("item")

for item in items:
     print(item.title.text)
     print(item.link.text)