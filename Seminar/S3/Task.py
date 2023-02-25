# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

import random

k = int(input('Введите число: '))
my_list = [random.randint(0, 100) for _ in range(10)]
print(my_list)

result = my_list[len(my_list) - k: len(my_list)] + my_list[:len(my_list) - k]

print(result)
# for i in range(len(my_list) - k, len(my_list)):
