
lines =[]
with open(r"e:\classroom\python\may15\names.txt","rt") as file:
    for line in file.readlines():
        # print(line, len(line), len(line.strip(" ")))
        if len(line.strip(" ")) == 1:
            continue

        if not line in lines:
            lines.append(line)


with open(r"e:\classroom\python\may15\names.txt","wt") as file:
    for line in  lines:
        file.write(line)

print("Remove all blank and duplicate lines!")



