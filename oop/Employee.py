class Employee:
    """
    This class is to represent an Employee
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print(self):
        print(self.name, self.salary)

    def netsalary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, hra):
        super().__init__(name, salary)
        self.hra = hra

    def print(self):
        super().print()
        print(self.hra)

    def netsalary(self):
        return self.salary + self.hra


e = Employee("Steve", 50000)
m = Manager("Bill", 70000, 30000)
print(e.netsalary())
print(m.netsalary())

print(Employee.__doc__)
print (str.__doc__)


