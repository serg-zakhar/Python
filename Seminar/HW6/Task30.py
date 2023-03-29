# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

print("Вывод арифметической прогрессии")
num_first = int(input("Введите первый элемент прогрессии: "))
num_count = int(input("Введите количество элементов: "))
num_step = int(input("Введите разность прогрессии: "))


def arythmetics_progression(num_first, num_count, num_step):
    arythm_list = []
    arythm_list.append(num_first)
    for i in range(2, num_count + 1):
        arythm_list.append(num_first + (i - 1) * num_step)
    return arythm_list


print(arythmetics_progression(num_first, num_count, num_step))
