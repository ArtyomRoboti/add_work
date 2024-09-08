import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda f, s: f in s, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *args):
        self.words = []
        for data in args:
            self.words.append(data)
    def __call__(self, *args, **kwargs):

        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())