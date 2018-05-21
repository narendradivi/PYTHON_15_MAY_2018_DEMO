nums = [11,10,20,22,45,55,21]

def iseven(n):
    return  n % 2 == 0

def isodd(n):
    return  n % 2 != 0

# for n in nums:
#     if n % 2 == 0:
#         print(n)

snums = filter(iseven, nums)
for n in snums:
    print(n)

for n in filter(isodd,nums):
    print(n)






