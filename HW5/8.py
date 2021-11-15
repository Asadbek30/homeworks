n = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
count = 0
for i in n:
    if i % 2 == 0:
        print(i, end = ' ')
    count += 1