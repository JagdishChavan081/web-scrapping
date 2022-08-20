#task: webscrapping with Bs4
#author: Jagdish Chavan
#for project purpose in this file Title extraction was performed from given link

#step1) importing necessary package
from bs4 import BeautifulSoup
import requests

#url, req, soup
url='https://www.google.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
print(soup.title)