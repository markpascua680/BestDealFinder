# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:49:35 2022

@author: Hsnyd
"""


from bs4 import BeautifulSoup
import requests

URL = 'https://www.corsair.com/us/en/search/?text= ' + input("Enter product name: ")

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")


try: 
    # Get all HTML product names and prices from first results page
    all_items = soup.findAll("span", attrs={"class":'price'})
    

    # Pick out each product's individual name and price from HTML
    items = []
    prices = []
    for item in all_items:
        items.append(item.string)



    # Pair product names and prices in a tuple
    items_and_prices = [()]
    for i in range(len(items)):
        items_and_prices.append((items[i], prices[i]))

    # Print products and their prices
    for item in items_and_prices:
        result = ': '.join(item)
        print(result + '\n')

except AttributeError:
    items = "NA"
    print("Item could not be found")