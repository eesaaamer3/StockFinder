import requests
from bs4 import BeautifulSoup

URL = 'https://ca.finance.yahoo.com/world-indices'
page_Data = requests.get(URL)