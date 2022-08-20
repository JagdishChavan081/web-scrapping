
#task: webscrapping with Bs4 and sava in csv
#author: Jagdish Chavan
#for project purpose in this file Title extraction was performed from given link

#step1) importing necessary package
from bs4 import BeautifulSoup
import requests
import csv

#url, req, soup
url='https://firstsiteguide.com/best-blogging-platforms/'
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
print(soup.title)


file=csv.writer(open('output.csv','w'))
file.writerow([soup.title])


#try on extracturl.py