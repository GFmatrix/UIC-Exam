import requests 
from bs4 import BeautifulSoup 
URL = "https://kun.uz"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html.parser')
for news in soup.find_all("a", class_="news-lenta"):
    r = requests.get(f"{URL}{news['href']}") 
    soup = BeautifulSoup(r.content, 'html.parser')
    meta = soup.find_all("meta",attrs={'property':'og:image'})
    img = meta[0]['content']
    print(f"{news.text} - {img}")
