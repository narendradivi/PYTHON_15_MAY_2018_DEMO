
class Countries:
    def __iter__(self):
        print("__iter__")
        self.names = ["India","US","UK"]
        self.pos = 0
        return self

    def __next__(self):
        print("__next__")
        if self.pos == len(self.names):
            raise StopIteration
        else:
            self.pos = self.pos + 1
            return self.names[self.pos - 1]


cobj = Countries()
for c in cobj:
    print(c)
