a = [1, 1, 3, 5, 8, 13, 21, 34, 55, 89]
total = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        total = a[i] + total
print(total)
        