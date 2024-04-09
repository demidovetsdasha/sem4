from BinaryAddition import BinaryAddition
from BinaryConverter import BinaryConverter
from CONST import BINARY_ZERO, ONE_ADDITION

class BinaryMultiplier:
   def __init__(self, binary_converter, binary_addition):
       self.binary_converter = binary_converter
       self.binary_addition = binary_addition

   def multiply(self, a: str, b: str) -> list[str]:
       result = BINARY_ZERO
       flag_sign = a[0] == b[0]
       if b[0] == '1':
           b = '0' + b[1:]
       while b != ''.join(BINARY_ZERO):
           additional_multiplier1 = self.binary_converter.convert_to_additional_code(self.binary_converter.convert_to_decimal(a))
           additional_result = self.binary_converter.convert_to_additional_code(self.binary_converter.convert_to_decimal("".join(result)))
           result = self.binary_addition.add_in_additional_code(additional_multiplier1, additional_result)
           b = self.binary_addition.add_in_additional_code(self.binary_converter.convert_to_additional_code(self.binary_converter.convert_to_decimal(b)), ''.join(ONE_ADDITION))
       if flag_sign:
           result = '0' + result[1:]
       else:
           result = '1' + result[1:]
       return result
