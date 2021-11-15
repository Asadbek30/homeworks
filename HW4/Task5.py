x = 0
while x <= 100:
    N = int(input('Enter number: '))
    x += N
    if x > 100:
        print('Error')
    else:
        print(x)