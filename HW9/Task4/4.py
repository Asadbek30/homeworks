my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
prod = 1
for elem in my_dictionary:
    prod *= my_dictionary[elem]
print(prod)