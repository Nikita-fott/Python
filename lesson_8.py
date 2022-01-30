#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime

class Date:
    now = datetime.now()
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_int(cls, day_month_year):
        day, month, year = map(int, day_month_year.split('-'))
        new_date = cls(day, month, year)
        return new_date

    @staticmethod
    def validation(day_month_year):
        if day_month_year.count('-') == 2:
            day, month, year = map(int, day_month_year.split('-'))
            return 1 <= day <= 31 and 1 <= month <= 12 and year <=9999

    def get_new_date(self):
        date_1 = datetime(self.year, self.month, self.day)
        if Date.now > date_1:
            delta_date = Date.now - date_1
            return "{} день назад вышел альбом Оксимирона".format(delta_date.days)
        else:
            delta_date = date_1 - Date.now
            return "Через {} день выйдет новый альбом Оксимирона".format(delta_date.days)

dates = [
    '30.12.2020',
    '30-12-2020',
    '01/01/2021',
    '100-25-2020',
    '25-11-2027',
    ]

for i in dates:
    if Date.validation(i):
        date = Date.get_int(i)
        get_new_date = date.get_new_date()
        print(get_new_date)
    else:
        print(f'Неправильная дата или формат строки с датой')


#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_error(Exception):
    def __init__(self, txt):
        self.txt = txt

numbers = input('Введите два числа через пробел: ')

try:
    number_1, number_2 = map(int, numbers.split())
    if number_1 or number_2 == 0:
        raise My_error('На ноль делить нельзя')
    if number_1 >= number_2:
        result = abs(round(number_1 / number_2, 2))
    else:
        result = abs(round(number_2 / number_1, 2))
except ValueError:
    print('Вы ввели не числовые значения')
except My_error as my_err:
    print(my_err)
else:
    print(f'Результат: {result}')

#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class My_error(Exception):
    def __init__(self, text):
        self.text = text

numbers = []
while True:
    number = input('Введите данные, нажмите Enter, конец = stop: ')
    if number == 'stop':
        break
    else:
        try:
            if number.isdigit() == True:
                numbers.append(int(number))
            else:
                raise My_error(f'{number} - не числового формата')
        except My_error as end:
            print(end)

str_numbers = ' '.join(str(i) for i in numbers)
print(f'В список попали следующие введенные числовые значения {str_numbers}')

#4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod

class Storage:
    def __init__(self):
        self._dict_office = {}

    def add_unit(self, oe):   #oe = officeEquipment
        self._dict_office.setdefault(oe.get_group_name_office_equipment(), []).append(oe)

    def give_away(self, name):
        if self._dict_office[name]:
            self._dict_office.setdefault(name).pop(0)

class OfficeEquipment(ABC):
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.group_name_office_equipment = self.__class__.__name__
        self.condition_list = ['замена не требуется', 'износ 50%', 'требуется замена']

    def get_group_name_office_equipment(self):
        return f'{self.group_name_office_equipment}'

    def get_group_name_office_equipment(self):
        return f'{self.group_name_office_equipment}'

    def __repr__(self):
        return f'{self.name} {self.model} {self.year}'

    @staticmethod
    def validation(unit):
        if not isinstance(unit.name, str):
            print(f'{unit.name} должно быть "str"')

    @abstractmethod
    def work(self, paper_quantity):
        pass

    @abstractmethod
    def get_condition(self):
        pass

    @property
    @abstractmethod
    def get_repair(self):
        pass

class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(*args)
        self.total_quantity_paper = 0

    def work(self, paper_quantity):
        self.paper_quantity = paper_quantity
        self.total_quantity_paper = self.paper_quantity + self.paper_quantity/10
        self.condition = round(self.total_quantity_paper / 10000, 2)
        if self.condition > 0:
            print(f'Печать {self.paper_quantity} страниц, износ устройства: {self.condition * 100}%')
        else:
            print('Сканирование невозможно')

    def get_condition(self):
        if self.total_quantity_paper < 1000:
            print(f'Состояние {self.name}: {self.condition_list[0]}')
        elif 1000 <= self.total_quantity_paper < 10000:
            print(f'Состояние {self.name}: {self.condition_list[1]}')
        else:
            print(f'Состояние {self.name}: {self.condition_list[2]}')

    @property
    def get_repair(self):
        return self.total_quantity_paper

    @get_repair.setter
    def get_repair(self, new_total_quantity_paper):
        self.total_quantity_paper = new_total_quantity_paper

class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(*args)
        self.total_quantity_paper = 0

    def work(self, paper_quantity):
        self.paper_quantity = paper_quantity
        self.total_quantity_paper = self.paper_quantity + self.paper_quantity / 10
        self.condition = round(self.total_quantity_paper / 3500, 2)
        if self.condition > 0:
            print(f'Сканирование {self.paper_quantity} страниц, износ устройства: {self.condition * 100}%')
        else:
            print('Сканирование невозможно')

    def get_condition(self):
        if self.total_quantity_paper < 500:
            print(f'Состояние {self.name}: {self.condition_list[0]}')
        elif 500 <= self.total_quantity_paper < 3500:
            print(f'Состояние {self.name}: {self.condition_list[1]}')
        else:
            print(f'Состояние {self.name}: {self.condition_list[2]}')

    @property
    def get_repair(self):
        return self.total_quantity_paper

    @get_repair.setter
    def get_repair(self, new_total_quantity_paper):
        self.total_quantity_paper = new_total_quantity_paper

class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(*args)
        self.total_quantity_paper = 0

    def work(self, paper_quantity):
        self.paper_quantity = paper_quantity
        self.total_quantity_paper = self.paper_quantity + self.paper_quantity/10
        self.condition = round(self.total_quantity_paper / 5000, 2)
        if self.condition > 0:
            print(f'Копирование {self.paper_quantity} страниц, износ устройства: {self.condition * 100}%')
        else:
            print('Сканирование невозможно')

    def get_condition(self):
        if self.total_quantity_paper < 300:
            print(f'Состояние {self.name}: {self.condition_list[0]}')
        elif 300 <= self.total_quantity_paper < 3000:
            print(f'Состояние {self.name}: {self.condition_list[1]}')
        else:
            print(f'Состояние {self.name}: {self.condition_list[2]}')

    @property
    def get_repair(self):
        return self.total_quantity_paper

    @get_repair.setter
    def get_repair(self, new_total_quantity_paper):
        self.total_quantity_paper = new_total_quantity_paper


storage = Storage()
printer_1 = Printer('LexMark', 'SD 5000', 2020)
printer_1.validation(printer_1)
storage.add_unit(printer_1)
printer_1.work(5000)
printer_1.get_condition()
scanner_1 = Scanner('Samsung', 'KL-5000', 2021)
storage.add_unit(scanner_1)
scanner_1.work(35)
scanner_1.get_condition()

xerox_1 = Xerox('LG', 'BU-5000', 2019)
storage.add_unit(xerox_1)
xerox_1.work(50)
xerox_1.get_condition()

print(storage._dict_office)
storage.give_away('Printer')
print(storage._dict_office)

#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
#10 + 5 i

class CopmlexNumbers:
    __i = 'i'
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    @classmethod
    def get_int(cls, number):
        a, b = map(float, number.rstrip('i').split())
        numbers = cls(a, b)
        return numbers

    def __str__(self):
        return f'Сложение/умножение: {self.a} + ({self.b}{CopmlexNumbers.__i})'

    def __add__(self, other):
        return CopmlexNumbers(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return CopmlexNumbers((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))

a = CopmlexNumbers.get_int('10 5i')
b = CopmlexNumbers.get_int('15 -8i')
print(a + b)
print(a * b)