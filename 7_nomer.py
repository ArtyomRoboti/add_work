def convert(temp_C):
    return (temp_C * 1.8) + 32


_temp_C = int(input('Введите температуру в градусах Цельсия '))
print('Температура в Фаренгейтах =', convert(_temp_C))
