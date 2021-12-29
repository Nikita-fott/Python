#ДЗ 2
#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
list = [1, 1.5, 'float', True, [5, 6], {'home':'дом'}, (5, 'sds'), None]
print(type(list))

for i in list:
    print(type(i))

#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

a =int(input('Введите количетсво элементов в списке: '))
count_list = 0
list = []
while count_list < a:
    element = input('Введите элемент списка: ')
    list.append(element)
    count_list+=1

old = list
print(old)
for i in range(0, len(list)-1, 2):
    list[i], list[i+1] = list[i+1], list[i]
print(list)

#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите номер месяца: '))

# list = ['зима',[12, 1, 2], 'весна', [3, 4, 5], 'лето', [6, 7, 8], 'осень', [9, 10, 11]]
# for i in list:
#     if month in list[1]:
#         print(list[0])
#     elif month in list[3]:
#         print(list[2])
#     elif month in list[5]:
#         print(list[4])
#     else:
#         print(list[6])
#     break
#
# month = int(input('Введите номер месяца: '))
# dict = {'зима' : [12, 1, 2], 'весна':[3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
#
# for i in dict:
#     if month in dict[i]:
#         print(i)
#         break
#
# month = int(input('Введите номер месяца: '))

list_month = ['зима', 'весна', 'лето', 'осень']
dict_month = {0:'зима' ,1 : 'весна', 2:'лето',3 : 'осень', 4:'зима'}
if 1 <= month <= 2 or month == 12:
    print(list_month[0])
    print(dict_month[month // 3])
elif 3 <= month <= 5:
    print(list_month[1])
    print(dict_month[month // 3])
elif 6 <= month <= 8:
    print(list_month[2])
    print(dict_month[month // 3])
elif 9 <= month <= 11:
    print(list_month[3])
    print(dict_month[month // 3])
else:
    print('Необходимо ввести число от 1 до 12')

#  Пользователь вводит строку из нескольких слов, разделённых пробелами.
#  Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

str = input('Введите строку: ')
str_split = str.split(' ')
for i, element in enumerate(str_split):
    if len(element) > 10:
       print(i+1, element[0:10])
    else:
        print(i+1, element)

#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 2]
a = None
while a != 'конец':
    number = int(input('введите число: '))
    for i in range(0, len(my_list)):
        if number == my_list[i]:
            my_list.insert(i + 1, number)
            print(my_list)
            break
        elif number > my_list[0]:
            my_list.insert(0, number)
            print(my_list)
        elif number < my_list[-1]:
            my_list.append(number)
            print(my_list)
        elif number < my_list[i] and number > my_list[i+1]:
            my_list.insert(i+1, number)
            print(my_list)
            break
    a = input('Если хотите продолжить нажмите "Enter" или введите "конец" если устали: ')


#Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

keys = ['название', 'цена', 'количество', 'ед']
goods = []     #характеристики каждого товара
all = []       #изначальный список все наших товаров"""
all2 = []    #собирает списки keys и all в словари"""
all3 = []    #результат список кортежей"""
names = []   #список наименований товаров"""
prices =[]   #список цен"""
amounts = []    #список количества каждого товара"""

while True:
    name = input('Введите наименование товара, если ввели все позиции, то - stop: ')
    if name == 'stop':
        break
    else:
        price = int(input('Введите цену: '))
        amount = int(input('Введите количество: '))
        ed = 'шт'
        goods = [name, price, amount, ed]
        all.append(goods)
        names.append(name)
        prices.append(price)
        amounts.append(amount)
        analytics = dict(название=names, цена=prices, количество=amounts, ед='шт')  #собрана аналитика товаров в словарь"""

for i in all:
    d = dict(zip(keys, i))  #создал словари для каждого товара из списка all"""
    all2.append(d)

for el in enumerate(all2, 1):
    all3.append(el)
print(all3)
print(analytics)