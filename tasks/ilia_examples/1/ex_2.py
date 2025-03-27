# Список английских слов (имена, фамилии, абстрактные понятия)
english_list = [
    "John", "Sarah", "Emma", "Michael", "Elizabeth", "William", "James", "Olivia", "Sophia", "Benjamin",
    "Charlotte", "Alexander", "Mia", "Ethan", "Amelia", "Aiden", "Isabella", "Noah", "Emily", "Mason",
    "Ava", "Jacob", "Ella", "Lucas", "Liam",
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Wilson", "Taylor",
    "Anderson", "Thomas", "Moore", "Jackson", "Martin", "Lee", "Perez", "Harris", "Clark", "Ramirez",
    "freedom", "happiness", "friendship", "respect", "kindness", "adventure", "love", "courage", "hope", "peace",
    "success", "dream", "patience", "wisdom", "honesty", "smile", "trust", "laughter", "gratitude", "inspiration",
    "beauty", "nature", "family", "memories", "light", "power", "challenge", "balance", "comfort", "serenity",
    "Oliver", "Mason", "Lily", "Evans", "Scott", "Reed", "Carter", "Turner", "Cooper", "Walker",
    "energy", "creativity", "opportunity", "joy", "bravery", "unity", "hopeful", "vision", "learning", "growth",
    "dedication", "confidence", "expression", "passion", "forgiveness"
]

# Список русских слов (имена, фамилии, абстрактные понятия)
russian_list = [
    "Aleksandr", "Mariya", "Ivan", "Anna", "Dmitrij", "Elena", "Maksim", "Ol'ga", "Sergej", "Natal'ya",
    "Andrej", "Tat'yana", "Nikita", "Ekaterina", "Mihail", "Irina", "Vladimir", "Lyudmila", "Roman", "Svetlana",
    "Evgenij", "Anastasiya", "Konstantin", "YUliya", "Pavel",
    "Ivanov", "Petrov", "Sidorov", "Kuznecov", "Smirnov", "Popov", "Vasil'ev", "Novikov", "Fyodorov", "Morozov",
    "Volkov", "Zajcev", "Solov'yov", "Lebedev", "Kozlov", "Krylov", "Mihajlov", "Belov", "Alekseev", "Makarov",
    "svoboda", "druzhba", "lyubov'", "mir", "radost'", "nadezhda", "sila", "vera", "uspekh", "put'",
    "tvorchestvo", "sem'ya", "vremya", "mechta", "schast'e", "vdohnovenie", "dobro", "krasota", "zhizn'", "mudrost'",
    "garmoniya", "priroda", "znanie", "ulybka", "solnce", "sila", "teplo", "dobrota", "poznanie", "radost'",
    "Nikolaj", "Galina", "Viktor", "Lidiya", "Arkadij", "Elizaveta", "Vasilisa", "Igor'", "Margarita", "Oleg",
    "Grigorij", "YUliya", "Platon", "Kirill", "Vera", "Nadezhda", "Polya", "Olesya", "Stepan", "Leonid",
    "svet", "teplo", "proshchenie", "mechta", "put'"
]


# Функция для преобразования слов в их soundex-коды
def soundex(list):
    # Создаем пустой словарь для хранения слов и их soundex-кодов
    soundex_dict = {}

    # Перебираем каждое слово в переданном списке
    for word in list:
        # Берем первую букву слова как основу кода
        soundex_code = word[0]

        # Обрабатываем остальные буквы слова
        for letter in word[1:]:
            # Заменяем буквы на цифры согласно правилам soundex
            if letter in 'bfpv':
                soundex_code += '1'
            elif letter in 'cgjkqsxz':
                soundex_code += '2'
            elif letter in 'dt':
                soundex_code += '3'
            elif letter in 'l':
                soundex_code += '4'
            elif letter in 'mn':
                soundex_code += '5'
            elif letter in 'r':
                soundex_code += '6'

        # Добавляем слово и его soundex-код в словарь
        soundex_dict[word] = soundex_code

    # Возвращаем заполненный словарь
    return soundex_dict


# Выводим soundex-коды для английских и русских слов
print(soundex(english_list))
print(soundex(russian_list))