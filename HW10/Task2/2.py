a = [int(i) for i in input().split()]
print(*[i for i in set(a) if a.count(i) > 1])