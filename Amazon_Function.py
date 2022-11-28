# Returns all items of first results page on Amazon

from bs4 import BeautifulSoup
import requests
 
def AmazonRequest(searchterm, numresults):
    URL = 'https://www.amazon.com/s?k=' + searchterm
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try: 
        # Get all HTML product names and prices from first results page
        all_items = soup.findAll("span", attrs={"class":"a-size-medium a-color-base a-text-normal"})
        all_prices = soup.findAll("span", attrs={"class": 'a-offscreen'})
    
        # Find and select each products price from the filtered HTML code
        prices = []
        for item in all_prices:
            prices.append(item.string)
        
        # Find and select each products name from the filtered HTML code
        names = []
        for item in all_items:
            names.append(item.string)
        
        # Prints products and their respective prices
        if (numresults <= len(all_items)):
            for i in range(numresults):
                print(str(names[i]) + ': ' + str(prices[i]))
        else:
            for i in range(len(all_items)):
                print(str(names[i]) + ': ' + str(prices[i]))
    
    except AttributeError:
        print("Item could not be found on Amazon.")

AmazonRequest("3090", 4)