from pathlib import Path
import shutil
import asyncio

main_path = Path('C:/Users/d.valov')

test_file = Path('C:/Users/d.valov/Downloads/Калькулятор_ЗП омс.xlsx')
downloads_path = main_path / 'Downloads'
documents_path = main_path / 'Documents'
print(type(test_file.suffix))

class Files:
    def __init__(self, suffix: str):
        self.suffix = suffix

    async def start_clean(self):
        for file in downloads_path.rglob(f"*.{self.suffix}"):
            print(file)

async def main():

    file_forms = {
        'doc': {'docx', 'pdf'},
        'table':'xlsx'
    }
    cleaners = [Files(fmt).start_clean() for fmt in file_forms]
    print(type(cleaners))
    print(cleaners)
    await asyncio.gather(*cleaners)

    print(')')

if __name__ == "__main__":
    asyncio.run(main())
