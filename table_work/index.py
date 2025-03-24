import os
import pandas as pd

main_fail = 'table/Мед реабилитация для СОГАЗ.xlsx'

df = pd.read_excel(main_fail, skiprows=4, usecols=['Дата',
                                                        'услуга',
                                                        'УЕТ',
                                                        'время нахожденя в отделении'])

df_main = (df[df.isnull().any(axis=1)]).values.tolist()

uet_mas = []


for uet in df_main:
    if uet[3].isnull():
        uet_mas.append([uet[1], uet[3]])

print(uet_mas)