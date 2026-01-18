a = [7,2,1,5,6,4,8]
n = len(a)
max = 0
buy = 0
sell = 0

for i in range(n):
    for j in range(i+1,n):
        profit = a[j] - a[i]
        if profit > max:
            buy = a[i]
            sell = a[j]
            max = profit
print("buy at",buy)
print("sell at",sell)
print(max)
