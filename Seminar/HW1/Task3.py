# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

num = input('Введите номер билета: ')
if len(num) != 6:
    print('Число должно быть шестизначным!')
else:
    sum1 = 0
    sum2 = 0
    for i in range(3):
        sum1 = sum1 + int(num[i])
    for i in range(3, 6):
        sum2 = sum2 + int(num[i])
    if sum1 == sum2:
        print('Билет счастливый!')
    else:
        print('Может в следующий раз повезет')
