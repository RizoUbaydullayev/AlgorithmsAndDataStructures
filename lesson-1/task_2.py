"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


def quadratic(test_list):
    """
    Сложность: 2+2n^2 = O(n^2).
    """
    minNum = test_list[0]  # O(1)
    for i in range(len(test_list)):  # O(n)
        for y in range(len(test_list)):  # O(n)
            if test_list[i] < test_list[y] and test_list[i] < minNum:  # O(1)
                minNum = test_list[i]  # O(1)
    return minNum  # O(1)


def linear(test_list):
    """
     Сложность: n.
     """
    minNum = test_list[0]  # O(1)
    for i in test_list:    # O(n)
        if minNum > i:   # O(1)
            minNum = i   # O(1)
    return minNum   # O(1)


prices = [154554, 100, 9, 50, 74, 489, 1125, 12, 45, 10]
print(quadratic(prices))
print(linear(prices))
