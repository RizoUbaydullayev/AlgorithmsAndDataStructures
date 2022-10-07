"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print('Время работы func_1: ', timeit.timeit('func_1(nums=[el for el in range(11, 50)])',
                                             setup='from __main__ import func_1'))

print('Время работы func_2: ', timeit.timeit('func_2(nums=[el for el in range(11, 50)])',
                                             setup='from __main__ import func_2'))


"""
    Функция func_2 работает быстрее, потому что в нем используется list comprehension
"""



# print(timeit.timeit('func_3(nums=[el for el in range(11, 100)])', setup='from __main__ import func_3')) #1
# print(timeit.timeit('func_4(nums=[el for el in range(11, 100)])', setup='from __main__ import func_4'))
# print(timeit.timeit('func_5(nums=[el for el in range(11, 100)])', setup='from __main__ import func_5'))
# print(timeit.timeit('func_6(nums=[el for el in range(11, 100)])', setup='from __main__ import func_6'))
