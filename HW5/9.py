a = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 111, 147]
count = 0
for i in a:
    if i % 3 == 0 and i % 7 > 0:
        print(i)
    count += 1


    