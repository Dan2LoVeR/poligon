from xml.etree import ElementTree as et
import pandas as pd

# pip install pandas
# pip install elementpath

#функция для парсинга LOM файла
def parse_tree(item):
    list = []
    # создание списка с личными данными всех пользователей
    for elem in item.iter():
        for elems in elem.findall('PERS'):
            # все данные данного списка хранятся в строковых значениях
            list.append([elems.find('ID_PAC').text,
                         elems.find('FAM').text,
                         elems.find('IM').text,
                         elems.find('OT').text,
                         elems.find('W').text])
    return list


#функция для парсинга DOM файла
def parse_dree(item):
    list = []
    # создание списка с id и суммой услуг всех пользователей
    for elem in item.iter():
        for elems in elem.findall('ZAP'):
            # все данные данного списка хранятся в строковых значениях
            list.append([elems.find('PACIENT/ID_PAC').text,
                         elems.find('Z_SL/SL/SUM_M').text])

    return list


def main():
    # файл LOM()
    f_lom = 'LOM290104S29030_2407167.xml'
    # файл DOM
    f_dom = 'DOM290104S29030_2407167.xml'

    # преобразование xml файлов для их чтения
    lom = et.parse(f_lom)
    lom_tree = lom.getroot()
    lom_list = parse_tree(lom_tree)

    dom = et.parse(f_dom)
    dom_tree = dom.getroot()
    dom_list = parse_dree(dom_tree)

    # список id всех пациентов
    list_id = []
    # список ФИО всех пациентов
    list_fio = []
    # список сумм за услуги всех пациентов
    list_cost = []

    # создание словаря для удобства записи в excel
    for elem in lom_list:
        for elems in dom_list:
            if (elem[0] == elems[0]):
                list_id.append(elems[0])
                list_fio.append(elem[1] + '.' + elem[2] + '.' + elem[3] + '.')
                list_cost.append(float(elems[1]))

                # все списки хранят данные в строковых значениях
                # исключение список cost в нём хранятся числа с плавающей точкой
                result = {
                    'id': list_id,
                    'fio': list_fio,
                    'cost': list_cost,

                }

    # запись результата в excel
    df = pd.DataFrame(result)
    # запись общей суммы всех стоимости услуг в excel
    # значение sum имеет тип число с плавающей точкой
    df.at[0, 'summ'] = sum(list_cost)
    df.to_excel('test.xlsx')


if __name__ == '__main__':
    main()
