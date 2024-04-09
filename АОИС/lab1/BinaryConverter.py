from CONST import *
from math import frexp, ldexp


class BinaryConverter:
    def convert_to_binary(self, a: int) -> str:
        result = ""
        a = abs(a)

        while a > 0:
            y = str(a % 2)
            result = y + result
            a = int(a / 2)

        zeros_count: int = BIT_SIZE - 1 - len(result)
        result = zeros_count * "0" + result

        return result

    def convert_to_decimal(self, a: str) -> int:
        total = 0
        j = 0

        for i in range(len(a) - 1, 0, -1):
            if a[i] == "1":
                total += pow(2, j)
            j += 1

        if a[0] == "0":
            return total

        result = int("-" + str(total))
        return result

    def convert_to_straight_code(self, a: int) -> str:
        result = self.convert_to_binary(a)
        if a >= 0:
            result = "0" + result

        if a < 0:
            result = "1" + result

        return result

    def convert_to_reverse_code(self, a: int) -> str:
        result = self.convert_to_binary(a)
        if a >= 0:
            result = "0" + result

        if a < 0:
            total = list(result)
            for i in range(0, len(total)):
                if total[i] == "0":
                    total[i] = "1"
                else:
                    total[i] = "0"
            result = "1" + "".join(total)

        return result

    def convert_to_additional_code(self, a: int) -> str:
        result = self.convert_to_binary(a)
        if a >= 0:
            result = "0" + result

        if a < 0:
            result = self.convert_to_reverse_code(a)
            total = list(result)
            for i in range(len(total) - 1, -1, -1):
                if total[i] == "0":
                    total[i] = "1"
                    break
                if total[i] == "1":
                    total[i] = "0"
            result = "".join(total)

        return result

    def convert_float_to_binary(self, number):
        sign = 0 if number >= 0 else 1
        number = abs(number)

        if number == 0:
            return "0" * 32
        elif number == float("inf"):
            return str(sign) + "1" * 8 + "0" * 23

        integer_part = int(number)
        fractional_part = number - integer_part

        binary_integer_part = ""
        while integer_part:
            binary_integer_part = str(integer_part % 2) + binary_integer_part
            integer_part //= 2

        binary_fractional_part = ""
        while len(binary_fractional_part) < 23:
            fractional_part *= 2
            bit = int(fractional_part)
            fractional_part -= bit
            binary_fractional_part += str(bit)

        exponent = len(binary_integer_part) - 1
        exponent_bits = exponent + 127

        mantissa = (binary_integer_part[1:] + binary_fractional_part)[:23]
        binary_exponent = bin(exponent_bits)[2:].zfill(8)
        return str(sign) + binary_exponent + mantissa

    def convert_binary_to_float(self, binary_str: str) -> float:
        sign = int(binary_str[0])
        exponent = int(binary_str[1:9], 2) - 127
        mantissa = "1" + binary_str[9:]

        decimal_mantissa = 0
        for i, bit in enumerate(mantissa):
            decimal_mantissa += int(bit) * 2 ** (-i)

        result = decimal_mantissa * (2 ** exponent)
        if sign == 1:
            result = -result

        return result





