"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

import hashlib


def get_substrings(text):
    result_set = set()
    for i in range(len(text)):
        result_set.add(
            hashlib.sha1(text[:len(text)-i].encode()).hexdigest()
        )
    for i in range(len(text)):
        result_set.add(
            hashlib.sha1(text[i:len(text)].encode()).hexdigest()
        )
    for i in text:
        result_set.add(
            hashlib.sha1(i.encode()).hexdigest()
        )
    return f'Слово {text} {len(result_set)} уникальных подстрок'


print(get_substrings('Hello'))


'''
Hello   #1
Hell    #2
Hel     #3
He      #4
H       #5
Hello
 ello   #6
  llo   #7
   lo   #8
    o   #9
H     
 e      #10
  l     #11
   l
    o
'''