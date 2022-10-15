"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

import collections
import timeit
lst = []
dq = collections.deque(lst)

"""
1) сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее
"""


def lst_append(lst):
    for i in range(100):
        lst.append(i)


def lst_pop(lst):
    for i in range(50):
        lst.pop()


def lst_extend(lst):
    elements = [el for el in range(100, 155)]
    lst.extend([elements])


print("list: append", timeit.timeit('lst_append(lst)', setup='from __main__ import lst, lst_append'))
print("list: pop", timeit.timeit('lst_pop(lst)', setup='from __main__ import lst, lst_pop'))
print("list: extend", timeit.timeit('lst_extend(lst)', setup='from __main__ import lst, lst_extend'), '\n')

"""
2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка и сделать выводы что и 
где быстрее
"""


def dq_appendleft(dq):
    for i in range(100):
        dq.appendleft(i)


def dq_popleft(dq):
    for i in range(50):
        dq.popleft()


def dq_extendleft(dq):
    elements = [el for el in range(100, 155)]
    dq.extendleft(elements)


print("deque: appendleft", timeit.timeit('dq_appendleft(dq)', setup='from __main__ import dq, dq_appendleft'))
print("deque: popleft", timeit.timeit('dq_popleft(dq)', setup='from __main__ import dq, dq_popleft'))
print("deque: extendleft", timeit.timeit('dq_extendleft(dq)', setup='from __main__ import dq, dq_extendleft'), '\n')

"""
3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее
"""


def lst_get_elem(lst):
    for i in range(100, 150):
        a = lst[i]


def dq_get_elem(dq):
    for i in range(100, 150):
        a = dq[i]


print("list: get element", timeit.timeit('lst_get_elem(lst)', setup='from __main__ import lst, lst_get_elem'), '\n')
print("deque: get element", timeit.timeit('dq_get_elem(dq)', setup='from __main__ import dq, dq_get_elem'))


"""
Вывод: Только метод appendleft у deque выполняется выстрее чем append у list. Во всех остальных случаях 
    (pop, popleft, extend, extendleft, получение элемента) операции со списком выполняется быстрее чем с deque.
"""