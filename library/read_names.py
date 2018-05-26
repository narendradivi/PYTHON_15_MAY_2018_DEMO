

f = open(r"e:\classroom\python\names.txt","rt")
# print(TextIOWrapper.__bases__)
names =  f.readlines()
print(type(names))
for i,n in enumerate(sorted(names)):
    print("%02d: %s" % (i + 1, n), end= '')

f.close()