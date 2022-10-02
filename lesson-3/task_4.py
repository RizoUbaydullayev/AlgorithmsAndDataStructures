"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4


class HashedLinks:
    def __init__(self):
        self.link_storage = {}


    def add_link(self, url):
        salt = uuid4().hex
        hash_url = hashlib.pbkdf2_hmac('sha256', url.encode(), salt.encode('utf-8'), 100000)
        if self.link_storage.get(url) is None:
            self.link_storage.setdefault(url, hash_url.hex())
        else:
            return f'Хеш из кэша: {self.link_storage[url]}'


MyPlaylist = HashedLinks()

MyPlaylist.add_link('https://www.youtube.com/watch?v=tUZQSpy_Oik&list=RDDoB6v0yuGPM&index=19')
MyPlaylist.add_link('https://www.youtube.com/watch?v=vI6yG78jPnk&list=RDDoB6v0yuGPM&index=45')
MyPlaylist.add_link('https://www.youtube.com/watch?v=6kCk3J_85oY&list=RDDoB6v0yuGPM&index=46')

print(MyPlaylist.add_link('https://www.youtube.com/watch?v=tUZQSpy_Oik&list=RDDoB6v0yuGPM&index=19'))
print(MyPlaylist.add_link('https://www.youtube.com/watch?v=6kCk3J_85oY&list=RDDoB6v0yuGPM&index=46'))


