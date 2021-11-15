a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
count = 0
for i in a:
    if i < 11 and i % 2 > 0:
        print(a[i], end=' ')
    count += 1