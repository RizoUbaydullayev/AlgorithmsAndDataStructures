"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join([num for num in str(enter_num)])[::-1]


print(timeit.timeit('revers(15485)', setup='from __main__ import revers'))
print(timeit.timeit('revers_2(15485)', setup='from __main__ import revers_2'))
print(timeit.timeit('revers_3(15485)', setup='from __main__ import revers_3'))
print(timeit.timeit('revers_4(15485)', setup='from __main__ import revers_4'))

'''
Самая эффективная из этих является функций revers_3. Потому что в нем не используется рекурсия и цикл. 
'''
