# upper triangle
a = [[1, 2, 3], [4, 3, 5], [6, 5, 7]]
raw = len(a)
col = len(a[0])

for i in range(0, raw):
    for j in range(0, col):
        if j >= i:
            print(a[i][j], end=" ")

        else:
            print("*", end=" ")
    print()


# lower triangle


a = [[1, 2, 3], [4, 3, 5], [6, 5, 7]]
raw = len(a)
col = len(a[0])

for i in range(0, raw):
    for j in range(0, col):
        if j <= i:
            print(a[i][j], end=" ")

        else:
            print("*", end=" ")
    print()


# diagonal

a = [[1, 2, 3], [4, 3, 5], [6, 5, 7]]
raw = len(a)
col = len(a[0])

for i in range(0, raw):
    for j in range(0, col):
        if j == i:
            print(a[i][j], end=" ")

        else:
            print("*", end=" ")
    print()
