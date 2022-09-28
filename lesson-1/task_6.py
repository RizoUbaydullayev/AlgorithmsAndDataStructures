"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.__queueBase = []
        self.__queueRevision = []
        self.__completedList = []

    # ------------------------------------------------------------------------------------------------------------------

    def showQueueBase(self):
        for number, task in enumerate(self.__queueBase):
            print(f'{number+1}. {task}')

    def showQueueRevision(self):
        for number, task in enumerate(self.__queueRevision):
            print(f'{number+1}. {task}')

    def showCompletedList(self):
        for number, task in enumerate(self.__completedList):
            print(f'{number+1}. {task}')

    def showAll(self):
        def main(tasks):
            for i in range(len(tasks)):
                print(f'{i+1}. {tasks[i]}')

        print('\tBase queue')
        main(self.__queueBase)
        print('\tQueue for revision')
        main(self.__queueRevision)
        print('\tSolved tasks')
        main(self.__completedList)

    # ------------------------------------------------------------------------------------------------------------------

    def addToQueueBase(self, taskText):
        self.__queueBase.append(taskText)

    def addToQueueRevision(self, taskNumber=0):
        if taskNumber != 0:
            self.__queueRevision.append(self.__queueBase.pop(taskNumber-1))
        else:
            for number, task in enumerate(self.__queueBase):
                print(f'{number+1}. {task}')

            taskNumber = input("\n\tEnter the number of the job you want to move to the queue for revision.")
            while (not taskNumber.isdecimal()):
                taskNumber = input("\n\tEnter the number of the job you want to move to the queue for revision")

            self.__queueRevision.append(self.__queueBase.pop(int(taskNumber) - 1))

    def addToCompletedList(self, taskNumber=0):
        if taskNumber == 0:
            for el in range(len(self.__queueBase) + len(self.__queueRevision)):
                if el == len(self.__queueBase):
                    print('\tQueue for revision')
                if el <= len(self.__queueBase)-1:
                    print(f'{el+1}. {self.__queueBase[el]}')
                if el > len(self.__queueBase)-1:
                    print(f'{el+1}. {self.__queueRevision[el - len(self.__queueBase)]}')

            taskNumber = input("\n\tEnter the number of the task you want to move to the list of completed")
            while (not taskNumber.isdecimal()):
                taskNumber = input("\n\tEnter the number of the task you want to move to the list of completed")

        if int(taskNumber) <= len(self.__queueBase):
            self.__completedList.append(self.__queueBase.pop(int(taskNumber)-1))
        if int(taskNumber) > len(self.__queueBase) and \
                len(self.__queueRevision) >= int(taskNumber) - len(self.__queueBase):
            self.__completedList.append(self.__queueRevision.pop(int(taskNumber)-len(self.__queueBase)-1))


tasksToday = TaskBoard()
tasksToday.addToQueueBase('View reports on the work of managers')
tasksToday.addToQueueBase('Listen to the call recording of the sales department in CRM')
tasksToday.addToQueueBase('Request in the accounting department data on received payments')
tasksToday.addToQueueBase('View the contract with Interpretation LLC')
tasksToday.addToQueueBase('Coordinate the layout of business cards and badges')
tasksToday.addToQueueBase('Finish the sales budget for the next month')
tasksToday.addToCompletedList(5)
tasksToday.addToQueueRevision(4)
