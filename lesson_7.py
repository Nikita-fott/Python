#1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, li):
        self.my_matrix = li

    def __add__(self, other):
        if len(self.my_matrix) != len(other.my_matrix):
            return 'Размер матриц не совпадает'
        summa = [map(sum, zip(*i)) for i in zip(self.my_matrix, other.my_matrix)]
        return Matrix(summa)

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_matrix])

a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print('##########')
print(b)
print('##########')
print(a+b)

#2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothing(ABC):
    total_fabric_cost = []
    def __init__(self, name):
        self.name = name
        Clothing.total_fabric_cost.append(self)

    @abstractmethod
    def fabric_costs(self):
        pass

    def clothing_size(self):
        try:
            if self.V <= 140:
                return f'Для {self.name} размера S потребуется {self.fabric_costs()} материала'
            elif 140 <= self.V < 160:
                return f'Для {self.name} размера M потребуется {self.fabric_costs()} материала'
            else:
                return f'Для {self.name} размера L потребуется {self.fabric_costs()} материала'
        except TypeError:
            print('Укажите размер в цифрах')

    @property
    @abstractmethod
    def new_size (self):
        pass

class Coat(Clothing):
    total_fabric = []
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    def fabric_costs(self):
        self.fabric_costs_item = round(self.V/6.5 + 0.5, 2)
        return self.fabric_costs_item

    @property
    def new_size(self):
        return self.V

    @new_size.setter
    def new_size(self, size):
        self.V = size

class Suit(Clothing):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    def fabric_costs(self):
        self.fabric_costs_item = round(self.V * 2 + 0.3, 2)
        return self.fabric_costs_item

    @property
    def new_size(self):
        return self.V

    @new_size.setter
    def new_size(self, size):
        self.V = size

a = Coat('Coat', 150)
print(a.clothing_size())

b = Suit('Suit', 138)
print(b.clothing_size())

add = sum([i.fabric_costs_item for i in Clothing.total_fabric_cost])
print(f'Для изготовления двух изделий потребуется {add} материала')

a.new_size = 130
print(a.clothing_size())
b.new_size = 180
print(b.clothing_size())

add = sum([i.fabric_costs_item for i in Clothing.total_fabric_cost])
print(f'Для изготовления двух изделий потребуется {add} материала')

#3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка

class Cell:
    def __init__(self, amount_cell: int):
        self.amount_cell = amount_cell
        self.symbol = '*'

    def __add__(self, other):
        return Cell(self.amount_cell + other.amount_cell)

    def __sub__(self, other):
        if self.amount_cell < other.amount_cell:
            return 'Отрицательне значение'
        else:
            return Cell(self.amount_cell - other.amount_cell)

    def __mul__(self, other):
        if self.amount_cell * other.amount_cell == 0:
            return 'Введите значение больше нуля'
        else:
            return Cell(self.amount_cell * other.amount_cell)

    def __truediv__(self, other):
        try:
            return Cell(self.amount_cell // other.amount_cell)
        except ZeroDivisionError:
            return 'На ноль делить нельзя, ввести значени больше нуля'

    def __str__(self):
        return f'Количетво ячеек: {self.amount_cell}'

    def make_order(self, row_cell):
        integer = '\n'.join([row_cell * self.symbol for i in range(self.amount_cell // row_cell)])
        if self.amount_cell % row_cell == 0:
            return integer
        else:
            return '\n'.join([integer, (self.amount_cell % row_cell) * self.symbol])

a = Cell(7)
b = Cell(3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print((a*b).make_order(8))