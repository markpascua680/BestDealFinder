
from bs4 import BeautifulSoup
import requests
 
URL = 'https://www.amazon.com/Noctua-redux-1700-high-Performance-Award-Winning-Affordable/dp/B07CG2PGY6/ref=sr_1_1_sspa?crid=36F410L4YBBCC&keywords=pc+fan&qid=1663710594&sprefix=pc+fa%2Caps%2C201&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFDOTBQTkc5Q004MjMmZW5jcnlwdGVkSWQ9QTA4Nzc2OTcyM1RIVTRLVkM4MjlHJmVuY3J5cHRlZEFkSWQ9QTA1OTE2MjU5UExZVDU4MFRZSUYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

File = open("out.csv", "a")
 
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
 
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

try: 
    title = soup.find("span", attrs={"class": 'a-offscreen'})
    title_value = title.string
    title_string = title_value.strip().replace(',', '')
    print(title_string)
except AttributeError:
    title_string = "NA"
    print("product Title = ", title_string)