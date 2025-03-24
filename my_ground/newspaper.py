import os
from bs4 import BeautifulSoup
import requests
import datetime
import json
import random
from fake_useragent import UserAgent

def news_parsing():
    ua = UserAgent()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-Agent': ua.google,
    }
    article_dict = {}
    url = f'https://habr.com/en/articles/'
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    all_hrefs_article = soup.find_all('a', class_='tm-title__link')
    for article in all_hrefs_article:
        article_name = article.find('span').text
        artikle_link = f'https://habr.com{article.get("href")}'
        article_dict[article_name] = artikle_link
    with open(f"articles_{datetime.datetime.now().strftime('%d_%m_%Y')}.json", "w", encoding='utf-8') as f:
        try:
            json.dumb(article_dict, f, indent=4, ensure_ascii=False)
            print('статьи получены)')
        except:
            print('получить статьи не получилось(')


def main():
    # блок для проверки видит ли книгу прога
    book_f = "D:\\driveinfo.calibre"
    if os.path.exists(book_f):
        print('книга найдена)')
    else:
        print('книга не найдена(')

    news_parsing()


if __name__ == "__main__":
    main()
