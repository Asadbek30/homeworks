dict = {
    '1st': 1,
    '2nd': 2,
    '3rd': 3,
    '4th': 4,
    '5th': 5
}

for elem in dict.values():
    for prod in elem:
        elem[prod] **= 3