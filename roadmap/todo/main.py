import requests
from bs4 import BeautifulSoup as BS

url_map = 'https://ximepa.ru/load/27-1-2'
responce = requests.get(url_map).text
data = BS(responce, 'html.parser')
print(data)