# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

nums_count = int(input("Введите количество элементов в списке: "))
nums_min = int(input("Введите минимальное число в списке: "))
nums_max = int(input("Введите максимальное число в списке: "))
nums = [random.randint(-100, 100) for _ in range(nums_count)]
print(nums)

nums_index = []
for i in range(nums_count):
    if nums[i] >= nums_min and nums[i] <= nums_max:
        nums_index.append(i)

print(nums_index)
