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

        return "".join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products])


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

    @classmethod
    def new_product(cls, product):
        """
        Фабричный метод для создания нового товара
        """
        name, description, price, quantity = product["name"], product["description"], product["price"], product["quantity"]
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

product_item = Product('Test', 'Test', 1000, 10)
print(product_item.price)

product_item.price = -100
print(product_item.price)