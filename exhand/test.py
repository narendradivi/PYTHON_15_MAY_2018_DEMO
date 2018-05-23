t = (10,20,30)
try:
    v = int(input("Enter a number :"))
    print (t[v])
except ValueError:
    print("Sorry! Invalid number. Try again!")
# except IndexError:
#     print("Sorry! Number is too large!")
else:
    print("All good!")
finally:
    print("Done")

print("The End")





