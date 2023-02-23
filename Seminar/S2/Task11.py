# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1

num = int(input('Введите число: '))
if num <= 1:
    print('Число должно быть больше 1')
else:
    fib_sum = 0
    fib_pos = -1
    fib1 = 0
    fib2 = 1
    i = 2
    while fib_sum <= num:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        # print(fib_sum)
        if fib_sum == num:
            fib_pos = i
        i += 1
print(fib_pos)
