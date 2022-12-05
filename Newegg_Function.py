from bs4 import BeautifulSoup
import requests

def NeweggRequest(searchterm, numresults, filters):
    filterstring = ""
    
    for i in filters:
        if filters[i] == 1:
            filterstring = "&N="
            break

    numfilters = 0
    for i in range(len(filters)):
        if filters[i] == 1:
            if numfilters > 0:
                filterstring += "%20"
            if i == 0:
                filterstring += "4131"
            if i == 1:
                filterstring += "4814"
            if i == 2:
                filterstring += "4808"
            numfilters += 1

    print(filterstring)
    
    URL = 'https://www.newegg.com/p/pl?d=' + searchterm + filterstring
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:
        # Checks if any results are present.
        if (soup.find('span', attrs={"class", "result-message-error"})):
            print("Your search returned no results\n")
        
        # Gets all HTML prices and product names from the first results page
        all_prices = soup.findAll("li", attrs={"class":"price-current"})
        all_names = soup.findAll('a', attrs={"class":'item-title'})

        # Find and select each products price in dollars and cents and then join them together to form the whole price.
        i = 0
        price_whole = []
        valid_name = []
        for item in all_prices:
            
            if (str(item) != '<li class="price-current"></li>'):
                valid_name.append(all_names[i])
                i += 1
                
                curr_dollar = item.find('strong').string
                curr_cent = item.find('sup').string
                price_whole.append(curr_dollar + curr_cent)
            
        # Prints products and their respective prices
        numresults += 1
        if (numresults <= len(all_prices)):
            for i in range(1, numresults):
                print(str(all_names[i].string) + ': $' + str(price_whole[i]) + '\n')
        else:
            for i in range(1, (len(all_prices)-2)):
                print(str(all_names[i].string) + ': $' + str(price_whole[i]) + '\n')
    
    except AttributeError:
        print("Item could not be found")
        
#filter[0] = in stock, filter[1] = new, filter[2] = free shipping
filter = [0, 0, 0]

NeweggRequest("3070", 4, filter)