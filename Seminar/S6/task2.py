# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

import random

nums_count = int(input("Введите количество элементов в массиве: "))
nums = [random.randint(10, 99) for _ in range(nums_count)]
print(nums)

nums_big = []

for i in range(1, nums_count - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        nums_big.append(nums[i])
print(len(nums_big))
print(nums_big)
