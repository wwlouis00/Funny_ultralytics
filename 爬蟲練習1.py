import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將此頁面的HTML GET下來
print(r.text) #印出HTML
