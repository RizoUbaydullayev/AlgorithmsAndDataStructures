"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companyProfits = {
    'Exxon_Mobil': 290,
    'Volkswagen': 278,
    'Walmart': 514,
    'Sinopec_Group': 415,
    'BP': 304,
    'Royal Dutch Shell': 397,
    'China_National_Petroleum': 393,
    'Saudi Aramco': 356,
    'Toyota_Motor': 273,
    'Apple': 265,
}


def solution_1(testDict):
    """
    Сложность O(n)
    Это решение намного эффективнее.
    """
    result = [value for value in sorted(testDict.items(), reverse=True, key=lambda sort_val: sort_val[1])]  # O(n)
    return result[:3]


def solution_2(testDict):
    """
    Сложность O(n)
    """
    result = {}
    count = 0
    testDictSort = {k: v for k, v in sorted(testDict.items(), reverse=True, key=lambda sort_val: sort_val[1])}  # O(n)
    for k, v in testDictSort.items():  # O(n)
        result[k] = testDictSort[k]
        count += 1
        if count == 3:
            break
    return result


print(solution_1(companyProfits))
print(solution_2(companyProfits))
