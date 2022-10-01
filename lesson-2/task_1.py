"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc():

    def get_operation():
        operation = input('Введите операцию (+, -, *, / или 0 для выхода):')
        if len(operation) > 1 or operation not in ['+', '-', '/', '*', '0']:
            print('Ошибка!!\n')
            return get_operation()
        return operation

    def get_number(text_for_user='Введите число:'):
        number = input(f'{text_for_user}')
        try:
            float(number)
            return float(number)
        except ValueError:
            print('Ошибка!!')
            return get_number(f'{text_for_user}')

    def performing_an_operation(first_number, second_number, operation):
        if operation == '+':
            return first_number + second_number
        if operation == '-':
            return first_number - second_number
        if operation == '/':
            return first_number / second_number
        if operation == '*':
            return first_number / second_number

    # ------------------------------------------------------------------------

    operation = get_operation()  # получаем от пользователья что он хочет

    if operation.strip() == '0':  # провка на завершение программы
        return

    first_number = get_number(text_for_user='Введите первое число:')  # получаем первое число
    second_number = get_number(text_for_user='Введите второе число:')  # получаем второе число
    result = performing_an_operation(first_number, second_number, operation)

    if str(result).split('.')[1] == '0':  # если результат в виде [число].[нули] то выводим ответ без нулей
        print(f'Ваш результат: {int(result)}\n')
    else:
        print(f'Ваш результат: {result}\n')
    calc()


calc()
