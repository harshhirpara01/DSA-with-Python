
nums = [1,2,3,4,5,3,4,5,6,7,43]

# place last element at first in existing array
n = len(nums)


nums = [nums[-1]] + nums[0:n-1] #this will create new array with same name but memeory location is diffrent


print(nums)



nums[:] = [nums[-1]] + nums[0:n-1] # this will update value in same array

print(nums)

