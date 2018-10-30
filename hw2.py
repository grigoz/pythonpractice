# 1
import copy
geo_logs = [
['visit1', ['Москва', 'Россия']],
['visit2', ['Дели', 'Индия']],
['visit3', ['Владимир', 'Россия']],
['visit4', ['Лиссабон', 'Португалия']],
['visit5', ['Париж', 'Франция']],
['visit6', ['Лиссабон', 'Португалия']],
['visit7', ['Тула', 'Россия']],
['visit8', ['Тула', 'Россия']],
['visit9', ['Курск', 'Россия']],
['visit10', ['Архангельск', 'Россия']],
]
a = []
for element in geo_logs:
    if element[1][1] == 'Россия':
        a.append(element)
geo_logs.clear()
geo_logs =copy.copy(a)
print(geo_logs)
# 2
ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}
unique = []

for value in ids.values():
    for element in value:
        if element not in unique:
            unique.append(element)
print(unique)

# 3
queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]
i = 0
r = 0
t = 0
for q in queries:
    a = q.split(' ')
    if len(a) == 3:
        i += 1
    if len(a) == 2:
        r += 1
    if len(a) == 1:
        t += 1
print('Запросов из 3 слов: {}%'.format(i/len(queries)*100))
print('Запросов из 2 слов: {}%'.format(r/len(queries)*100))
print('Запросов из 1 слова: {}%'.format(t/len(queries)*100))

# 4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
print(max(stats))

# 5
stream = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]
stream_list = []
for e in stream:
    stream_list.append(e.split(','))
unique_ids = len(set(line[1] for line in stream_list))
views = sum([int(line[2]) for line in stream_list])
print(views/unique_ids)

# 6
stats = [
['2018-01-01', 'google', 25],
['2018-01-01', 'yandex', 65],
['2018-01-01', 'market', 89],
['2018-01-02', 'google', 574],
['2018-01-02', 'yandex', 249],
['2018-01-02', 'market', 994],
['2018-01-03', 'google', 1843],
['2018-01-03', 'yandex', 1327],
['2018-01-03', 'market', 1764],
]
query = ['2018-01-01', 'google']
for i in range(len(stats)):
        if query[0] == stats [i][0] and query[1] == stats[i][1]:
            print(stats[i][2])
