from bs4 import BeautifulSoup
import requests

def DellRequest(searchterm, numresults):
    URL = 'https://www.dell.com/en-us/search/' + searchterm
    
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    
    try:
        # Check if any results are present
        if soup.find('div', class_='zero-results-page'):
            print("Your search returned no results\n")
            exit()
    
        # Get all items listed in the search results
        items = soup.findAll('article', class_='stack-system ps-stack')
    
        # Find each product's name from list of search results and store it
        product_names = []
        for i in items:
            product_names.append(i.find('h3', class_='ps-title').text.replace('\n', '').lstrip().rstrip())
    
        # Find each product's price from list of search results and store it
        product_prices = []
        for i in items:
            product_prices.append(i.find('div', class_='ps-dell-price ps-simplified').text.replace('\n', '')
                                  .replace('Dell Price', '').lstrip().rstrip())
    
        # Print each product and its respective price
        if (numresults <= len(items)):
            for i in range(numresults):
                print(str(product_names[i]) + ': ' + str(product_prices[i]))
        else:
            for i in range(len(items)):
                print(str(product_names[i]) + ': ' + str(product_prices[i]))
    
    except AttributeError:
        print("error")
        
DellRequest("Laptop", 3)