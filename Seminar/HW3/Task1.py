# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

num = int(input(f'Ведите количество чисел в списке: '))
num_x = int(input(f'Ведите искомое число: '))
num_list = []
count = 0
num_max1 = num_max2 = 0
num_diff = 100
for i in range(num):
    num_list.append(random.randint(1, 100))
    if num_list[i] == num_x:
        count += 1
    elif num_list[i] > num_x and num_list[i] - num_x < num_diff:
        num_max1 = num_list[i]
        num_diff = num_list[i] - num_x
    elif num_list[i] < num_x and num_x - num_list[i] < num_diff:
        num_max2 = num_list[i]
        num_diff = num_x - num_list[i]

print(num_list)

if count != 0:
    print(f'Искомое число {num_x} встречается в заданном списке: {count} раз')
else:
    if num_max1 != 0 and num_max2 != 0 and num_max1 - num_x == num_max2 - num_x:
        print(f'Искомое число {num_x} отсутствует в списке, самые близкие ему по значению: {num_max1}, {num_max2}')
    elif num_max1 != 0 and num_max2 != 0 and num_max1 - num_x > num_x - num_max2 or num_max1 == 0:
        print(f'Искомое число {num_x} отсутствует в списке, самое близкое ему по значению: {num_max2}')
    elif num_max1 != 0 and num_max2 != 0 and num_max1 - num_x < num_x - num_max2 or num_max2 == 0:
        print(f'Искомое число {num_x} отсутствует в списке, самое близкое ему по значению: {num_max1}')
