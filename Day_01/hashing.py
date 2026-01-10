arr = [1, 2, 2, 3, 1, 4, 2]

hash_map = {}

for num in arr:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1

print(hash_map)
