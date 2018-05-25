class A:
    pass
    # def print(self):
    #     print("In A")


class B:
    def print(self):
        print("In B")


class C(A, B):
    pass
    # def print(self):
    #     print("In C")


obj = C()
obj.print()


