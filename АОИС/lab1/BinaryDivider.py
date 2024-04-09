from BinaryAddition import BinaryAddition
from BinaryConverter import BinaryConverter
from CONST import BINARY_ZERO, BINARY_ONE


class BinaryDivider:
    def __init__(self, binary_converter: BinaryConverter, binary_addition: BinaryAddition):
        self.binary_converter = binary_converter
        self.binary_addition = binary_addition

    def division(self, a: str, b: str) -> str:
        integer = "".join(BINARY_ZERO)
        flag_sign = a[0] != b[0]
        a = '0' + a[1:]
        b = '1' + b[1:]
        additional_numerator = self.binary_converter.convert_to_additional_code(self.binary_converter.convert_to_decimal(a))
        additional_denominator = self.binary_converter.convert_to_additional_code(self.binary_converter.convert_to_decimal(b))
        check_type_fraction = self.binary_addition.add_in_additional_code(additional_numerator, additional_denominator)
        if check_type_fraction[0] == '0':
            while a[0] != '1':
                a = self.binary_addition.add_in_additional_code(a, self.binary_converter.convert_to_additional_code(self.binary_converter.convert_to_decimal(b)))
                if a[0] != '1':
                    integer = self.binary_addition.add_in_additional_code("".join(integer), "".join(BINARY_ONE))
        if list(integer) == BINARY_ZERO:
            return integer
        if flag_sign:
            return '1' + integer[1:]
        else:
            return integer
