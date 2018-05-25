class A:
    def print(self):
        print("In A")


class B(A):
    pass
    # def print(self):
    #     print("In B")


class C:
    def print(self):
        print("In C")


class D(B,C):
    pass


obj = D()
print( D.__mro__)
obj.print()





