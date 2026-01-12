# nums = [33,56,78,746,77,43,12,3,4,5,6,7,54,65,78,98,2333]
#
#
# high = float("-inf")
#
# second_high = float("-inf")
# for i in range(0,len(nums)):
#     if nums[i] > high:
#         high = nums[i]
# print(high)
#
#
# for i in range(0,len(nums)):
#     if nums[i] > second_high and nums[i]!= high:
#         second_high = nums[i]
#
# print(second_high)

# new solution ------------------------->>>>>>>>


nums = [33,56,78,746,77,43,12,3,4,5,6,7,54,65,78,98,2333]


high = float("-inf")

second_high = float("-inf")

for i in range(0,len(nums)):
    if nums[i] > high:
        second_high = high
        high = nums[i]
    elif nums[i] > second_high and nums[i] != high:
        second_high = nums[i]

print(high)
print(second_high)
