prod = lambda a, b, c : (a + b) ** (c ** ((a * b) ** (a * c)))

print(prod(a = float(input()),b = float(input()),c = float(input())))