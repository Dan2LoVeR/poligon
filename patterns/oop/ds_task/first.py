import asyncio


class Bear:
    def __init__(self, country: str, color: str):
        self.country = country
        self.color = color

    async def dance(self):
        print(f'{self.country} танец')

    async def hug(self):
        print(f'пушистые, {self.color} объятия')


async def main():
    bear_list = {
        'белый': 'антарктический',
        'бурый': 'русский'
    }

    bears_party = [Bear(country, color).dance() for color, country in bear_list.items()]
    bears_dead = [Bear(country, color).hug() for color, country in bear_list.items()]
    

    await asyncio.gather(*bears_party)
    await asyncio.gather(*bears_dead)


if __name__ == "__main__":
    asyncio.run(main())