from xml.etree import ElementTree as et
import pandas as pd
import zipfile as zp
from pathlib import Path

# pip install pandas
# pip install elementpath
def zip_open():
    dir = Path.parts
    print(dir)


def main():
    zip_open()
    # переменные с файлами
    f_lom = 'LOM290104S29030_2407180.xml'
    f_dom = 'DOM290104S29030_2407180.xml'
    f_vm = 'VM290104S29030_2407180.xml'

    # преобразование xml файлов для их чтения(сократил запись)
    lom = (et.parse(f_lom)).getroot()
    dom = (et.parse(f_dom)).getroot()
    vm = (et.parse(f_vm)).getroot()

    # инициализация списков в которые заносятся данные из парсинга
    # и в конечном счёте добавления их в словарь с результатом(result)
    pers_list = []
    visit_list = []
    bd_list = []
    fall_list = []

    # циклы где сначала парсится файл VM: COMMENT-комментарий об ошибке; ID_PAC- id пациента; N_ZAP-номер записи
    # далее циклом находим пользователя в LOM, где находим его ФИО(FAM, IM, OT) и дату рождения(DR)
    # так же находим номер записи(Z_SL/SL/NHISTORY) в DOM
    # все данные хранятся в строковом значении(str)
    for fall in vm.findall('PR'):
        fall_list.append(fall.find('COMMENT').text)
        for pers in lom.findall('PERS'):
            if fall.find('ID_PAC').text == pers.find('ID_PAC').text:
                pers_list.append([pers.find('FAM').text,
                                  pers.find('IM').text,
                                  pers.find('OT').text, ])
                bd_list.append(pers.find('DR').text)
        for visit in dom.findall('ZAP'):
            if fall.find('N_ZAP').text == visit.find('N_ZAP').text:
                visit_list.append(visit.find('Z_SL/SL/NHISTORY').text)

    # тот самый словарь с результатом для более удобного занесения итоговых значений в excel
    # все данные хранятся в строковых значениях(str)
    result = {
        "Номер истории болезни": visit_list,
        "ФИО": pers_list,
        "ДР": bd_list,
        "Ошибка": fall_list
    }

    # занесение словаря с результатом в excel и его сохранение
    df = pd.DataFrame(result)
    df.to_excel('test.xlsx')


if __name__ == '__main__':
    main()
