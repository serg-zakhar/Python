# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

vinny_poem = input("Введите что придумал Винни-Пух: ").split()
print(vinny_poem)
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']


def count_vowels(word):
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


count = count_vowels(vinny_poem[0])


def check_vowels(vinny_poem):
    for word in vinny_poem:
        if not count == count_vowels(word):
            return False
    return True


print(f"Парам пам-пам" if check_vowels(vinny_poem) else "Пам парам")