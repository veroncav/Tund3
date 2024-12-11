# nimi=input(" Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#     if nimi=="JUKU":
#         print("Lähme kinno")
#         try:
#             vanus=int(input(f" Kui vana sa oled {nimi}? "))
#             if vanus<0:
#                 print("Viga!")
#             elif vanus<=6:
#                 print("Tasuta")
#             elif vanus<15:
#                 print("Lastepilet")
#             elif vanus <65:
#                 print("Taispilet")
#             elif vanus <100:
#                 print("Sooduspilet")
#             else:
#                 print("Nii palju!!")
#         except:
#             print(" Täisarv oli vaja sisestada ")
#     else:
#         print(" Ootan Juku ")
#     print(" Suured tähed ")
# else:
#     print(" Segatud sõne ")


#Ülesanne 2
#variant1
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. Mis on sinu nimi? ")
# nimed=["Kirill","Zhan"]
# if nimi.isalpha() and nimi2.isalpha():
#    if (nimil in nimed) and (nime2 in nimed):
#        print("Nad on pinginaabrid")
#     else:
#         print ("Nad ei ole naabrid")
# else:
#     print("Viga")

# #variant2
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. Mis on sinu nimi? ")

# nimed=["Kirill" , "Zhan"]
# if (nimi1== "Kirill" and nimi2== "Zhan") or (nimi2=="Kirill" and nimi1=="Zhan"):
#     print("Nad on pinginaabrid")
# else:
#     print ("Nad ei ole naabrid")

    #Ulesanne 3
# try:
#     a=float(input("Toa pikkus"))
#     b=float(input("Toa laius"))
#     S=a*b
#     print(f"Poranda pindala on {S}m**2")
#     vastus=input(" Kas tahad remondi teha? (Jah-1/Ei-0)") #Jan/Ei
#     if vastus.upper()=="JAH" or vastus=="1":
#        print("Remont")
#        hind=float(input("Ühe meetri hind: "))

#     elif vastus.upper()=="EI" or vastus=="0":
#         print("-")
#     else:
#         print("Ei saa aru")
# except:
#         print("Numbrid!!!")


#Ulesanne 4

price = input("Введите начальную цену товара: ")

if price.isdigit() or (price.replace('.', '', 1).isdigit() and price.count('.') <= 1):
    price = float(price)  # Преобразуем ввод в число
    if price > 700:
        discounted_price = price * 0.7  # Скидка 30%
        print(f"Цена со скидкой: {discounted_price:.2f} евро.")
    else:
        print("Скидка не применяется, товар дешевле 700 евро.")
else:
    print("Ошибка: введите корректное число.")


    #Ulesanne 5

    temperature = input("Введите температуру в комнате (°C): ")

if temperature.replace('.', '', 1).isdigit():
    temperature = float(temperature)
    if temperature > 18:
        print("Температура комфортная для зимы.")
    else:
        print("Температура слишком низкая.")
else:
    print("Некорректное значение температуры.")

 
    #Ulesanne 6

pikkus_input = input("Palun sisesta oma pikkus (cm): ")

if pikkus_input.isdigit():
    pikkus = int(pikkus_input)
    if pikkus > 0 and pikkus <= 220:
        if pikkus < 160:
            print("Sa oled lühike.")
        elif 160 <= pikkus <= 170:
            print("Sa oled keskmist kasvu.")
        else:
            print("Sa oled pikk.")
    else:
        print("Palun sisesta õige pikkus .")
else:
    print("Palun sisesta korrektne number!")

    #Ulesanne 7
    height = input("Введите ваш рост (в см): ")
gender = input("Введите ваш пол (м/ж): ").lower()

if height.isdigit():
    height = int(height)
    if gender == "м":
        if height < 160:
            print("Вы низкого роста.")
        elif height <= 185:
            print("Вы среднего роста.")
        else:
            print("Вы высокого роста.")
    elif gender == "ж":
        if height < 150:
            print("Вы низкого роста.")
        elif height <= 170:
            print("Вы среднего роста.")
        else:
            print("Вы высокого роста.")
    else:
        print("Некорректный пол.")
else:
    print("Некорректный рост.")

    #Ulesanne 8

    import random

products = ["молоко", "хлеб", "сахар", "масло"]
prices = {product: random.uniform(1, 5) for product in products} 
total = 0

for product in products:
    quantity = input(f"Сколько {product} вы хотите купить? (0, если не нужно): ")
    if quantity.isdigit():
        quantity = int(quantity)
        cost = quantity * prices[product]
        total += cost
        print(f"{product.capitalize()}: {quantity} шт. по {prices[product]:.2f} € за шт. = {cost:.2f} €")
    else:
        print(f"Некорректное количество для {product}.")

print(f"Общая сумма: {total:.2f} €.")

#Ulesanne 9

side1 = input("Введите длину первой стороны: ")
side2 = input("Введите длину второй стороны: ")

if side1.replace('.', '', 1).isdigit() and side2.replace('.', '', 1).isdigit():
    side1 = float(side1)
    side2 = float(side2)
    if side1 == side2:
        print("Эта фигура может быть квадратом.")
    else:
        print("Эта фигура не квадрат.")
else:
    print("Некорректные данные.")

    #Ulesanne 10

    num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
operation = input("Введите операцию (+, -, *, /): ")

if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: деление на ноль."
    else:
        result = "Некорректная операция."
    
    print(f"Результат: {result}")
