class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 30)
print(p1.name)
print(p1.age)


p2 = Person(input(), int(input()))
print(p2.name)
print(p2.age)

