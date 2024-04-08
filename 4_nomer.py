import random
rand_val = random.randrange(1, 100)

while 1 > 0:
    hum_val = int(input('Угадайте число от 1 до 100 '))
    if hum_val == rand_val:
        print('Поздравляю с победой!')
        break
    if hum_val > rand_val:
        print('Меньше')
    if hum_val < rand_val:
        print('Больше')
