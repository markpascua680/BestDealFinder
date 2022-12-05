# Returns all items of first results page on Amazon

from bs4 import BeautifulSoup
import requests
 
def AmazonRequest(searchterm, numresults, filters):
    filterstring = ""
    
    for i in filters:
        if i == 1:
            filterstring = "&rh=n%3A172282"
            break

    numfilters = 0
    for i in range(len(filters)):
        if filters[i] == 1:
            if i == 1:
                filterstring += "%2Cp_n_condition-type%3A2224371011"
            if i == 2:
                filterstring += "%2Cp_76%3A1249137011"
            numfilters += 1

    URL = 'https://www.amazon.com/s?k=' + searchterm + filterstring
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
                print(str(names[i]) + ': ' + str(prices[i]) + '\n')
        else:
            for i in range(len(all_items)):
                print(str(names[i]) + ': ' + str(prices[i]) + '\n')
    
    except AttributeError:
        print("Item could not be found on Amazon.")

#filter[0] = not used, filter[1] = new, filter[2] = free shipping
filter = [0, 1, 0]
AmazonRequest("3070", 4, filter)