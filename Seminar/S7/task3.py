# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

values = []


def same_by(func, values: list):
    my_list = list(map(func, values))
    print(my_list)
    my_list = set(my_list)
    print(my_list)
    if len(my_list) <= 1:
        return True
    else:
        return False


if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
