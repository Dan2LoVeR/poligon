import pandas as pd
import openpyxl
from xml.etree import ElementTree as ET

def create_tree(const, constanta):
    new_elem = ET.Element('new_tag')
    new_elem.set('attribute_name', 'attribute_value')
    new_elem.text = 'element_text'
    const.append(new_elem)
    constanta.write('test.xml')

def main():
    tree = ET.parse('test.xml')
    root = tree.getroot()
    data = pd.read_excel('test.xlsx')
    print(data.head())
    create_tree(root,tree)

if __name__ == "__main__":

    main()