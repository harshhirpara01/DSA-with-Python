nums = [33,56,78,746,77,43,12,3,4,5,6,7,54,65,78,98,2333]

high = nums[0]

for i in range(0,len(nums)):
    if nums[i] > high:
        high = nums[i]

print(high)