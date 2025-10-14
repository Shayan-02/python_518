import json, csv

f = open("./1.json", "r", encoding="utf-8")
data = json.load(f)
print(data)
f.close()

f = open("./1.csv", "w", encoding="utf-8")
csv.writer(f).writerow(data)
f.close()
