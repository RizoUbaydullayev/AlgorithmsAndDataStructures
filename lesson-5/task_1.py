"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple, defaultdict


def get_average_profit():
    company_profits = namedtuple('companies', 'q1 q2 q3 q4 average_profit')
    companies = defaultdict(int)
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    sum_average_profit = 0

    for i in range(count):
        company_name = input("Введите название предприятия: ")
        while company_name in companies.keys():
            company_name = input("Это предприятие уже есть в списке. Введите другое: ")

        profit_for_year = input(
            'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): '
        ).split()

        profit_current = company_profits(
            q1=profit_for_year[0],
            q2=profit_for_year[1],
            q3=profit_for_year[2],
            q4=profit_for_year[3],
            average_profit=sum([int(quarter) for quarter in profit_for_year])/len(profit_for_year)
        )

        companies[company_name] = profit_current

        sum_average_profit += profit_current.average_profit

        result_above_average = 'Предприятия, с прибылью выше среднего значения:'
        result_below_average = 'Предприятия, с прибылью ниже среднего значения:'

        for el in companies:
            if companies[el].average_profit > sum_average_profit/count:
                result_above_average += f' {el}'
            else:
                result_below_average += f' {el}'

    return f'{sum_average_profit/count}\n{result_above_average}\n{result_below_average}'


print(get_average_profit())
