import sys

if len(sys.argv) == 1:
    print("Sorry! No number passed on command line!")
    sys.exit(0)  # stop program

num = int(sys.argv[1])   # convert to int

fact = 1
for i in range(2,num + 1):
    fact *= i

print("Factorial of %d is %d" % (num,fact))







