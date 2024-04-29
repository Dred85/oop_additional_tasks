"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import date


today = date.today()

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        if year <= today.year:
            self.year = year
        else:
            raise ValueError('Эта машина еще не была выпущена')


# код для проверки
car1 = Car('Toyota', 'Corolla', 2022)

car2 = Car('Toyota', 'Corolla', 2025)
print(car1.__dict__)
print(car2.__dict__)
# raises Exception('Эта машина еще не была выпущена')
