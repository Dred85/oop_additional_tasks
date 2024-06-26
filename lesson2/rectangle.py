"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def display(self):
        print(f'ширина: {self.width}, длина: {self.height}, площадь: {self.area()}, периметр: {self.perimeter()}')
    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        width = round(diagonal / (1 + aspect_ratio ** 2) ** 0.5, 2)
        height = round((diagonal * aspect_ratio) / (1 + aspect_ratio ** 2) ** 0.5, 2)
        return cls(width, height)

    @staticmethod
    def is_square(width, height):
        return True if width == height else False





# код для проверки
rectangle = Rectangle(4, 5)


rectangle.display()
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
