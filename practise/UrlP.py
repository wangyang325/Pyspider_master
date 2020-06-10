import urllib.request
from bs4 import BeautifulSoup

url = "http://tieba.baidu.com"
response = urllib.request.urlopen(url)
html = response.read()
#print(html.decode('utf-8'))

soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
#print(soup.prettify())

for ap in soup.find_all('p'):
    print(ap)
