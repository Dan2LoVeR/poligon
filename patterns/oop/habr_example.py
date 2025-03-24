class AnimeCharacter:
    default_status = 'main_character'

    def __init__(self, name, anime, team, gender='female'):
        self.name = name
        self.surname = anime
        self.team = team
        self.__gender = gender # private attribute

    def get_character(self):
        return f'{self.name}'

    @classmethod
    def get_default_status(cls):
        return cls.default_status

    @staticmethod
    def get_talk():
        return 'Озвучивал Анкорд'

class FilmCharacter(AnimeCharacter):
    def

luffy = AnimeCharacter('Луффи', 'One Piece', 'Мугивары', 'male')

print(luffy.get_character())
print(luffy.get_default_status())
print(luffy.get_talk())
# Output: Луффи main_character Озвучивал Анкорд
