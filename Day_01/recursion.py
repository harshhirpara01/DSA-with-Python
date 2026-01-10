def greet():
    print("harsh")
    greet() # <---- it gives recursion depth error so always add base condition

greet()


#<<<<<< - with the bse condition

def greet(count):
    if count > 10:
        return
    print("harsh")
    count += 1
    greet(count)
    # <---- it gives recursion depth error so always add base condition --->>>>


greet(0)


def fun(x,n):
    if n == 0:
        return
    print(x)
    fun(x,n-1)


fun(15,8)


