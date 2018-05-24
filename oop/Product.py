class Product:
    def __init__(self, name, price=None):
        self.__name = name
        self.__price = price

    def __str__(self):
        return "%s - %d" % (self.__name, 0 if self.__price is None else self.__price)

    def print(self):
        print(self.__name, self.__price)

    @property
    def netprice(self):
        return self.__price * 1.15

    @netprice.setter
    def netprice(self,value):
        pass


p1 = Product("iPhone X", 80000)  # Create object
print (p1.netprice)
p1.netprice = 95000



