from bs4 import BeautifulSoup
import requests

def AcerRequest(brandname, searchterm, numresults, filters):
    URL = 'https://store.acer.com/en-us/catalogsearch/result/?q=' + brandname + searchterm
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:
        # Get all items listed in the search results
        items = soup.findAll("li", attrs={"class": "item product product-item"})
    
        # Find each product's name from list of search results and store it
        product_names = []
        for item in items:
            product_names.append((item.find("a", attrs={"class": "product-item-link"})).string.replace('\n', '').lstrip().rstrip())
        
        # Check if there are any search results
        if len(product_names) == 0:
            products = ["Acer:", "Your search returned no results.", ""]
            return products
        
        # Find each product's price from list of search results and store it
        product_prices = []
        for i in items:
            product_prices.append(i.find("span", attrs={"class": "price"}).string)

        # Print each product and its respective price
        products = ['Acer:']
        if (numresults <= len(items)):
            for i in range(numresults):
                products.append(str(product_names[i]) + ': ' + str(product_prices[i]))
        else:
            for i in range(len(items)):
                products.append(str(product_names[i]) + ': ' + str(product_prices[i]))
        products.append("")
        return products
    
    except AttributeError:
        return "Acer Error"

def AmazonRequest(brandname, searchterm, numresults, filters):
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

    URL = 'https://www.amazon.com/s?k=' + brandname + searchterm + filterstring
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try: 
        # Get all HTML product names and prices from first results page
        all_items = soup.findAll("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
        all_prices = soup.findAll("span", attrs={"class": 'a-offscreen'})

        # Find and select each products price from the filtered HTML code
        prices = []
        for item in all_prices:
            prices.append(item.string)
        
        # Check if there are any search results
        if len(all_items) == 0:
            products = ["Amazon:", "Your search returned no results.", ""]
            return products
        
        # Find and select each products name from the filtered HTML code
        names = []
        for item in all_items:
            names.append(item.string)
        
        # Constructs a list of products and their respective prices
        products = ['Amazon:']
        if (numresults <= len(all_items)):
            for i in range(numresults):
                products.append(str(names[i]) + ': ' + str(prices[i]))
        else:
            for i in range(len(all_items)):
                products.append(str(names[i]) + ': ' + str(prices[i]))
        products.append("")
        return products
    
    except AttributeError:
        return "Amazon Error"

def BestBuyRequest(brandname, searchterm, numresults, filters):
    
    filterstring = "st="
    if (filters[1] == 1) and (filters[2] == 0):
        filterstring = "id=pcat17071&qp=condition_facet%3DCondition~New&st="
    if (filters[1] == 1) and (filters[2] == 1):
        filterstring = "id=pcat17071&qp=condition_facet%3DCondition~New%5Ecurrentoffers_facet%3DCurrent%20Deals~Free%20Shipping%20Eligible&st="
    if (filters[1] == 0) and (filters[2] == 1):
        filterstring = "id=pcat17071&qp=currentoffers_facet%3DCurrent%20Deals~Free%20Shipping%20Eligible&st="
    
    URL = 'https://www.bestbuy.com/site/searchpage.jsp?' + filterstring + brandname + searchterm
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:
        # Check if there are any search results
        if (soup.find('div', attrs={"class": "no-results-copy"})):
            products = ["BestBuy:", "Your search returned no results.", ""]
            return products
        
        # Filter down HTML code for later find functions.
        all_items = soup.findAll('div', attrs={"class": "shop-sku-list-item"})
        all_prices = soup.findAll('div', attrs={"class": "priceView-hero-price priceView-customer-price"})
        
        # Find and select each products price from the filtered HTML code
        prices = []
        for item in all_prices:
            prices.append(item.find('span', attrs={"aria-hidden": "true"}).string)
        
        # Find and select each products name from the filtered HTML code
        names = []
        for item in all_items:
            names.append(item.find('h4', attrs={"class": "sku-title"}).find('a').string)
        
        # Prints products and their respective prices
        products = ['BestBuy:']
        if (numresults <= len(all_prices)):
            for i in range(numresults):
                products.append(str(names[i]) + ': ' + str(prices[i]))
        else:
            for i in range(len(all_prices)):
                products.append(str(names[i]) + ': ' + str(prices[i]))
        products.append("")
        return products
    
    except AttributeError:
        return "BestBuy Error"

def BHRequest(brandname, searchterm, numresults, filters):
    
    filterstring = ""
    
    if (filters[0] == 1) and (filters[2] == 0):
        filterstring = "&filters=fct_a_filter_by%3A03_INSTOCK"  
    if (filters[0] == 1) and (filters[2] == 1):
        filterstring = "&filters=fct_a_filter_by%3A01_FREESHIP%7C03_INSTOCK"
    if (filters[0] == 0) and (filters[2] == 1):
        filterstring = "&filters=fct_a_filter_by%3A01_FREESHIP"  
    
    URL = 'https://www.bhphotovideo.com/c/search?q=' + brandname + searchterm + filterstring
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:    
        # Gets all HTML prices and product names from the first results page
        all_prices = soup.findAll("span", attrs={"data-selenium":"uppedDecimalPrice"})
        all_names = soup.findAll("span", attrs={"data-selenium":"miniProductPageProductName"})
        
        # Check if there are any search results
        if ((len(all_names) and len(all_prices)) == 0):
            products = ["BH:", "Your search returned no results.", ""]
            return products
            
        # Find and select each products price in dollars and cents and then join them together to form the whole price.
        price_whole = []
        for item in all_prices:
            curr_dollar = item.find("span", attrs={"data-selenium":"uppedDecimalPriceFirst"}).string
            curr_cent = item.find("sup", attrs={"data-selenium":"uppedDecimalPriceSecond"}).string
            price_whole.append(curr_dollar + "." + curr_cent)
            
        # Prints products and their respective prices'
        products = ['B&H:']
        if (numresults <= len(all_prices)):
            for i in range(numresults):
                products.append(str(all_names[i].string) + ': ' + str(price_whole[i]))
        else:
            for i in range(len(all_prices)):
                products.append(str(all_names[i].string) + ': ' + str(price_whole[i]))
        products.append("")
        return products
    
    except AttributeError:
        return "B&H Error"

def DellRequest(brandname, searchterm, numresults, filters):
    URL = 'https://www.dell.com/en-us/search/' + brandname + searchterm
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:

    
        # Get all items listed in the search results
        items = soup.findAll('article', attrs={'class':'stack-system ps-stack'})
    
        # Find each product's name from list of search results and store it
        product_names = []
        for i in items:
            product_names.append(i.find('h3', attrs={'class': 'ps-title'}).text.replace('\n', '').lstrip().rstrip())
        
        # Check if there are any search results
        if len(items) == 0:
            products = ["Dell:", "Your search returned no results.", ""]
            return products
        
        # Find each product's price from list of search results and store it
        product_prices = []
        for i in items:
            product_prices.append(i.find('div', attrs={'class': 'ps-dell-price ps-simplified'}).text.replace('\n', '').replace('Dell Price', '').lstrip().rstrip())
    
        # Print each product and its respective price
        products = ['Dell:']
        if (numresults <= len(items)):
            for i in range(numresults):
                products.append(str(product_names[i]) + ': ' + str(product_prices[i]))
        else:
            for i in range(len(items)):
                products.append(str(product_names[i]) + ': ' + str(product_prices[i]))
        products.append("")
        return products
    
    except AttributeError:
        return "Dell Error"

def NeweggRequest(brandname, searchterm, numresults, filters):
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
    
    URL = 'https://www.newegg.com/p/pl?d=' + brandname + searchterm + filterstring
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:
        # Check if there are any search results
        if (soup.find('span', attrs={"class", "result-message-error"})):
            products = ["Newegg:", "Your search returned no results.", ""]
            return products
        
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
        products = ['Newegg:']
        numresults += 1
        if (numresults <= len(all_prices)):
            for i in range(1, numresults):
                products.append(str(all_names[i].string) + ': $' + str(price_whole[i]))
        else:
            for i in range(1, (len(all_prices)-2)):
                products.append(str(all_names[i].string) + ': $' + str(price_whole[i]))
        products.append("")
        return products
    
    except AttributeError:
        return "Newegg Error"

def WalmartRequest(brandname, searchterm, numresults, filters):
    
    filterstring = ""
    if filters[0] == 1:
        filterstring = "&facet=exclude_oos%3AShow+available+items+only"
    if (filters[0] == 1) and (filters[1] == 1):
        filterstring = "%7C%7Cexclude_oos%3AShow+available+items+only"
    if (filters[0] == 0) and (filters[1] == 1):
        filterstring = "&facet=condition%3ANew"
    URL = 'https://www.walmart.com/search?q=' + brandname + searchterm + filterstring
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:    
        # Gets all HTML prices and product names from the first results page
        all_prices = soup.findAll("div", attrs={"data-automation-id":"product-price"})
        all_names = soup.findAll("span", attrs={"data-automation-id":"product-title"})

        # Check if there are any search results
        if len(all_names) == 0:
            products = ["Walmart:", "Your search returned no results.", ""]
            return products
        
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
            
        # Constructs a list of products and their respective prices
        products = ['Walmart:']
        
        if (numresults <= len(all_prices)):
            for i in range(numresults):
                tempval = str(names[i].string)+ ': ' + str(prices[i])
                products.append(tempval)
        elif 10 > len(all_prices):
            for i in range(len(all_prices)):
                tempval = str(names[i].string)+ ': ' + str(prices[i])
                products.append(tempval)
        else:
            for i in range(10):
                tempval = str(names[i].string)+ ': ' + str(prices[i])
                products.append(tempval)
        products.append("")
        return products
    
    except AttributeError:
        return "Walmart Error"