n = 153

num = n
total = 0
digit = len(str(n))

while num>0:
    ld = num % 10
    total = total +(ld**digit)
    num = num//10

print(total)
if total == n:
    print("the number is armstrong")
else:
    print("the number is not armstrong")







