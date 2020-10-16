class Person:
    amount = 0 # Amount of person
    def __init__(self, name, age, height): # constructor
        self.name   = name
        self.age    = age
        self.height = height
        Person.amount += 1 # For each new person

    def __del__(self):  # We also can define a destructor
         Person.amount -= 1 # Countdown when a Person is removed

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def get_older(self, years): # We can define all kind of functions
        self.age += years

person1 = Person("Alessandra", 23, 165)
print(person1.name,' is ',person1.age,' years old, and he is ',person1.height,' tall.')
# Output = Alessandra  is  23  years old, and he is  165  tall.

print(Person.amount)

person2 = Person("Lavinia", 23, 165)
print(person2) # Output = Name: Lavinia, Age: 23, Height: 165 # Using __str__ 

print(Person.amount)

del(person1)

print(Person.amount)



