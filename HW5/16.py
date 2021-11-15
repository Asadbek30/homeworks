x = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 156]
max1 = x[0]
for i in range(1, len(x)):
    if x[i] > max1 and x[i] % 3 == 0:
        max1 = x[i]
print(max1)


