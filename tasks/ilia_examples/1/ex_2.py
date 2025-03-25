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

def soundex(list):
    soundex_dict = {}
    for word in list:
        soundex_code = word[0]
        for letter in word[1:]:
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
        soundex_dict[word] = soundex_code
    return soundex_dict

print(soundex(english_list))
print(soundex(russian_list))


