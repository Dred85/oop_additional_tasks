# Перенесите сюда свой код из прошлой домашки и продолжите работу с ним
"""
Для класс Product добавить строковое отображение в следующем виде:
Название продукта, 80 руб. Остаток: 15 шт.

В предыдущей домашке вы делали геттер для класса Category для вывода списка товаров, теперь каждый продукт имеет
реализованное строковое отображение. Вы можете вернуться к этому геттеру и оптимизировать его работу, просто преобразовав
объект продукта в строку.
Для класса Category добавить строковое отображение в следующем виде:
Название категории, количество продуктов: 200 шт.

Для удобства работы с продуктами реализовать возможность их складывать. Логика сложения должна работать так, чтобы в
итоге у вас получалась полная стоимость всех товаров на складе. Например, для товара a с ценой 100 рублей и количеством на
складе 10 и товара b с ценой 200 рублей и количеством на складе 2 результатом выполнения операции a + b должно стать значение,
полученное из 100 * 10 + 200 * 2 = 1400.
"""


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

        return f"{self.name}, количество продуктов: {sum([len(Product(**product)) for product in self.__products])} шт."


    def add_product(self, product):
        """
        Добавляет товар в категорию
        """
        self.__products.append(product)

    @property
    def products(self):
        """
        Возвращает список товаров в категории
        """
        return "".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products])


class Product:
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

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        result = self.__price * self.quantity + other.__price * other.quantity

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


data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]

categories = []
for category in data:
    products = []

    for product in category['products']:
        products.append(Product.new_product(product))
    category['products'] = products
    categories.append(Category(**category))

assert categories[0].products == '''Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
'''

category1 = Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ])

print(category1)




product1 = Product('Test', 'Test', 1000, 10)
product2 = Product('Test', 'Test', 2000, 20)

# print(product1 + product2)
# print(len(product2))
# # product_item.price = -100
# print(product_item.price)
