val = int(input('Введите число от 1 до 10 '))
begin_ = 1
for i in range(1, 11):
    print(f'{val} * {begin_} = {val * begin_}')
    begin_ += 1
