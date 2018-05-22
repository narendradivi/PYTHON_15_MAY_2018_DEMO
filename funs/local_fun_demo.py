n = 100
def f1():
    print("In f1()")
    global  n
    n = n + 10
    # Local function
    def f2():
        nonlocal n
        n = 20
        print(n)

    f2()
    print("In f1()", n)

# call fun f1
f1()
print("Global ", n)
