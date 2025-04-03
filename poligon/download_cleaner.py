from pathlib import Path
import shutil
import asyncio

main_path = Path('C:/Users/d.valov')

downloads_path = main_path / 'Downloads'
documents_path = main_path / 'Documents'

class Files:
    def __init__(self, category: str, suffixes: str):
        self.category = category
        self.suffixes = suffixes

    async def start_clean(self):
        for suffix in self.suffixes:
            for file in downloads_path.rglob(f"*.{suffix}"):
                shutil.move(file.absolute(), documents_path / self.category)
                print(f'Found {self.category}  file: {file.absolute()}')

async def main():

    file_forms = {
        'docs': {'docx', 'pdf'},
        'tables': {'xlsx', 'xls'}
    }
    cleaners = [Files(category, suffixes).start_clean() for category, suffixes in file_forms.items()]
    await asyncio.gather(*cleaners)

    print(')')

if __name__ == "__main__":
    asyncio.run(main())
