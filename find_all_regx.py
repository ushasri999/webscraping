import requests
import re
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

ans1  = soup.find_all(["h4", "a"])
print(ans1)

ans2  = soup.find_all(string = re.compile('Galaxy'))
print(ans2)

