#task: webscrapping with Bs4
#author: Jagdish Chavan
#present data in redable manner

#step1) importing necessary package
from bs4 import BeautifulSoup
import requests

#url, req, soup
url='https://firstsiteguide.com/best-blogging-platforms/'
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
print(soup.prettify())