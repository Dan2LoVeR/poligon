import json

with open("result.json", 'rb') as f:
    data = json.load(f)

list = data['messages']

count_mess_dan = 0
count_mess_vik = 0
count_love = 0
text_mes = []
# кто больше пишет, самое популярное сообщение/слово
# количество упоминаний о любви,
for mess in list:
    if 'from' in mess:

        if mess['from'] == '❤️Вика❤️':
            count_mess_vik += 1
        elif mess['from'] == 'Даня':
            count_mess_dan += 1
        else:
            continue



    if "text_entities" in mess and mess['text_entities']:
        text_mes.append(mess['text_entities'][0]["text"])
        love_words = ['люблю тебя', 'я тебя люблю', 'любимый', 'любимая']
        if mess['text_entities'][0]["text"] in love_words :
            count_love += 1

print(count_mess_dan, count_mess_vik, count_love)
print(sorted(text_mes))
