# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

print('Введите размер шоколадки')
count_length = int(input('Сколько плиток в длину: '))
count_width = int(input('Сколько плиток в ширину: '))
count_piece = int(input('Введите количество плиток, которые нужно отломить: '))

if count_piece % count_length == 0 and count_width > count_piece / count_length \
        or count_piece % count_width == 0 and count_length > count_piece / count_width:
    print('YES')
else:
    print('NO')
