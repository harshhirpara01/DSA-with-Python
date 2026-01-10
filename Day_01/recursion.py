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



#functional recursion

def func(sum,i,n):
    if i > n:
        print(sum)
        return
    func(sum+i,i+1,n)

func(sum,1,9)


#factorial using recursion


def fun(n):
    if n==0 or n ==1:
        return 1
    return n * fun(n-1)

fun(5)


# reverse the array

def fun(nums,left,right):
    if left >=right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    fun(nums,left+1,right-1)


fun([7,98,9,9,6,6,5,8],1,8)

# palindrom using recursion

def fun(s,left,right):
    if left>=right:
        return True

    if s[left] !=  s[right]:
        return False

    return fun(s,left,right-1)



#fibonaaci using recursion

def fibo(num):
    if num==0 or num==1:
        return 1
    return fibo(num-10) + fibo(num-2)





