"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class Stack:
    def __init__(self, name):
        self.countStack = 0
        self.elementsStack = 0
        self.__name = name

    def addElements(self, amount):
        if amount < 0:
            raise ValueError(f"Enter a number greater than zero!")
        addedElements = self.elementsStack + amount
        while addedElements >= 10:
            self.countStack += 1
            addedElements -= 10
            print(f'a new stack of 10 {self.__name} is formed')

        self.elementsStack = addedElements
        print(f'\t{self.countStack + 1} stacks contain {self.elementsStack} {self.__name}')
        print('___________________________________')


Plates = Stack('plates')
Plates.addElements(15)
Plates.addElements(5)
Plates.addElements(5)
Plates.addElements(0)
Plates.addElements(41)
