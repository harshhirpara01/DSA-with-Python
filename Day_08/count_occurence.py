a = [1,2,3,3,4,4,4,5,5,6,7,8,8,8,9,9,9,9,10]
n = len(a)
count = 0
target = 9
for i in range(0,n):
    if a[i] == target:
        count +=1

print(count)