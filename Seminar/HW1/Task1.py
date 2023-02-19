# Найдите сумму цифр трехзначного числа.

num = input('Введите число: ')
num_sum = int(num[0]) + int(num[1]) + int(num[2])
# while num > 0:
#     num_sum = num_sum + (num % 10)
#     num = num // 10
print(num_sum)

