import requests
from bs4 import BeautifulSoup as BS

url = 'https://mail.google.com/mail/u/0/#inbox'
responce = requests.get(url).text
data = BS(responce, 'html.parser')
print(data)
