import docx
import re

from typing import List, Dict


def generate_html_table(data: List[List[str]], headers: List[str], styles: Dict[str, str] = None) -> str:
    table_styles = ""
    html = '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"></head>'
    if styles:
        table_styles = f' style="{"; ".join([f"{key}: {value}" for key, value in styles.items()])}"'
    html += f"<table class = 'container-xxl table table-info table-striped'>\n"

    html += "  <thead>\n"
    html += "    <tr>\n"
    for header in headers:
        html += f"      <th>{header}</th>\n"
    html += "    </tr>\n"
    html += "  </thead>\n"

    html += "  <tbody>\n"
    napravl = ['Терапев. Отделение', 'Хирур.\nотделение', 'Стоматологотделение', 'Жен.конс.', 'Узкие специалисты']
    for row in data:

        for cell in row:
            if cell in napravl:
                head = headers[:1]+[cell]+headers[2:]
                html += "    <tr>\n"
                for block in head:
                    html += f"      <th>{block}</th>\n"
                html += "    </tr>\n<tr>\n"

            else:
                html += f"      <td>{cell}</td>\n"
        html += "    </tr>\n"
    html += "  </tbody>\n"

    html += "</table>\n"

    return html


styles = {
    "border-collapse": "collapse",
    "width": "50%",
    "margin": "20px auto",
    "border": "1px solid red",
}

doc = docx.Document('График работы на сайт с 07.10.2024. по 12.10.2024.docx')

result = []
keys = None
table1 = doc.tables[0]
for i, row in enumerate(table1.rows):
    text = (cell.text for cell in row.cells)
    row_data = list(text)
    result.append(row_data)

regex = r"[а-яА-Я]{2,3}"
trigger = ['ВЫЗОВА\n', '', 'Бревенник', 'Хабарка']
napravl = ['Терапев. Отделение', 'Хирур. отделение', 'Стоматологотделение',  'Жен.конс.', 'Узкие специалисты']
kab = ['К.1.1.12', 'К.1.1.14', 'Шушкова Е.Д.']
string = ''

for row in result:
    for val in row:
        if row.count(val) > 1 and re.match(regex, val) and val not in trigger or val in kab:
            row.remove(val)
    if row == ['', '', '', '', '', '', '', '', '', '']:
        result.remove(row)

print(result)

headers = result[0]
print()
html_table = generate_html_table(result[1:], headers, styles)
file = open('index.html', 'w', encoding="UTF-8")
file.write(html_table)
file.close()