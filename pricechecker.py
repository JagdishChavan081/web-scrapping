#iporting modules
import requests
from bs4 import BeautifulSoup
import smtplib

#creating variables
url='https://www.amazon.in/gp/product/B09CCMBHH1/ref=s9_acss_bw_cg_Header_5d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=DXETCRXAT508NE1A62GA&pf_rd_t=101&pf_rd_p=ebe55e3b-56e9-4df0-af96-8dd4bad2973d&pf_rd_i=1375424031'

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

price_value=139190
email_address='jagdish.chavan080@gmail.com'
password='---------'
receiver_email='jagdish.chavan081@gmail.com'

def getPrice():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title =soup.find(id='productTitle').get_text().strip()
    #price=soup.find(id='a-price-whole').get_text().strip()
    print(title)
    print(price)


if __name__ == '__main__':
    getPrice()
