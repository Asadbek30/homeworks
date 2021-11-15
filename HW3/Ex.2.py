N = int(input('Enter number: '))
x = 2
while x <= N:
    if x == 2 or x == 3 or x == 5 or x == 11:
        print(x)
    elif x % 2 > 0 and x % 3 > 0 and x % 5 > 0 and x % 11 > 0:
        print(x)
    x += 1