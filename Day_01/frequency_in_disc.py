import requests

nums = [5,4,1,2,5,8,9,6,3,2,5,8,7,4,5,1,2,3,6,9,8,5,4]


hash = {}

n = len(nums)

for i in range(0,n):
    hash[nums[i]] = hash.get(nums[i],0)+1

print(hash)

url = "https://backend.faithdex.io/api/v1/explore/faithrate?chainId=56"

a = requests.get(url)

print(a.json())