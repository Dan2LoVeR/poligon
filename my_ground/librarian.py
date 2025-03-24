import os
import shutil
from datetime import datetime


def sortbook():
    download_path = "C:/Users/данча/Downloads"
    tree = os.listdir(download_path)
    now_date = (datetime.today()).strftime('%d_%m_%Y')
    books_today = []

    for i in tree:
        mtime = os.path.getmtime(download_path + '/' + i)
        mtimesreadable = datetime.fromtimestamp(mtime).strftime('%d_%m_%Y')
        if mtimesreadable == now_date:
            books_today.append([download_path + '/' + i, i])
    return books_today


def main():
    book_f = "D:\\driveinfo.calibre"
    cd_f = "D:\\con.txt"

    if os.path.exists(book_f):
        print('книга найдена')

    elif os.path.exists(cd_f):
        print('карта памяти найдена')
        list = sortbook()
        for path in list:
            shutil.move(path[0], 'D:/' + path[1])

    elif os.path.exists(book_f) and os.path.exists(book_f):
        print('выберите запоминающее устройство')

    else:
        print('сохранять некуда (')


if __name__ == '__main__':
    main()
