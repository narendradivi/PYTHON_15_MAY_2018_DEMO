import os

startdir = r"e:\classroom\python\may15\demo"

files = os.walk(startdir)

for dir in files:
    if dir[0].find(".git") >= 0 :
        continue

    print("Directory : ", dir[0])

    for file in dir[2]:
        if file.endswith(".py"):
            print("   ", file)



