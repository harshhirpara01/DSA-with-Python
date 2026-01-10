from Day_01.Extraction_of_digit_using_loop import last_digit

n = 1234
num = n
result = 0

while num >0:
    last_digit = num%10
    result  = (result*10) + last_digit
    num = num //10

if result == n:
        print("the number is palindrome")
else:
        print("the number is not palindrome")

