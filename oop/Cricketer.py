class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country


class Batsman(Cricketer):
    def __init__(self, name, country, runs):
        Cricketer.__init__(self, name, country)
        self.runs = runs

    def getpoints(self):
        return self.runs // 100


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        Cricketer.__init__(self, name, country)
        self.wickets = wickets

    def getpoints(self):
        return self.wickets // 5


class AllRounder(Batsman, Bowler):
    def __init__(self, name, country, runs, wickets):
        Batsman.__init__(self, name, country, runs)
        Bowler.__init__(self, name, country, wickets)

    def getpoints(self):
        return Batsman.getpoints(self) + Bowler.getpoints(self)


b = Batsman("Abc", "India", 5000)
print(b.getpoints())
bow = Bowler("Xyz", "India", 350)
print(bow.getpoints())
a = AllRounder("Pqr", "India", 5000, 200)
print(a.getpoints())
