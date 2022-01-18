#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных будет свидетельствовать пустая строка.

a = int(input('Сколько строк будет добавлено в файл: '))
i = 1
strokes = []
while i < a + 1:
    stroke = input(f'Введите {i} строку: ')
    strokes.append(stroke)
    i += 1

with open('task-1.txt', 'w', encoding='UTF-8') as f:
    f.write('\n'.join(strokes))


#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

f = open('task-2.txt', 'r', encoding='utf-8')
fr = f.readlines()
print(f'В файле {f.name} находится {len(fr)} строка')
for i in range(0, len(fr)):
    print(f'В строке {i+1} находится {len(fr[i].split())} слов')

#3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
#Пример файла:
# Иванов 23543.12
# Петров 13749.32

def salary():
    with open('task-3.txt', 'r', encoding='utf-8') as f:
        workers = []
        salaries = []
    for line in f:
        worker, salary = line.split(' ')
        salary = salary.replace('\n', '')
        salary = float(salary)
        salaries.append(salary)
        if salary < 20000:
            workers.append(worker)
    print(f'Следующие сотрудники имеют зп < 20000 {workers}')
    print(salaries)

from functools import reduce

def summa(a, b):
    return a + b

av_salary = reduce(summa, salaries)/len(salaries)
print(av_salary)

#4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_numerals = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open('task-4.txt', 'r', encoding='utf-8') as f:
    numeral = []
    numbers = []
    for el in f:
        print(el, end='') #вывод исходного файла
        a = el.split(' ')[0]
        numeral.append(a) #сохранил латиницу
        number = el.split('—')[1] #сохранил цифру соответствующую латинице
        numbers.append(number)

numeral_new = [v for k, v in dict_numerals.items() if k in numeral] #соответствие перевода из словаря, идея в том: например значению four соответствует только перевод четыре
content = []
for i in range(0, len(numeral_new)):
    content.append(numeral_new[i]+' —'+numbers[i])


with open('task-4-new.txt', 'w+', encoding='utf-8') as f_new:
    f_new.writelines(content)
    # f_new.seek(0)
    # f_new_read = f_new.read()
    # print(f_new_read)


#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from functools import reduce

try:
    with open('task-5.txt', 'w+', encoding='utf-8') as f:
        numbers = input('Введите числа через пробел: ')
        f.write(numbers)
        f.seek(0)
        numbers_read = f.read()
        numbers_list = list(map(int, numbers_read.split(' ')))
        print(numbers_list)

        def summa(a, b):
            return a + b
        print(reduce(summa, numbers_list))
except ValueError:
    print('Введите только числовые значения')

#6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
#Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dict_subject = {}

with open('task-6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in lines:
        subject = i.split(':')[0]
        value_subject = i.replace('(', ' ').split()
        dict_subject[subject] = sum(int(i) for i in value_subject if i.isdigit())
print(dict_subject)

#7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

dict_firms = {}
average_profits = {}

with open('task-7.txt', 'w+', encoding='utf-8') as f:
    profits = []
    firms = []
    n = int(input('Введите количество фирм: '))
    while n > len(firms):
        firm = input('Введите через пробел название фирмы, форму собственности, выручку, издержки: ')
        firms.append(firm)
    #print(firms)
    f.write('\n'.join(firms))
    f.seek(0)
    f_firms = f.readlines()
    #print(a)
    for i in f_firms:
        revenue = float(i.split(' ')[2])
        costs = float(i.split(' ')[3])
        name = i.split(' ')[0]
        profit = revenue - costs
        if profit > 0:
            profits.append(profit)
        dict_firms[name] = profit

# print(profits)
# print(dict_firms)
from functools import reduce

def summa(a, b):
    return a + b
av = reduce(summa, profits)/len(profits)
#print(av)
average_profits = {'average_profit':av}
report_form = [dict_firms, average_profits]
# print(dict_firms)
# print(average_profits)
print(report_form)

import json
with open("task-7-json.json", "w", encoding='utf-8') as report_form_json:
    json.dump(report_form, report_form_json)
