import json
from bs4 import BeautifulSoup as Soup
from pathlib import Path
path = "metadata.calibre"
xml_path = 'D:/Digital Editions/BookHistory.xml'

with open(path, 'r') as file:
    data = json.load(file)
count = 0
for item in data:
    count += 1




if __name__ == '__main__':
    with open(xml_path, 'r', encoding='utf-8') as xml:
        soup = Soup(xml.read(), 'xml')

    book_list = []
    for elem in soup.find_all('history'):
        book_list.append([
            elem.find('bookId').text,
            elem.find('lastReadProc').text
        ])


    


    print(count)

    directory = Path('D:/Digital Editions/BookInformations/D')
    count = 0
    for filepath in directory.rglob('*'):
        if filepath.is_file():

            with open(filepath, 'r', encoding='utf-8') as xml_inf:
                book_inf = Soup(xml_inf.read(), 'xml')

            book_id = book_inf.find('id').text

            for book in book_list:
                if book_id in book:
                    count+=1
                    book_name = book_inf.find('fileName').text
                    book_open = book_inf.find('readTimes').text
                    print(book_name, book_open, book_id, book[1])
    print(count)
