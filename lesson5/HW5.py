# Перенесите сюда свой код из прошлой домашки и продолжите работу с ним
from abc import ABC, abstractmethod


class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    products: list  # Приватный атрибут для списка товаров

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum([len(product) for product in self.__products])} шт."
        # return f"{self.name}, количество продуктов: {sum([{self.name} for product in self.__products])} шт."

    def add_product(self, product_):
        """
        Добавляет товар в категорию
        """
        if isinstance(product_, Product):
            self.__products.append(product_)
        else:
            raise TypeError('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

    @property
    def products(self):
        """
        Возвращает список товаров в категории
        """
        # return "".join(
        # [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products])
        return f"{self.__products}"

    @products.setter
    def products(self, products):
        if issubclass(type(products), Product):
            self.__products = products
        else:
            raise TypeError('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, product):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, '{self.description}', {self.price}, {self.quantity})"


class Product(BaseProduct, PrintMixin):
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: float  # Приватный атрибут для цены
    quantity: int

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        result = self.__price * self.quantity + other.__price * other.quantity
        if type(other) is not Product:
            raise TypeError('Ошибка сложения. Нельзя складывать не экземпляры одного класса')
        return result

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    @classmethod
    def new_product(cls, product):
        """
        Фабричный метод для создания нового товара
        """
        name, description, price, quantity = product["name"], product["description"], product["price"], product[

            "quantity"]

        return cls(name, description, price, quantity)

    @property
    def price(self):
        """
        Геттер для цены
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для цены с проверкой
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color















