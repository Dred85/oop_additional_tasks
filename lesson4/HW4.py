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
            self.__products.append(product)
        else:
            raise TypeError('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

    @property
    def products(self):
        """
        Возвращает список товаров в категории
        """

        return f"{ self.__products}"
            # [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products])


    @products.setter
    def products(self, products):
        if issubclass(type(products), Product):
            self.__products = products
        else:
           TypeError('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

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


if __name__ == '__main__':
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

    product_item = Product('Test', 'Test', 1000, 10)
    product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5, 'Xiaomi', 10000, 'red')
    product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')

    try:
        categories[0].products = 1
        # print(categories[0].products)
        # print(categories[0])
    except TypeError:
        print('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

    categories[0].products = product_item

    print(product_item.name in categories[0].products)
    # print(product_item.name)
    # print(categories[0].products)
