nums = [1,2,3,4,5,3,6,7,8,8,8,9,10]

dict = {}
n = len(nums)

for i in range(0,n):
    dict[nums[i]] = 0
    j = 0
    for k in dict:
        nums[j] = k
        j+=1

print(j)


print(dict)
print(nums)