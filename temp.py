import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

names = soup.find_all("a", class_ = "title")
product_names = []
for name in names:
    product_names.append(name.text)
print(product_names)

prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")
prices_list = []
for price in prices:
    prices_list.append(price.text)
print(prices_list)

descriptions = soup.find_all("p", class_ = "description card-text")
descriptions_list = []
for description in descriptions:
    descriptions_list.append(description.text)
print(descriptions_list)


df = pd.DataFrame({"Product Name": product_names, "Price": prices_list, "Description": descriptions_list})

df.to_csv("product_details.csv")