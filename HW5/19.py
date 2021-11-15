x = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 156, 25, 68, 75, 90]
max1 = x[-1]
max2 = x[-2]
max3 = x[-3]
for i in range(len(x)):
    if x[i] > max1:
        max3 = max1
        max1 = x[i]
    elif x[i] > max3:
        max3 = x[i]
    elif x[i] > max2:
        max3 = max2
        max2 = x[i]
print(max1, max2, max3)   