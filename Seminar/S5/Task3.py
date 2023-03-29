# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

number = int(input("Введите число: "))


def check_simple_number(number):
    for div in range(2, number):
        if number % div == 0:
            return False
    return True


print(f'Число {number} простое' if check_simple_number(number) else f'Число {number} не является простым')
