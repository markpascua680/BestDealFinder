from bs4 import BeautifulSoup
import requests


def WalmartRequest(searchterm, numresults, filters):
    
    filterstring = ""
    if filters[0] == 1:
        filterstring = "&facet=exclude_oos%3AShow+available+items+only"
    if (filters[0] == 1) and (filters[1] == 1):
        filterstring = "%7C%7Cexclude_oos%3AShow+available+items+only"
    if (filters[0] == 0) and (filters[1] == 1):
        filterstring = "&facet=condition%3ANew"
    URL = 'https://www.walmart.com/search?q=' + searchterm + filterstring
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:    
        # Gets all HTML prices and product names from the first results page
        all_prices = soup.findAll("div", attrs={"data-automation-id":"product-price"})
        all_names = soup.findAll("span", attrs={"data-automation-id":"product-title"})

        # Checks if any results are present.
        if len(all_names) == 0:
            print("Your search returned no results\n")
        
        # Find and select each product price from the filtered HTML code. Remove any unnecessary words from filtered results.
        prices = []
        for item in all_prices:
            val = item.find("div").string
            templist = list()
            templist.extend(val)
            if (templist[0] == 'N'):
                fixedval = ""
                for item in templist:
                    if ((item != 'N') and (item != 'o') and (item != 'w') and (item != ' ')):
                        fixedval +=item
                prices.append(fixedval)
            else:
                prices.append(val)
        
        # Find and select each product name from the filtered HTML code.
        names = []
        for item in all_names:
            names.append(item.string)
            
        # Prints products and their respective prices
        if (numresults <= len(all_prices)):
            for i in range(numresults):
                print(str(names[i].string) + ': ' + str(prices[i]) +'\n')
        elif 10 > len(all_prices):
            for i in range(len(all_prices)):
                print(str(names[i].string) + ': ' + str(prices[i]) +'\n')
        else:
            for i in range(10):
                print(str(names[i].string)+ ': ' + str(prices[i]) +'\n')
    
    except AttributeError:
        print("Item could not be found")

#filter[0] = in stock, filter[1] = new, filter[2] = not used
filter = [1, 1, 0]
WalmartRequest("Graphics Card", 4, filter)