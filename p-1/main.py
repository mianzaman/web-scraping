
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")
# print(soup)

# cards = soup.find_all("div", class_ ="col-md-4 col-xl-4 col-lg-4")
#
# print(len(cards))

# names = soup.find_all("a", {"class": "title"})
#
# # print(names)
# for name in names:
#     print(name.text)

prices = soup.find_all("h4", {"class": "price"})

# print(prices)
for price in prices:
    print(price.text)

# descriptions = soup.find_all("p", {"class": "card-text"})

# print(prices)
# for description in descriptions:
#     print(description.text)
