# n = 1234
# num = n
# result = 0
#
# while num >0:
#     last_digit = num%10
#     result  = (result*10) + last_digit
#     num = num //10
#
# if result == n:
#         print("the number is palindrome")
# else:
#         print("the number is not palindrome")

a = 153
n = a
digit = len(str(a))
total = 0

while a > 0:
    ld = n % 10
    total = total + (ld ** digit)
    n = n // 10

print(total)