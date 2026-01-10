n = 5438

num = n
count =0
while num > 0:
    count+=1
    num= num//10

print(count)


################ ------>>>> Add some mathamatics and try to solve same <<<<------- ##############

from math import *

nn = 5438
nums = nn
def count_digit(nums):
    return int(log10(nums)+1)

a = count_digit(nums)
print(a)