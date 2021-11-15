x = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 156]
max1 = 1
max2 = -1
for i in range(len(x)):
    if x[i] < max1:
        max2 = max1
        max1 = x[i]
    elif x[i] > max2:
        max2 = x[i]

print(max1+max2)