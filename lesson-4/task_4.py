"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

import timeit
array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    result = {array.count(el): el for el in array}
    return f'Чаще всего встречается число {result[sorted(result.keys())[-1]]}, '\
        f'оно появилось в массиве {sorted(result.keys())[-1]} раз(а)'


print(func_1(array))
print(func_2(array))
print(func_3(array))

print(timeit.timeit('func_1([1, 3, 1, 3, 4, 5, 1])', setup='from __main__ import func_1'))
print(timeit.timeit('func_2([1, 3, 1, 3, 4, 5, 1])', setup='from __main__ import func_2'))
print(timeit.timeit('func_3([1, 3, 1, 3, 4, 5, 1])', setup='from __main__ import func_3'))

'''
У меня не получилось ускорить.
'''