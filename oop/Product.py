class Product:
    taxper = 15  # static or class attribute

    @staticmethod
    def settaxper(newtaxper):
        Product.taxper = newtaxper

    def __init__(self, name, price=None):
        self.__name = name  # object or instance attributes
        self.__price = price

    def __str__(self):
        return "%s - %d" % (self.__name, 0 if self.__price is None else self.__price)

    def print(self):
        print(self.__name, self.__price)

    @property
    def netprice(self):
        return (self.__price * Product.taxper / 100) + self.__price

    @netprice.setter
    def netprice(self, value):
        pass


Product.settaxper(17)
p1 = Product("iPhone X", 80000)  # Create object
p2 = Product("Samsung S9", 70000)  # Create object

print(p1.netprice)
