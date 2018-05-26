
import random

def random_generator(count,start,stop):
    for i in range(1,count + 1):
        yield  random.randrange(start,stop)


for n in random_generator(10,1000,2000):
    print(n)