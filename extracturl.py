#task: webscrapping with Bs4
#author: Jagdish Chavan
#extract urls 

#step1) importing necessary package
from bs4 import BeautifulSoup
import requests

#url, req, soup
url='https://www.google.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
for link in soup.find_all('a'):
    print(link.get('herf'))