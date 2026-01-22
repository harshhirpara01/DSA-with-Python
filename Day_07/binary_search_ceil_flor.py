nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 18

l = 0
h = len(nums) - 1
floor = -1
ceil = -1

while l <= h:
    mid = (l + h) // 2

    if nums[mid] == target:
        floor = nums[mid]
        ceil = nums[mid]
        break

    elif nums[mid] > target:
        ceil = nums[mid]
        h = mid - 1
    else:
        floor = nums[mid]
        l = mid + 1

print("floor:", floor)
print("ceil:", ceil)
