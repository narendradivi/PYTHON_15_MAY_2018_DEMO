from  datetime import datetime

f = open("persons.txt")

persons = {}
total = 0
for line in f.readlines():
    line = line.strip("\n")
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    try:
        # print(parts[1], len(parts[1]))
        dob = datetime.strptime(parts[1],"%d-%m-%Y")
    except ValueError as ex:
        # print(ex, type(ex))
        continue

    age = (datetime.now() - dob).days // 365
    persons[name] = age
    total = total + age


f.close()
avgage = total // len(persons)

for  name,age in sorted(persons.items(), key = lambda x : x[1]):
    print("%-20s  %3d  %2d" %  (name, age , age - avgage))
