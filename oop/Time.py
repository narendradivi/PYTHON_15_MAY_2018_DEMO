class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        print("__eq__")
        return self.totalseconds == other.totalseconds

    def __gt__(self, other):
        return self.totalseconds > other.totalseconds


t1 = Time(11, 20, 30)
t2 = Time(10, 20, 30)

print(t1 == t2)
t3 = t1 + 10

