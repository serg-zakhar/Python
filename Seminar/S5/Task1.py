# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

fib_index = int(input("Введите номер числа Фибоначчи: "))


def fib(fib_index):
    if fib_index == 1:
        return 1
    elif fib_index == 0:
        return 0
    else:
        return fib(fib_index - 1) + fib(fib_index - 2)


print(fib(fib_index))
