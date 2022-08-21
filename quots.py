#task to scrap text data from given url
#author: Jagdish Chavan

#importing libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#proviing url
url = 'https://bluelimelearning.github.io/my-fav-quotes/'
uclient=uReq(url)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,'html.parser')
quotes=page_soup.findAll('div',{'class':'quotes'})

for quote in quotes:
    fav_quotes=quote.findAll('p',{'class':'aquote'})
    aquote =fav_quotes[0].text.strip()

    fav_quotes=quote.findAll('p',{'class':'author'})
    author =fav_quotes[0].text.strip()

    print(aquote)
    print(author)