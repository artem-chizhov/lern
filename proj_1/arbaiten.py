region_list = ["ДФО", "ЦФО", "ЮФО"]
rate_list = []
region_yes = float(2)
children_yes = float(1)
salary_yes = float(0.5)
insurance_yes = float(1.5)
base_rate = float(13)


    #Блок карточка клиента
#Имя клиента
while True:
    first_name = input("Введите имя клиента: ")
    if first_name != "":
        break
    else:
        print("Не может быть пустым!")
#Фамилия клиента
while True:
    last_name = input("Введите фамилию клиента: ")
    if last_name != "":
        break
    else:
        print("Не может быть пустым!")
#Ввод паспорта
while True:
    while True:
        try:
            passport = int(input("Введите серию и номер паспорта(только цифры(10), без пробела): "))      
        except ValueError:
            print("Не верный формат.")
        else:
            break
    if len(str(passport)) == 10:
        break
    else:
        print("Должно быть 10 цифр!")
# Ввод региона
while True:
    region = input("Введите Ваш регион (например ЦФО\ДФО\ЮФО): ").upper()
    if region in region_list:
        break
    else:
        print("Ошибка: Не может быть пустым или не верный формат")
#Ввод количества детей
while True:
    while True:
        try:
            children = int(input("Введите количество детей(при отсутствии указать 0): "))
        except ValueError:
            print("Только целые числа (1,2,3,4)")
        else:
            break
    if children >= 30:
        print("Слишком большое число!")
    elif children >= 3:
        rate_list.append(children_yes)
        break
    else:
        break
#Чекбокс ЗП клиента
while True:
    salary_project = input("Являетесь зарплатным клиентом (да\нет)? ").lower()
    if salary_project == "да":
        rate_list.append(salary_yes)
        break
    elif salary_project == "нет":
        break
    else:
        print("Ошибка ввода! Следует вводить - да или нет")
#Чек бокс страховки
while True:
    insurance = input("Планируется ли страхование кредитного продукта?  ")
    if insurance == "да":
        rate_list.append(insurance_yes)
        break
    elif insurance == "нет":
        break
    else:
        print("Ошибка ввода! Следует вводить - да или нет")
    #Блок ввода расчетных данных
#Сумма первоначального взноса
while True:
    try:
        initial_pay = float(input("Введите сумму первоначального взноса: "))
    except ValueError:
        print("Не верный формат ввода!\nРазделитель дробной части точка." )
    else:
        break
#Срок ипотеки
while True:
    while True:
        try:
            expiration = int(input("Введите срок ипотеки (Мес.): "))
        except ValueError:
            print("Не верный формат ввода! Только цифры!")
        else:
            break
    if expiration <= 360 and expiration >= 6 and expiration != 0:
        break
    else:
        print("Максимальный срок 360 месяцев (30 лет)\nМинимальный срок 6 месяцев!")
#Сумма ипотеки
while True:
    try:
        mortgage_amount = float("Введите сумму ипотеки(минимальная сумма 100000, максимальная 10000000): ")
    except ValueError:
        print("Не верный формат ввода! Только цифры!\nРазделитель дробной части точка.")
    if mortgage_amount != 0 and mortgage_amount >= 100000 and mortgage_amount <= 10000000:
        break
    else:
        print("минимальная сумма 100000, максимальная 10000000!")

    #Блок калькуляции
#Вычисляем % клиента
if region == region_list[0]:
    client_rate = region_yes
elif len(rate_list):
    client_rate = base_rate - (sum(rate_list))
else:
    client_rate = base_rate
#Подводим подсчет ипотеки
overpayment = ((mortgage_amount - initial_pay)/100*client_rate)/12*expiration
full_amount = overpayment + mortgage_amount - initial_pay
monthly_pay = full_amount / expiration
#Выводим данные пользователю
print(f'Ваша ставка по ипотеке: {client_rate}')
print(f'Сумма переплаты за весь срок составит: {overpayment}')
print(f'Полная сумма ипотеки составит: {full_amount}')
print(f'Ежемесячный платёж составит: {monthly_pay}')
