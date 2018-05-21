
directory = {}

while True:
    entry = input("Enter name and phone number [end to stop] :")
    if entry == "end":
        break

    # split entry into two parts
    parts = entry.split(",")
    if len(parts) < 2:
        continue

    if len(parts[1]) == 10 and parts[1].isdigit():
        directory[parts[0]] = parts[1]

for  name,phone in sorted(directory.items()):
    print(name,phone)




