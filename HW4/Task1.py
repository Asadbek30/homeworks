n = int(input('Enter number: '))
x = 0
while n > 0:
    y = n % 10
    n //= 10
    x *= 10
    x += y
print(x)