#task: webscrapping with Bs4
#author: Jagdish Chavan
#extract image, styles and DIV tags

#step1) importing necessary package
from bs4 import BeautifulSoup
import requests

#url, req, soup
url='https://firstsiteguide.com/best-blogging-platforms/'
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")

#div tag
#print(soup.find_all('div'))

#style tag
#print(soup.find_all('style'))

#image tag
#print(soup.find_all('img'))

#formating   bold tag
##print(soup.find_all('b'))

#formating italic tag
#print(soup.find_all('i'))

#formating italic tag
print(soup.find_all('strong'))