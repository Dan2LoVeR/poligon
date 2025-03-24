import requests
from bs4 import BeautifulSoup as BS
import re
import os
import shutil
from datetime import datetime


def svodka():
    url = 'https://erotorrent.ru/'
    response = requests.get(url).text
    data = BS(response, 'html.parser')
    count = 0
    for block in data.find_all('div', class_='short_news'):
        if count <= 9:
            game = {
                'title': block.find('span').text,
                'date': block.find('div', class_='over_right').text,
                'tags': block.find('div', class_='over_right_cat').text,
            }
            count+=1
        else:
            break

        print(game)
        
    url = 'https://briefly.ru/nonfiction/'
    response = requests.get(url).text
    data = BS(response, 'html.parser')
    article_block = data.find('div', class_='index alphabet')
    for article in article_block.find_all('li'):
        title = (article.find_all('a'))[1]
        print(title.text, '=>', title['href'])


def habr(path):
    url = 'https://habr.com/ru/feed/'
    response = requests.get(url).text
    data = BS(response, 'html.parser')

    count = []
    for article in data.find_all('h2', class_='tm-title tm-title_h2'):
        title = re.sub(r'[^\w\s]', '', article.a.span.text)

        link = 'https://habr.com' + article.a['href']
        open_url = requests.get(link)
        with open(f"{path}/daily/II/{title}.html", 'w', encoding='utf-8') as file:
            file.write(open_url.text)

def main():
    book_f = ["D:\\driveinfo.calibre", "E:\\driveinfo.calibre"]

    svodka()
    if os.path.exists(book_f[0]) or os.path.exists(book_f[1]):
        if os.path.exists(book_f[0]):
            file_path = 'D:\\'
        else:
            file_path = 'E:\\'



    else:
        print('сохранять некуда (')

if __name__ == '__main__':
    main()


