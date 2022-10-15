"""
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""


class HexadecimalNumbers:

    def __init__(self, value):
        self.value = value
        self.__value_int = int(self.value, 16)

    def __mul__(self, other):
        other_int = int(other.value, 16)
        result = self.__value_int * other_int
        return hex(result)[2:].upper()

    def __add__(self, other):
        other_int = int(other.value, 16)
        result = self.__value_int + other_int
        return hex(result)[2:].upper()


first_number = HexadecimalNumbers("A2")
second_number = HexadecimalNumbers("C4F")
multiplication_hex_num = first_number * second_number
sum_hex_num = first_number + second_number
print(f'Произведение: {multiplication_hex_num}')
print(f'Сумма: {sum_hex_num}')
