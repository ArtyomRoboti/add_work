# Нужна помощь в решение задачи
val = int(input('Задайте число: '))
begin_val = 2
while begin_val <= val:
    if begin_val % 2 == 0 or begin_val % 3 == 0:
        begin_val += 1
        continue
    print(begin_val)
    begin_val += 1
