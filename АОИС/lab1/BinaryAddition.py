from typing import List
from BinaryConverter import BinaryConverter
from CONST import *

class BinaryAddition:
    def __init__(self, binary_converter: BinaryConverter):
        self.binary_converter = binary_converter

    def __add_binary(self, first_el: list[str], second_el: list[str]) -> list[str]:
        result = []
        count = 0
        for i in range(len(first_el) - 1, -1, -1):
            if int(first_el[i]) + int(second_el[i]) + count == 3:
                result.insert(0, "1")
                count = 1
            elif int(first_el[i]) + int(second_el[i]) + count == 2:
                result.insert(0, "0")
                count = 1
            elif int(first_el[i]) + int(second_el[i]) + count == 1:
                result.insert(0, "1")
                count = 0
            else:
                result.insert(0, "0")
                count = 0

        if count == 1:
            result.insert(0, "1")

        return result

    def add_in_straight_code(self, a: str, b: str) -> str:
        first, second = list(a), list(b)
        result = self.__add_binary(first, second)
        return "".join(result)

    def add_in_reverse_code(self, a: str, b: str) -> str:
        first, second = list(a), list(b)

        result = self.__add_binary(first, second)

        if len(result) > BIT_SIZE:
            result.pop(0)
            result = self.__add_binary(result, BINARY_ONE)

        if result[0] == "1":
            for i in range(1, len(result)):
                if result[i] == "0":
                    result[i] = "1"
                else:
                    result[i] = "0"

        return "".join(result)

    def add_in_additional_code(self, a: str, b: str) -> str:
        first, second = list(a), list(b)
        result = self.__add_binary(first, second)

        if len(result) > BIT_SIZE:
            result.pop(0)

        if result[0] == "1":
            for i in range(1, len(result)):
                if result[i] == "0":
                    result[i] = "1"
                else:
                    result[i] = "0"
            for i in range(len(result) - 1, -1, -1):
                if result[i] == "0":
                    result[i] = "1"
                    break
                if result[i] == "1":
                    result[i] = "0"

        return "".join(result)

    def add_binary_floats(self, a, b):
        assert len(a) == 32 and len(b) == 32, "Binary strings must be 32 bits long"

        sign_a = int(a[0])
        sign_b = int(b[0])
        exponent_a = int(a[1:9], 2)
        exponent_b = int(b[1:9], 2)
        mantissa_a = int(a[9:], 2)
        mantissa_b = int(b[9:], 2)

        exponent_a -= 127
        exponent_b -= 127

        mantissa_a += 2 ** 23
        mantissa_b += 2 ** 23

        if sign_a == 1:
            mantissa_a = -mantissa_a
        if sign_b == 1:
            mantissa_b = -mantissa_b

        if exponent_a > exponent_b:
            mantissa_b >>= (exponent_a - exponent_b)
        else:
            mantissa_a >>= (exponent_b - exponent_a)

        result_mantissa = mantissa_a + mantissa_b

        if result_mantissa < 0:
            result_sign = 1
            result_mantissa = -result_mantissa
        else:
            result_sign = 0

        result_exponent = max(exponent_a, exponent_b)
        result_exponent += 127

        if result_mantissa < 0:
            result_mantissa = -result_mantissa
        result_mantissa >>= 1

        while result_mantissa >= 2 ** 23:
            result_mantissa >>= 1
            result_exponent += 1

        result_exponent_binary = format(result_exponent, '08b')
        result_mantissa_binary = format(result_mantissa, '023b')

        result_binary = str(result_sign) + result_exponent_binary + result_mantissa_binary

        return result_binary


    '''def add_binary_floats(self, a, b):
        assert len(a) == 32 and len(b) == 32, "Binary strings must be 32 bits long"

        result_sign = 1

        sign1 = -1 if a[0] == '1' else 1
        sign2 = -1 if b[0] == '1' else 1

        exponent1 = self.binary_converter.convert_to_decimal(a[1:9]) - 127
        exponent2 = self.binary_converter.convert_to_decimal(b[1:9]) - 127

        mantissa1 = 1 + self.binary_converter.convert_to_decimal(a[9:]) / (2 ** 23)
        mantissa2 = 1 + self.binary_converter.convert_to_decimal(b[9:]) / (2 ** 23)

        # Проверяем, какая мантисса больше и при необходимости выравниваем их по экспоненте
        if exponent1 < exponent2:
            mantissa1 *= 2 ** (exponent2 - exponent1)
            exponent1 = exponent2
        else:
            mantissa2 *= 2 ** (exponent1 - exponent2)
            exponent2 = exponent1

        # Обрабатываем случаи с разными знаками
        if sign1 == sign2:
            mantissa_result = mantissa1 + mantissa2
        else:
            # Если знаки разные, просто складываем мантиссы и выбираем знак большей по модулю мантиссы
            mantissa_result = abs(mantissa1 - mantissa2)
            result_sign = sign1 if abs(mantissa1) > abs(mantissa2) else sign2

        # Нормализуем мантиссу и корректируем экспоненту при необходимости
        while mantissa_result >= 2:
            mantissa_result /= 2
            exponent1 += 1

        # Проверяем на переполнение экспоненты
        if exponent1 > 127:
            return "Overflow"

        # Если знак не определен в случае разных знаков, выбираем знак первого числа
        if sign1 != sign2:
            result_sign = sign1

        return self.binary_converter.convert_float_to_binary(result_sign * mantissa_result * (2 ** exponent1))'''

