import os


def filecontains(file, st):
    print(file)
    with open(file, "rt") as f:
        for line in f.readlines():
            if line.find(st) >= 0:
                return True
        else:
            return False


startdir = r"e:\classroom\python\may15\demo"
st = "print"

files = os.walk(startdir)

for dir in files:
    if dir[0].find(".git") >= 0:
        continue

    print("Directory : ", dir[0])

    for file in dir[2]:
        if file.endswith(".py"):
            if filecontains(dir[0] + "\\" + file, st):
                print("  ", file)
