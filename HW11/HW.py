def wholivesHigher(floor, porch, flat, name, flatname, name1, flatname1):
    a = (flatname % 10) / 3
    b = (flatname1 % 10) / 3 
    if a > b:
        print(name)
    else:
        print(name1)
print(wholivesHigher(10, 3, 3, 'Elbek', 69, 'MS', 59))