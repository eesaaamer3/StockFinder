import requests
from bs4 import BeautifulSoup

URL = 'https://ca.finance.yahoo.com/world-indices'
page = requests.get(URL).text

stock_data = []

page_data = BeautifulSoup(page, "html.parser")

stock_table = page_data.find('table').find("tbody").find_all('tr')

for row in stock_table:
    stock_data.append(list([row.find('td', attrs={'class': 'data-col1 Ta(start) Pend(10px)'}).text.strip(), row.find('td', attrs={'class': 'data-col2 Ta(end) Pstart(20px)'}).text.strip(), row.find('td', attrs={'class': 'data-col3 Ta(end) Pstart(20px)'}).text.strip(),  row.find('td', attrs={'class': 'data-col4 Ta(end) Pstart(20px)'}).text.strip()]))
