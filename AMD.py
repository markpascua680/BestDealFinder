# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:11:23 2022

@author: Hsnyd
"""

from bs4 import BeautifulSoup
import requests

URL = 'http://www.amd.com/en/direct-buy/us/'

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

print('pass1')
webpage = requests.get(URL, headers=HEADERS)
print('pass2')
soup = BeautifulSoup(webpage.content, "lxml")

print('pass3')

try: 
    # Get all HTML product names and prices from first results page
    all_items = soup.find("span", attrs={"class": 'visually-hidden'})
    print('pass4')
    all_prices = soup.find("span", attrs={"class": 'shop-price'})
    print('pass5')

except AttributeError:
    items = "NA"
    print("Item could not be found")
    # Pick out each product's individual name and price from HTML
