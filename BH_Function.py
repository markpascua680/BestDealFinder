from bs4 import BeautifulSoup
import requests


def BHRequest(searchterm, numresults):
    URL = 'https://www.bhphotovideo.com/c/search?q=' + searchterm
     
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
     
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:    
        # Gets all HTML prices and product names from the first results page
        all_prices = soup.findAll("span", attrs={"data-selenium":"uppedDecimalPrice"})
        all_names = soup.findAll("span", attrs={"data-selenium":"miniProductPageProductName"})
        
        # Checks if any results are present.
        if ((len(all_names) and len(all_prices)) == 0):
            print("Your search returned no results\n")
            
        # Find and select each products price in dollars and cents and then join them together to form the whole price.
        price_whole = []
        for item in all_prices:
            curr_dollar = item.find("span", attrs={"data-selenium":"uppedDecimalPriceFirst"}).string
            curr_cent = item.find("sup", attrs={"data-selenium":"uppedDecimalPriceSecond"}).string
            price_whole.append(curr_dollar + "." + curr_cent)
            
        # Prints products and their respective prices'
        if (numresults <= len(all_prices)):
            for i in range(numresults):
                print(str(all_names[i].string) + ': ' + str(price_whole[i]) +'\n')
        else:
            for i in range(len(all_prices)):
                print(str(all_names[i].string) + ': ' + str(price_whole[i]) +'\n')
    
    except AttributeError:
        print("Item could not be found")

BHRequest("3090", 4)