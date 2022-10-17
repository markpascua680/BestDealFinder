from bs4 import BeautifulSoup
import requests
 
URL = 'https://www.gamestop.com/search/?q=' + input("Enter product name: ")
 
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate', 'connection': 'keep-alive'})
COOKIES = ({'cmapi_cookie_privacy': 'permit 1,2 functional', 'notice_preferences': '1:', 'cmapi_gtm_bl': 'ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc', 'notice_gdpr_prefs': '0,1:', 'notice_behavior': 'implied,eu'})

webpage = requests.get(URL, headers=HEADERS, cookies=COOKIES)
soup = BeautifulSoup(webpage.content, "lxml")

try:    
    # # Gets all HTML prices and product names from the first results page
    all_prices = soup.findAll('span', attrs={'data-testid':"price-small"})
    # all_names = soup.findAll('div', attrs={'class':"font-body text-sm tracking-n3 pr-1 line-clamp-3 md:pr-0"})
    
    for item in soup:
        print(str(item))
    # Checks if any results are present.
    # if ((len(all_names) and len(all_prices)) == 0):
    #     print("Your search returned no results\n")
        
    # Prints products and their respective prices
    # for i in range(len(all_prices)):
    #     print(str(all_names[i]) + ': ' + str(all_prices[i]) +'\n')

except AttributeError:
    print("Item could not be found")
