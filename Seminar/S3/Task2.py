# Задаем список из рандомных чисел (рандомной длины),
# нужно составить новый список только с уникальными значениями

import random

my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

dictionary = {}

for element in my_list:
    if dictionary.__contains__(element):
        dictionary[element] += 1
    else:
        dictionary[element] = 1

result = []

for (i, j) in dictionary.items():
    if j == 1:
        result.append(i)

print(result)
