a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
total = 0
for i in a:
    if a.index(i) % 2 == 0:
        total += i
print(total)
