nums = [1,2]

def rotate(nums,k):
    n = len(nums)
    rotate = k % n
    for i in range(0,rotate):
        e = nums.pop()
        nums.insert(0,e)
    print(nums)


rotate(nums,7)
