class Person:
    def __init__(self, name, age, job):
        self.esm = name
        self.sen = age
        self.shoghl = job
    def sleep(self):
        return f"{self.esm} is sleeping"
    def info(self):
        return f"name : {self.esm} \nage : {self.sen} \njob : {self.shoghl} "
    


p1 = Person("ali", 35, "accountant")
print(p1.sleep())
print(p1.info())