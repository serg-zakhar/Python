# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
import random

num_rates = int(input("Введите количество оценок: "))
list_rates = list(random.randint(1, 5) for _ in range(num_rates))
print(list_rates)


def change_rate(rate):
    if rate == 4:
        return 2
    elif rate == 5:
        return 1
    else:
        return rate

new_list_rate = []

for rate in list_rates:
    new_list_rate.append(change_rate(rate))

print(new_list_rate)
