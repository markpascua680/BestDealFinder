from bs4 import BeautifulSoup
import requests
 
def BestBuyRequest(searchterm, numresults, filters):
    
    filterstring = "st="
    if (filters[1] == 1) and (filters[2] == 0):
        filterstring = "id=pcat17071&qp=condition_facet%3DCondition~New&st="
    if (filters[1] == 1) and (filters[2] == 1):
        filterstring = "id=pcat17071&qp=condition_facet%3DCondition~New%5Ecurrentoffers_facet%3DCurrent%20Deals~Free%20Shipping%20Eligible&st="
    if (filters[1] == 0) and (filters[2] == 1):
        filterstring = "id=pcat17071&qp=currentoffers_facet%3DCurrent%20Deals~Free%20Shipping%20Eligible&st="
    
    URL = 'https://www.bestbuy.com/site/searchpage.jsp?' + filterstring + searchterm
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:
        if (soup.find('div', attrs={"class": "no-results-copy"})):
            print("Your search returned no results\n")
        
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
        if (numresults <= len(all_prices)):
            for i in range(numresults):
                print(str(names[i]) + ': ' + str(prices[i]))
        else:
            for i in range(len(all_prices)):
                print(str(names[i]) + ': ' + str(prices[i]))
                
    except AttributeError:
        print("error")


#filter[0] = not used, filter[1] = new, filter[2] = free shipping
filter = [0, 1, 1]
BestBuyRequest("3090", 4, filter)