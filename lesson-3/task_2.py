"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import json
import hashlib
from uuid import uuid4

password = input('Введите пароль: ')
salt = uuid4().hex
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
print(f'Созданный хеш: {key.hex()}\n')

with open("passwords.json", mode="w", encoding="utf-8") as f:
    result = {
        salt: key.hex()
    }
    json.dump(result, f, indent=2, ensure_ascii=False)

with open("passwords.json", mode="r", encoding="utf-8") as f:
    result = json.load(f)


def get_password():
    new_password = input('Введите пароль еще раз для проверки: ')
    for salt, key in result.items():
        new_key = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), salt.encode('utf-8'), 100000)
        if new_key.hex() == key:
            print('Вы ввели правильный пароль')
            return
        else:
            print('Вы ввели неправильный пароль\n')
            get_password()


get_password()
