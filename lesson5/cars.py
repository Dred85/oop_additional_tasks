"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""

import timeit


class Car:
    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age

    def get_set_del(self):
        self.age += 100
        del self.age
        self.age = 10


class CarSlots:
    __slots__ = ('brand', 'model', 'age')

    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age

    def get_set_del(self):
        self.age += 100
        del self.age
        self.age = 10


car = Car('Toyota', 'Corolla', 2022)
car_slots = Car('Toyota', 'Crown', 1990)

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)
print(f"Без слотс:{t1}, слотс:{t2}")
print((t1 - t2) / t1 * 100)
