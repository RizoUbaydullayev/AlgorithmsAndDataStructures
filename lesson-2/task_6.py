"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint
number = randint(0, 100)


def guess_number(number, tries=10, text_for_user='Введите число: '):
    if tries == 0:
        print(f'Вы не отгадали число - {number}! ')
        return

    user_number = int(input(f'{text_for_user}'))

    if user_number == number:
        print('Вы отгадали число!')
        return

    else:

        if user_number > number:
            text_for_user = 'Введите число поменьше: '
        else:
            text_for_user = 'Введите число побольше: '

        guess_number(number, tries-1, text_for_user)


guess_number(number)
