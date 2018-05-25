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
        if not isinstance(other,Time):
            return False
        return self.totalseconds == other.totalseconds

    def __gt__(self, other):
        return self.totalseconds > other.totalseconds

    def __add__(self, other):
        totalsec =  self.totalseconds + other
        hours = totalsec // 3600
        mins = (totalsec - (hours * 3600)) // 60
        secs = (totalsec - (hours * 3600) - (mins * 60))
        return Time(hours,mins,secs)

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

t1 = Time(11, 20, 30)
t2 = Time(10, 20, 30)

print(t1 == t2)
print(t1 == 100)

t3 = t1 + 100
print(str(t1))
print(str(t3))

