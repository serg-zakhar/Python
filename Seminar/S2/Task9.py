# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

n = int(input('Введите число: '))
if n <= 0:
    print('Число должно быть больше 0')
else:
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f'Факториал числа {n} = {factorial}')