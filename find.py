import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

price = soup.find("h4", {"class": "price float-end card-title pull-right"})
print(price)
print(price.string)

prgh = soup.find("p", {"class": "description card-text"})
print(prgh)
print(prgh.string)

prgh = soup.find("p", class_ = "description card-text")
print(prgh)
print(prgh.string)

