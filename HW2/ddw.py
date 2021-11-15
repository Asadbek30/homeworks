x = int(input('Enter number: '))
if x == 1:
    print(False)
elif x % 2 > 0 and x % 3 > 0:
    print(True)
elif 2 <= x <= 3:
    print(True)
else:
    print(False)