a = [5,9,1,2,4,15,6,3]


for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == 13:
            print(i,j)
