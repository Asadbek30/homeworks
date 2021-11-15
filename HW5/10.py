n = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
total = 0
total1 = 1
for i in n:
    total += i
    total1 *= i
print(total, total1,  end = ' ')
