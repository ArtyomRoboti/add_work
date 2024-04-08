def calc_IMT(_rost, _ves):
    return _ves / (_rost ** 2)


rost = float(input('Введите рост в метрах '))
ves = int(input('Введите вем в кг '))

print(f'ИМТ = {calc_IMT(rost, ves):.1f}')
