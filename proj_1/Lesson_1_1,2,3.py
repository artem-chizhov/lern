
# Calculating the perimeter and area of a square
square_length = input("Введите длину стороны квадрата: ")
square_perimeter = float(square_length) * 4
square_area = float(square_length) ** 2
print(f"Периметр квадрата равен: {square_perimeter}")
print(f"Площадь квадрата равна: {square_area}")

# Calculating the perimeter and area of a rectangle
rectangle_length = input("Введите длину прямоугольника: ")
rectangle_width = input("Ввелите ширину прямоугольника: ")
rectangle_perimeter = (float(rectangle_length) + float(rectangle_width)) * 2
rectangle_area = float(rectangle_width) * float(rectangle_length)
print(f"Периметр прямоугольника равен: {rectangle_perimeter}")
print(f"Площадь прямоугольника равна: {rectangle_area}") 

#separator
length_string = int(square_perimeter + rectangle_area)
sep = str(input("Введите разделитель задач (любой символ): "))[:length_string] 
print((sep * length_string)[:length_string])

#Financial planning
salary = float(input("Введите заработную плату в месяц: "))
percent_mortgage_sal = float(input("Введите, какой процент(%) уходит на ипотеку: "))
percent_live_sal = float(input("Введите, какой процент(%) уходит на жизнь: "))
calc_period = int(input("Введите за какое время произвести расчет(мес): "))
spent_mortgage = float(salary * percent_mortgage_sal / 100 * calc_period)
spent_live = float(salary * percent_live_sal / 100 * calc_period)
print(f"На ипотеку было потрачено: {spent_mortgage}")
print("Было накоплено: ", float(salary * calc_period - (spent_mortgage + spent_live)))
