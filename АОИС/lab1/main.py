from BinaryConverter import BinaryConverter
from BinaryAddition import BinaryAddition
from BinaryMultiplier import BinaryMultiplier
from BinaryDivider import BinaryDivider


def show_menu_positions():
    print('1. Convert decimal to binary in 3 ways')
    print('2. Add in additional code')
    print('3. Subtract decimal')
    print('4. Multiply in straight code')
    print('5. Divide in straight code')
    print('6. Convert float to binary32')
    print('7. Add to floats in binary32')


def main():
    binary_converter = BinaryConverter()
    binary_addition = BinaryAddition(binary_converter)
    binary_multiplier = BinaryMultiplier(binary_converter, binary_addition)
    binary_divider = BinaryDivider(binary_converter, binary_addition)

    while(True):
        show_menu_positions()
        match input():
            case "1":
                a = int((input("Input value = ")))
                print("Straight code: " + binary_converter.convert_to_straight_code(a))
                print("Reverse code: " + binary_converter.convert_to_reverse_code(a))
                print("Additional code: " + binary_converter.convert_to_additional_code(a))
            case "2":
                a = int((input("Input a = ")))
                b = int((input("Input b = ")))
                a = binary_converter.convert_to_additional_code(a)
                b = binary_converter.convert_to_additional_code(b)
                summa = binary_addition.add_in_additional_code(a, b)
                print("Binary result: " + summa)
                print("Decimal result: " + str(binary_converter.convert_to_decimal(summa)))
            case "3":
                a = int((input("Input a = ")))
                b = int((input("Input b = ")))
                a = binary_converter.convert_to_additional_code(a)
                b = binary_converter.convert_to_additional_code(b)
                summa = binary_addition.add_in_additional_code(a, b)
                print("Binary result: " + summa)
                print("Decimal result: " + str(binary_converter.convert_to_decimal(summa)))
            case "4":
                a = int((input("Input a = ")))
                b = int((input("Input b = ")))
                a = binary_converter.convert_to_straight_code(a)
                b = binary_converter.convert_to_straight_code(b)
                product = binary_multiplier.multiply(a, b)
                print("Binary result: " + str(product))
                print("Decimal result: " + str(binary_converter.convert_to_decimal(str(product))))
            case "5":
                a = int((input("Input a = ")))
                b = int((input("Input b = ")))
                a = binary_converter.convert_to_straight_code(a)
                b = binary_converter.convert_to_straight_code(b)
                product = binary_divider.division(a, b)
                print("Binary result: " + str(product))
                print("Decimal result: " + str(binary_converter.convert_to_decimal(str(product))))
            case "6":
                a = float((input("Input a = ")))
                a = binary_converter.convert_float_to_binary(a)
                print("Binary32 result: " + a)
            case "7":
                a = float((input("Input a = ")))
                b = float((input("Input b = ")))
                a = binary_converter.convert_float_to_binary(a)
                b = binary_converter.convert_float_to_binary(b)
                print(a,b)
                summa = binary_addition.add_binary_floats(a, b)
                print("Binary result: " + summa)
                print("Decimal result: " + str(binary_converter.convert_binary_to_float(summa)))


main()
