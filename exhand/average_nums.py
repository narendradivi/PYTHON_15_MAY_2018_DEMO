sum = 0
count = 0

while True:
    try:
        n = int (input("Enter a number [0 to stop] :"))
        if n == 0:
            break
        sum += n
        count +=1
    except:
        print("Sorry! Invalid Number.")

print("Average of numbers : ", sum // count)


