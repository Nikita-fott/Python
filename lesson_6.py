#1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    color_dict = {'красный': 7, 'желтый': 2, 'зеленный': 7}
    __color = ''

    def runnin(self):
        for __color, sw_time in self.color_dict.items():
            print(f'Цвет светофора {__color}, осталось {sw_time} секунд')
            time.sleep(sw_time)
            if __color == 'зеленный':
                print(f'Горит снова {__color}')

a = TrafficLight()
a.runnin()

#2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, lenght: [int, float], width: [int, float]):
        self._l = lenght
        self._w = width

    def weight(self):
        try:
            m = (self._l * self._w * 25 * 5) / 1000
            return m
        except TypeError:
            print('Введите числовые значения')

    def square(self):
        try:
            s = self._l * self._w
            return s
        except TypeError:
            print('Введите числовые значения')

asphalt = Road(20, 5000)
print(f'Количество асфальтобетона {asphalt.weight()} т. на территорию площадью {asphalt.square()} м2, при высоте слоя 5 см, и вес смеси 25 кг')

#3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: [int, float], bonus: [int, float]):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return ' '.join([self.s, self.n])

    def get_total_income(self):
        return sum(self._income.values())

a = Position('Ivan', 'Ivanov', 'engineer', 10000, 5555)

print(f'Сотрудник: {a.get_full_name()}, занимает должность {a.p} с доходом: {a.get_total_income()}')


#4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed: [int, float], color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True if is_police else False

    def police(self):
        if self.is_police == True:
            return print(f'{self.name} - полицейская машина')
        else:
            pass

    def go(self):
        try:
            if self.speed > 0:
                return print(f'{self.name} поехал')
        except ValueError:
            pass

    def stop(self):
        if self.speed == 0:
            return print(f'{self.name} остановился')
        else:
            pass

    def turn(self, direction):
        self._direction = direction
        if self._direction == 'right':
            return print(f'{self.name} повернул направо')
        elif self._direction == 'left':
            return print(f'{self.name} повернул налево')
        else:
            return print(f'{self.name} едет прямо')

    def show_speed(self):
        return print(f'{self.name} движется со скоростью {self.speed}')

class TownCar(Car):
    def __init__(self, *args):
        super().__init__(*args)
    def show_speed(self):
        if self.speed > 60:
            return print(f'{self.name} превысил скорость')

class WorkCar(Car):
    def __init__(self, *args):
        super().__init__(*args)
    def show_speed(self):
        if self.speed > 40:
            return print(f'{self.name} превысил скорость')
        else:
            return print(f'Текущая скорость {self.name} равна {self.speed}')

class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police = True)


car2 = TownCar(70, 'yellow', 'Porshe', False)
car2.go()
car2.stop()
car2.turn('')
car2.show_speed()
car2.police()
print('#######################################')
car3 = WorkCar(39, 'green', 'Nissan', False)
car3.go()
car3.stop()
car3.turn('right')
car3.show_speed()
car3.police()
print('#######################################')
car1 = SportCar(100, 'black', 'Ferrari', False)
car1.go()
car1.stop()
car1.turn('left')
car1.show_speed()
car1.police()
print('#######################################')
car4 = PoliceCar(15, 'white', 'Ford')
car4.go()
car4.stop()
car4.turn('')
car4.show_speed()
car4.police()

#5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        print(f'{self.title} - красного цвета, пишет красным')

class Pencil(Stationery):
    title = 'Карандаш'
    def draw(self):
        print(f'{self.title} - черного цвета, чертит черным')

class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        print(f'{self.title} - зеленного цвета, красит зеленным')

a = Stationery()
a.draw()
a1 = Pen()
a1.draw()
a2 = Pencil()
a2.draw()
a3 = Handle()
a3.draw()
