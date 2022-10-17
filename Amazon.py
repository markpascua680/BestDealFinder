# Returns all items of first results page on Amazon

from bs4 import BeautifulSoup
import requests
from getData import *

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

URL = 'https://www.amazon.com/s?k=' + input("Enter product name: ")

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

try: 
    # Get all HTML product names and prices from first results page
    all_items = soup.findAll("span", attrs={"class":"a-size-medium a-color-base a-text-normal"})
    all_prices = soup.findAll("span", attrs={"class": 'a-offscreen'})

    getData(all_items, all_prices)

except AttributeError:
    print("Item could not be found on Amazon.")