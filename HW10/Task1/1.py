list = [1, 3, 5, 6, 10]
sum = []

left_index = -1
right_index = -len(list) + 1
middle_index = 0

while middle_index < len(list):
    sum.append(list[left_index] + list[right_index])
    left_index += 1
    right_index += 1
    middle_index += 1

print(sum)