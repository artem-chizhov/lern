#    Напишите код для преобразования произвольного списка вида 
#    ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины)
#    в словарь 
# {'2018-01-01': {'yandex': {'cpc': 100}}} 
# {'2018-01-01': {'100': '100'}, 'yandex': {'2018-01-01': '100'}, 'cpc': {'yandex': '100'}, 100: {'cpc': '100'}}            

# a = ['2018-01-01', 'yandex', 'cpc', 100]
# b = dict.fromkeys(a[0:-1], "")

# for i in a:
#     b[i] = {}

# print(b)

dict_ = ['2018-01-01', 'yandex', 'cpc', 100]
last = dict_.pop()

for key_ in reversed(dict_):
    last = {key_: last}

print(last)






                #TASK4
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}                    
# pr = sorted(stats.values())
# print(list(stats.keys())[list(stats.values()).index(pr[-1])])
                    
                
                    
                    #TASK3
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт',
#     'python',
#     'python цикл for continue'
#     ]
# list_word = {}

# for num_ in queries:
#     word_ = len(num_.split())
#     if word_ in list_word:
#         list_word[word_] += 1
#     else:
#         list_word[word_] = int()
#         list_word[word_] += 1

# sum_ = sum(list_word.values())

# for perc in list_word.values():
    # p = 100 / (sum_ / perc)
    # print(f"Запросы содержащие {perc} слов составляют {round(p, 2)} % от всех имеющихся ")
    


                        #TASK2
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
# plenty = set()

# for num_ in ids.values():
#     for num_2 in range(len(num_)):
#         plenty.add(num_[num_2])
# print(list(plenty))


                        #TASK1
# geo_logs = [
#     {"visit1": ["Москва", "Россия"]},
#     {"visit2": ["Дели", "Индия"]},
#     {"visit3": ["Владимир", "Россия"]},
#     {"visit4": ["Лиссабон", "Португалия"]},
#     {"visit5": ["Париж", "Франция"]},
#     {"visit6": ["Лиссабон", "Португалия"]},
#     {"visit7": ["Тула", "Россия"]},
#     {"visit8": ["Тула", "Россия"]},
#     {"visit9": ["Курск", "Россия"]},
#     {"visit10": ["Архангельск", "Россия"]}]


# for Russia_all in range(len(geo_logs)):
#     for visit, city in geo_logs[Russia_all].items():
#         if geo_logs[Russia_all][str(*geo_logs[Russia_all].keys())][1] == "Россия":
#             print(visit, "->", *city)
