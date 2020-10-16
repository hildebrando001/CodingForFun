class Person:
    def __init__(self, name, age, height):
        self.name   = name
        self.age    = age
        self.height = height

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, height: {self.height}"

    def get_older(self, years):
        self.age += years


class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height) # "super" is accessing the parenthesis class
        self.salary = salary # This init refers to Person class


    def __str__(self):
        text = super(Worker, self).__str__()
        text += f", Salary: {self.salary}"
        return text


    def calc_yearly_salary(self):
        return self.salary * 12



worker1 = Worker("Carlos", 30, 173, 3000)
print(worker1)
print(worker1.calc_yearly_salary())

######################### OPERATORS OVERLOAD ######################################

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

v1 = Vector(5, 3)
v2 = Vector(4, 2)

print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)