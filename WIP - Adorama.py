# WORK IN PROGRESS #

from bs4 import BeautifulSoup
import requests
 
URL = 'https://www.adorama.com/l/?searchinfo=' + input("Enter product name: ")
 
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
 
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

try:
    # Checks if any results are present.
    if (soup.find('span', attrs={"class", "result-message-error"})):
        print("Your search returned no results\n")
    
    # Gets all HTML prices and product names from the first results page
    all_prices = soup.findAll('div', attrs={"class":"prices"})
    all_names = soup.findAll('a', attrs={"class":'item-title'})
    # print(all_prices)
    
    # # Find and select each products price in dollars and cents and then join them together to form the whole price.
    price_whole = []
    for item in all_prices:
        price = item.findAll('strong', attrs={"class":"your-price"})
        print(price)
    # # Prints products and their respective prices
    # for i in range(len(all_prices)):
    #     print(str(all_names[i].string) + ': $' + str(price_whole[i]) +'\n')

except AttributeError:
    print("Item could not be found")