else:
    print("Некорректные числа.")


    #Ulesanne 11

    birth_year = input("Введите год рождения: ")

if birth_year.isdigit():
    birth_year = int(birth_year)
    current_year = 2024
    age = current_year - birth_year
    
    if age % 10 == 0:
        print(f"Ваш возраст {age} лет. Это юбилей!")
    else:
        print(f"Ваш возраст {age} лет. Это не юбилей.")
else:
    print("Некорректный год рождения.")

    #Ulesanne 12

    price = input("Введите цену товара: ")

if price.replace('.', '', 1).isdigit():
    price = float(price)
    if price <= 10:
        final_price = price * 0.9  # Скидка 10%
    else:
        final_price = price * 0.8  # Скидка 20%
    print(f"Цена со скидкой: {final_price:.2f} €.")
else:
    print("Некорректная цена.")

    #Ulesanne 13

    gender = input("Ваш пол (м/ж): ").lower()

if gender == "м":
    age = input("Введите ваш возраст: ")
    if age.isdigit():
        age = int(age)
        if 16 <= age <= 18:
            print("Вы подходите для футбольной команды.")
        else:
            print("Вы не подходите для футбольной команды.")
    else:
        print("Некорректный возраст.")
elif gender == "ж":
    print("Для женщин отбор не проводится.")
else:
    print("Некорректный пол.")






#Kodutöö
    #Ulesanne 1

    number = input("Введите число: ")

if number.replace('-', '', 1).isdigit():
    number = int(number)
    if number > 0:
        print("Число положительное.")
        if number % 2 == 0:
            print("Число четное.")
        else:
            print("Число нечетное.")
    elif number < 0:
        print("Число отрицательное.")
    else:
        print("Число равно нулю.")
else:
    print("Ошибка: введите корректное число.")

    #Ulesanne 2

    angles = input("Введите три угла треугольника через пробел: ").split()

if len(angles) == 3 and all(angle.isdigit() and 0 < int(angle) < 180 for angle in angles):
    angles = [int(angle) for angle in angles]
    if sum(angles) == 180:
        print("Это треугольник.")
        if angles[0] == angles[1] == angles[2]:
            print("Треугольник равносторонний.")
        elif angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]:
            print("Треугольник равнобедренный.")
        else:
            print("Треугольник разносторонний.")
    else:
        print("Сумма углов не равна 180. Это не треугольник.")
else:
    print("Ошибка: введите три корректных угла от 1 до 179.")

    #Ulesanne 3

    answer = input("Хотите расшифровать номер дня недели? (да/нет): ").lower()

if answer == "да":
    day = input("Введите номер дня недели (1-7): ")
    if day.isdigit() and 1 <= int(day) <= 7:
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        print(f"Это {days[int(day) - 1]}.")
    else:
        print("Ошибка: введите число от 1 до 7.")
else:
    print("Хорошо, до свидания!")

    #Ulesanne 4
    day = input("Введите день рождения (1-31): ")
month = input("Введите номер месяца рождения (1-12): ")

if day.isdigit() and month.isdigit():
    day, month = int(day), int(month)
    if 1 <= month <= 12 and 1 <= day <= 31:
        if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19):
            sign = "Овен"
        elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20):
            sign = "Телец"
        elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 20):
            sign = "Близнецы"
        elif (month == 6 and 21 <= day <= 30) or (month == 7 and 1 <= day <= 22):
            sign = "Рак"
        elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
            sign = "Лев"
        elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
            sign = "Дева"
        elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 22):
            sign = "Весы"
        elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 21):
            sign = "Скорпион"
        elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
            sign = "Стрелец"
        elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 19):
            sign = "Козерог"
        elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
            sign = "Водолей"
        elif (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
            sign = "Рыбы"
        else:
            sign = "Некорректная дата."
        print(f"Ваш знак зодиака: {sign}.")
    else:
        print("Ошибка: неверная дата.")
else:
    print("Ошибка: введите числовые значения.")

    #Ulesanne 5

    value = input("Введите значение: ")

if value.isdigit() or (value.replace('.', '', 1).isdigit() and value.count('.') <= 1):
    value = float(value)
    if value.is_integer():
        print(f"50% от числа: {value * 0.5}")
    else:
        print(f"70% от числа: {value * 0.7}")
elif value.isalpha():
    print(f"Вы ввели текст: {value}")
else:
    print("Ошибка: некорректный ввод.")

    #Ulesanne 6

    answer = input("Хотите решить квадратное уравнение? (да/нет): ").lower()

if answer == "да":
    print("Введите коэффициенты уравнения ax^2 + bx + c = 0.")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")

    if all(x.replace('.', '', 1).isdigit() for x in [a, b, c]):
        a, b, c = float(a), float(b), float(c)
        if a != 0:
            D = b**2 - 4 * a * c
            print(f"Дискриминант D = {D:.2f}")
            if D > 0:
                x1 = (-b + D**0.5) / (2 * a)
                x2 = (-b - D**0.5) / (2 * a)
                print(f"Два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif D == 0:
                x = -b / (2 * a)
                print(f"Один корень: x = {x:.2f}")
            else:
                print("Корней нет.")
        else:
            print("Ошибка: коэффициент a не может быть равен 0.")
    else:
        print("Ошибка: введите числа.")
else:
    print("Хорошо, до свидания!")
