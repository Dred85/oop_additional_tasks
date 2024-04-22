"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""

from time import perf_counter, sleep
class Timer:

    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        self.elapsed_time = self.end - self.start
        return self.elapsed_time

with Timer() as timer:
    # sleep(1)
    with open("log.txt") as f:
        for line in f.readlines():
            print(line)
        # print(f.read())

print("Execution time:", timer.elapsed_time)
