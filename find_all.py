import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

prices = soup.find_all("h4", {"class": "price float-end card-title pull-right"})
print(len(prices))
for price in prices:
    print(price.string)

print(prices[3])
print(prices[3].string)