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

except AttributeError:
    items = "NA"
    print("Item could not be found")
