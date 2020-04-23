import requests
from bs4 import BeautifulSoup

URL = 'https://ca.finance.yahoo.com/world-indices'
page = requests.get(URL).text

page_data = BeautifulSoup(page, "html.parser")
print(page_data.prettify())