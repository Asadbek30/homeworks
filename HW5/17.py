p = int(input('Enter number: '))
x = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 156]
num1 = x[0]
num2 = x[1]
for i in range(1, len(x)):
    if 0 < p - x[i] < 10:
        num1 = x[i]
        num2 = x[i]
print(num1, num2)