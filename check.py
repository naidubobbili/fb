from bs4 import BeautifulSoup
import requests
url='https://www.facebook.com/login.php'
url='https://m.facebook.com/?refsrc=http%3A%2F%2Fwww.google.com%2Furl&_rdr'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')


print(soup.prettify(url))
