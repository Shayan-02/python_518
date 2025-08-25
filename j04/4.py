fname = input("enter your firstname: ")
lname = input("enter your lastname: ")
age = int(input("enter your age: "))
fullname = fname + " " + lname
print("your fullname is", fullname, "\nyour age is", age)
print(f"your fullname is {fullname} \nyour age is {age}")
print("your fullname is {} \nyour age is {}".format(fullname, age))