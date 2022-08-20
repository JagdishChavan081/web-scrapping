#task: webscrap stock price using beautiful soup
#author: Jagdish Chavan
#project stock data extraction 

#step1) importing necessary package
from bs4 import BeautifulSoup
import requests

def parseprice():
    req = requests.get('https://finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC')
    soup=BeautifulSoup(req.text,'lxml')
    price = soup.find('div',{'class':'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text 


while True:
    print('Current price:'+ str(parseprice()))