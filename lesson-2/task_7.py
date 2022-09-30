"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def get_sum_sequence(number, counter=1, sum=0):
    if counter == number:
        print(f'+{counter}={sum+counter}')
        return
    else:
        if counter == 1:
            print(f'{counter}', end='')
        else:
            print(f'+{counter}', end='')
        sum += counter
        get_sum_sequence(number, counter+1, sum)


def get_sum_formula(number):
    print(f'{number}({number}+1)/2={int(number*(number+1)/2)}')


get_sum_sequence(5)
get_sum_formula(5)
