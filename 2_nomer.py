val = int(input('Введите вес посылки в кг '))
if val <= 2:
    print('Цена доставки 50 рублей')
if val > 2 and val < 10:
    diff_val = val - 2
    coin = 50 + (20 * diff_val)
    print('Цена доставки', coin, 'рублей')
if val >= 10:
    print('Цена доставки 200 рублей')

