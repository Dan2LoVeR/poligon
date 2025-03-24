from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.filters import Command
import asyncio

API_TOKEN = "7659239800:AAHcmI5LTkst5maCEP_2941gcvsf2eV9b-E"

# Создаем меню в виде колонок
def create_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Клетка")],
        ],
        resize_keyboard=True
    )

def create_cell_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Химический состав клетки")],
            [KeyboardButton(text="Генетический аппарат клетки")],
            [KeyboardButton(text="Строение клетки")],
            [KeyboardButton(text="Размножение клетки")],
            [KeyboardButton(text="Биосинтез белка")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )

def create_subtopic_menu(subtopics):
    keyboard = [[KeyboardButton(text=key)] for key in subtopics]
    keyboard.append([KeyboardButton(text="Назад")])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Указываем пути к изображениям таблиц
table_images = {
    "Основные функциональные группы в клетке": "table/table2.jpg",
    "Основные компоненты клетки": "table/table3.jpg",
    "Моно- и полисахариды": "table/table5.jpg",
    "Структура белка": "table/table6.jpg",
    "Физиологическая роль элементов в клетке": "table/table21.jpg",
    "Сравнение прокариот и эукариот": "table/table22.jpg",
    "Нуклеиновые кислоты": "table/table79.jpg",

    "Азотистые основания": "table/table8.jpg",
    "Компоненты нуклеиновых кислот": "table/table10.jpg",
    "Правила комплементарности": "table/table11.jpg",
    "Сравнение ДНК и РНК": "table/table12.jpg",
    "Структура клетки": "table/table14.jpg",
    "Митохондрии": "table/table15.jpg",
    "Микротрубочки": "table/table16.jpg",
    "Центриоль": "table/table1.jpg",
    "Клеточные органеллы": "table/table23.jpg",
    "Двумембранные органеллы": "table/table24.jpg",
    "Строение мембраны": "table/table25.jpg",
    "Клеточный цикл": "table/table17.jpg",
    "Митоз": "table/table18.jpg",
    "Кинетохор": "table/table19.jpg",
    "Термины, связанные с транскрипцией": "table/table20.jpg"
}

# Содержимое тем
content = {
    "Химический состав клетки": {
        "Клетки имеют свой химический состав": """•	Макроэлементы (98%) – O, C, H, N.
        •	Микроэлементы (1,9%) – K, P, S, Mg, Cl, Ca, Na, Fe.
        •	Ультрамикроэлементы (0,01%) – I, Cu, Co, Zn, Mo, Br, Mn, B и др.
        •	Вода в среднем составляет 80% массы клетки (до 95% — в клетках медузы, 90% — в клетках зародыша человека, 79% — в мышцах сердца, 60% в старых клетках и 10% — в клетках эмали зубов). Вода находится в клетках в двух формах: в свободной — 95%.
        """,
        "Основные функциональные группы в клетке": "Изображение таблицы будет отправлено.",
        "Основные компоненты клетки": "Изображение таблицы будет отправлено.",
        "Моно- и полисахариды": "Изображение таблицы будет отправлено.",
        "Структура белка": "Изображение таблицы будет отправлено.",
        "Физиологическая роль элементов в клетке": "Изображение таблицы будет отправлено.",

    },
    "Генетический аппарат клетки": {
        "Сравнение прокариот и эукариот": "Изображение таблицы будет отправлено.",
        "Нуклеиновые кислоты": "Изображение таблицы будет отправлено.",
        "Азотистые основания": "Информация об азотистых основаниях.",
        "Компоненты нуклеиновых кислот": "Изображение таблицы будет отправлено.",
        "Правила комплементарности": "Изображение таблицы будет отправлено.",
        "Сравнение ДНК и РНК": "Изображение таблицы будет отправлено.",
    },
    "Строение клетки": {
        "Структура клетки": "Изображение таблицы будет отправлено.",
        "Митохондрии": "Изображение таблицы будет отправлено.",
        "Микротрубочки": "Изображение таблицы будет отправлено.",
        "Центриоль": "Изображение таблицы будет отправлено.",
        "Клеточные органеллы": "Изображение таблицы будет отправлено.",
        "Двумембранные органеллы": "Изображение таблицы будет отправлено.",
        "Строение мембраны": "Изображение таблицы будет отправлено.",
    },
    "Размножение клетки": {
        "Клеточный цикл": "Изображение таблицы будет отправлено.",
        "Митоз": "Изображение таблицы будет отправлено.",
        "Кинетохор": "Изображение таблицы будет отправлено.",
    },
    "Биосинтез белка": {
        "Термины, связанные с транскрипцией": "Изображение таблицы будет отправлено.",
    }
    # Добавьте остальные подпункты
}

# Основной код
async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    router = Router()

    @router.message(Command("start"))
    async def start_command(message: Message):
        await message.answer(
            "Приветствуем! Выберите категорию:",
            reply_markup=create_main_menu()
        )

    @router.message(lambda message: message.text == "Клетка")
    async def cell_menu(message: Message):
        await message.answer(
            "Выберите тему:",
            reply_markup=create_cell_menu()
        )

    @router.message(lambda message: message.text in content)
    async def subtopic_menu(message: Message):
        topic = message.text
        subtopics = content[topic]
        await message.answer(
            "Выберите подкатегорию:",
            reply_markup=create_subtopic_menu(subtopics)
        )

    @router.message(lambda message: any(message.text in subtopic for subtopic in content.values()))
    async def subtopic_content(message: Message):
        for topic, subtopics in content.items():
            if message.text in subtopics:
                if message.text in table_images:
                    # Отправка изображения таблицы
                    image_path = table_images[message.text]
                    await message.answer_photo(FSInputFile(image_path))
                else:
                    # Отправка текстового описания
                    response = subtopics[message.text]
                    await message.answer(response)
                break

    @router.message(lambda message: message.text == "Назад")
    async def go_back(message: Message):
        await message.answer(
            "Вы вернулись назад. Выберите тему:",
            reply_markup=create_cell_menu()
        )

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    input("Нажмите Enter, чтобы закрыть...")