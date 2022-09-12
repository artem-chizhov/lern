# zodiac_list = {"январь":(20,"козерог","водолей"), "февраль":(19,"водолей","рыбы"),
#             "март":(20,"рыбы","овен"), "апрель":(20,"овен","телец"),
#             "май":(21,"телец","близнецы"), "июнь":(21,"близнецы","рак"),
#             "июль":(22,"рак","лев"), "август":(21,"лев","дева"),
#             "сентябрь":(23,"дева","весы"), "октябрь":(23,"весы","скорпион"),
#             "ноябрь":(22,"скорпион","стрелец"), "декабрь":(22,"стрелец","козерог")


            




from audioop import reverse
from ntpath import join


# records = [["bar", 20.0],["aleg",50.0],["celtra",50.0]]
# a = []
# b = []
# # for _ in range(int(input())):
# # name = input()
# # score = float(input())
# # records.append([name, score])
# for x in range(len(records)):
#     a.append(records[x][1])

# for i in range(len(a)):
#     if max(a) == records[i][1]:
#         b.append(records[i][0])

# b = sorted(b)
# print("\n".join([str(i)for i in b]))

a = [29,1,2,2,4]
a = sorted(a)
z = []
for i in range(len(a)):
    if a[i] > a[0]:
        z.append(a[i])




print(a)
print(z)
# print(fruits.index('guava'))

# z = a.index(min(a))
