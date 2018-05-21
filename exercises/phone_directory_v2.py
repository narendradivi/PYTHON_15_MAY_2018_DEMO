directory = {}

while True:
    entry = input("Enter name and phone number [end to stop] :")
    if entry == "end":
        break

    # split entry into two parts
    parts = entry.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    phone = parts[1]

    if len(phone) == 10 and phone.isdigit():
        if name in directory:  # if name is already present
            directory[name].add(phone)
        else:
            directory[name] = {phone}  # create a new entry with name and phone in set

for name, phone in sorted(directory.items()):
    print(name, sorted(phone))
