"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class Users:
    def __init__(self, login, password, statusEmail):
        if type(statusEmail) != bool:
            raise ValueError('statusEmail only accepts boolean values')
        self.login = login
        self.password = password
        self.__statusEmail = statusEmail

    def changeStatus(self):
        if self.__statusEmail:
            self.__statusEmail = False
        else:
            self.__statusEmail = True

    def accessToResources(self):
        if self.__statusEmail:
            return 'Access is allowed'
        else:
            return 'Access is denied. Change activation status to get access'

    def __str__(self):
        return f'{self.login}'

    def __repr__(self):
        return f'{self.login}'


usersList = [
    Users('alex', 'a789x', True),
    Users('mila', 'bhd89x', True),
    Users('maison', '77ahjngfs', False),
    Users('martin', 'aikidsdc', True),
    Users('leo', 'iiaksa', False)]


for user in usersList:
    print(f'{user.login}:\n\t {user.accessToResources()}\n')

"""///////////////////////////////////////////////////////////////////////////////"""