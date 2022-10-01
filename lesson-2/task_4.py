"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

amount_of_elements = int(input('Введите количество элементов: '))


def get_summ(amount_of_elements, number=1, sum=0):
    if amount_of_elements < 1:
        print(sum)
    else:
        sum = sum + number
        get_summ(amount_of_elements-1, number=number/-2, sum=sum)


get_summ(amount_of_elements)
