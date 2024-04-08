yaer = int(input("Введите год "))
if yaer % 4 == 0 and yaer % 100 != 0:
    print('Год', yaer, 'високосный')
else:
    print('Год', yaer, 'не високосный')