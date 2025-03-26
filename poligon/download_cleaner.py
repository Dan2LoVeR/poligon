from pathlib import Path
import shutil
import asyncio

main_path = Path('C:/Users/d.valov')

test_file = Path('C:/Users/d.valov/Downloads/Калькулятор_ЗП омс.xlsx')
downloads_path = main_path / 'Downloads'
documents_path = main_path / 'Documents'
print(type(test_file.suffix))

class Files:
    def __init__(self, suffixes: str):
        self.suffixes = suffixes

    async def start_clean(self):
        for suffix in self.suffixes:
            for file in downloads_path.rglob(f"*.{suffix}"):

                print(f'Found {suffix} file: {file.name}')

async def main():

    file_forms = {
        'doc': {'docx', 'pdf'},
        'table': {'xlsx'}
    }
    cleaners = [Files(suffixes).start_clean() for suffixes in file_forms.values()]
    await asyncio.gather(*cleaners)

    print(')')

if __name__ == "__main__":
    asyncio.run(main())
