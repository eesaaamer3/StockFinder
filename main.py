import requests
from bs4 import BeautifulSoup

URL = 'https://ca.finance.yahoo.com/world-indices'
page = requests.get(URL).text

page_data = BeautifulSoup(page, "html.parser")


stock_name = page_data.find('td', attrs={'class': 'data-col1 Ta(start) Pend(10px)'})
price_box = page_data.find('td', attrs={'class': 'data-col2 Ta(end) Pstart(20px)'})

stock = stock_name.text.strip()
price = price_box.text.strip()

print(stock)
print(price)