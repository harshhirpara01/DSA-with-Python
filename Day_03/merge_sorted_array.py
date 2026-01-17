from more_itertools.recipes import unique

num = [1,2,3,4,5,6,5,1,2,5,47,98,5,2,3,1,4]
num2 = [8,4,5,6,3,2,1,4,5,8,9,7,4,5,1,2,36,9,5]

final = num  + num2

unique = []
for i in final:
    if i not in unique:
        unique.append(i)



print(unique)