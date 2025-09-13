# d = {"apple" : ["سیب", "زمین", "مردمک چشم", "یک شرکت تکنولوژی"]}

# print(d["apple"])

d = {
    "employee1": {
        "name": {"fname": "ali", "lname": "rezaee"},
        "age": 30,
        "nid": "0987654321",
        "job": ["computer manager", "accountant"],
    },
    "employee2": {
        "name": {"fname": "reza", "lname": "akbari"},
        "age": 32,
        "nid": "1234567890",
        "job": ["doctor", "mussisian"],
    },
}
x = d["employee2"]
for i in d:
    print(i, "->", d[i])
