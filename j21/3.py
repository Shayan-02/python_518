class Person:
    def __init__(self, name, age, job, gender):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender

    def move(self):
        pass


class Student(Person):
    def __init__(self, name, job, pid, grade):
        super().__init__(name, job)
        self.pid = pid
        self.grade = grade
    def move(self, movement):
        return f"{self.name} is {movement}ing..."


class Baby(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    def move(self, movement):
        print(f"{self.name} is {movement}ing...")


class Employee(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age, job)
        self.salary = salary
    def move(self, movement):
        return f"{self.name} is {movement}ing..."

