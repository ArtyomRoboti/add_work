def custom_write(file_name, strings):
    strings_positions = {}
    number_col = 1
    file = open(file_name, mode='w', encoding='utf-8')
    for f in strings:
        begin_file = file.tell()
        file.write(f + '/n')
        strings_positions[(number_col, begin_file)] = f
        number_col += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
