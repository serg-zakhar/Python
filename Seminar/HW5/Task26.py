# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

num = int(input("Введите число: "))
num_degree = int(input("Введите степень числа: "))


def num_deg(num, num_degree):
    if num_degree == 1:
        return num
    if num_degree > 1:
        return num * num_deg(num, num_degree - 1)


print(f'Число {num} в степени {num_degree} равно:  {num_deg(num, num_degree)}')
