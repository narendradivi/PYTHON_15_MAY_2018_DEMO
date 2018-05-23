names = ["Tom", "Steve", "Jackie", "Mike", "Micheal", "Bob", "Kim"]


def length(n):
    return len(n)


# for n in sorted(names, key=length):
#     print(n)

for n in sorted(names, key=lambda n: (len(n), n)):
    print(n)
