"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit
dct = {el: el**2 for el in range(50)}
ordereddct = OrderedDict(dct)


def get_el(dct):
    for i in range(25):
        a = dct[i]


print(timeit('get_el(dct)', setup="from __main__ import get_el, dct"))
print(timeit('get_el(ordereddct)', setup="from __main__ import get_el, ordereddct"))


def add_el(dct):
    for i in range(50, 80):
        dct[i] = i**2


print(timeit('add_el(dct)', setup="from __main__ import add_el, dct"))
print(timeit('add_el(ordereddct)', setup="from __main__ import add_el, ordereddct"))

'''
Вывод: Словарь работает чуть быстрее чем OrderedDict.
В Python 3.6 и более поздних версиях нет смысла использовать OrderedDict. Так как главная задача OrderedDict является 
сохранить порядок элементов словарья. А в версиях 3.6 и более это проблема уже решена.
'''

