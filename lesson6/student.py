"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def avg_rate(self):
        try:
            return sum(self.marks) / len(self.marks)
        except ZeroDivisionError:
            return 0.0


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
print(student.avg_rate())

student = Student('Ivan', 'Python', [])
print(student.avg_rate())
