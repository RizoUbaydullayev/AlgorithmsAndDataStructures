"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
"""

from collections import defaultdict
from functools import reduce


def operations_with_hex():
    first_num = list(input("Введите первое число: ").strip().replace(' ', '').upper())
    second_num = list(input("Введите второе число: ").strip().replace(' ', '').upper())

    def get_decimal_number(hex_num):

        key_to_convert = defaultdict(int)
        count = 10
        ascii_code = 65
        while count < 16:
            key_to_convert[chr(ascii_code)] = count
            count += 1
            ascii_code += 1

        result = []
        hex_num.reverse()
        for ind, value in enumerate(hex_num):
            value_to_add = key_to_convert[value]
            if value_to_add == 0:
                try:
                    value_to_add = int(value)
                except ValueError:
                    print("Ошибка")
                    exit(operations_with_hex())
            result.append(value_to_add * 16 ** ind)
        return result

    first_num_decimal = reduce(lambda x, y: x+y, get_decimal_number(first_num))
    second_num_decimal = reduce(lambda x, y: x+y, get_decimal_number(second_num))
    print(f'Сумма чисел: {list(hex(first_num_decimal+second_num_decimal)[2:].upper())}')
    print(f'Произведение: {list(hex(first_num_decimal * second_num_decimal)[2:].upper())}')


operations_with_hex()



