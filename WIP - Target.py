from bs4 import BeautifulSoup
import requests
 
URL = 'https://www.target.com/s?searchTerm=' + input("Enter product name: ")
 
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
 
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
print(soup)
try:    
    # Gets all HTML prices and product names from the first results page
    # all_prices = soup.findAll('div', attrs={'class':"h-padding-r-tiny"})
    # all_names = soup.findAll("a", attrs={"data-test":"product-title"})
    
    # print(len(all_prices))
    
    # prices = []
    # for item in all_prices:
    #     test = item.find('span').string
    #     prices.append(test)
    # print(len(prices))
    # Checks if any results are present.
    # if ((len(all_names) and len(all_prices)) == 0):
    #     print("Your search returned no results\n")
        
    # Prints products and their respective prices
    # for i in range(len(all_prices)):
    #     print(str(all_names[i].string) + ': ' + str(all_prices[i]) +'\n')

except AttributeError:
    print("Item could not be found")
