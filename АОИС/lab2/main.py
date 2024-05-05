from general import *
from true_table import *


def main():
    formula = input("Input formula: ")

    if not check_input(formula):
        raise Exception('Invalid input!')

    table, variables = true_table(formula)

    print("_" * 60)

    print(f'SKNF: {create_sknf(table, variables)}')
    print(f'SDNF: {create_sdnf(table, variables)}')

    print("_" * 60)

    print(f'SKNF in binary form:{binary_num_sknf(table, variables)}')
    print(f'SKNF in decimal form:{decimal_num_sknf(table, variables)}')

    print("_" * 60)

    print(f'SDNF in binary form:{binary_num_sdnf(table, variables)}')
    print(f'SDNF in decimal form:{decimal_num_sdnf(table, variables)}')

    print("_" * 60)
    print(f'INDEX binary:{index_form(table)}')
    print(f'INDEX decimal:{index_form_decimal(index_form(table))}')


if __name__ == "__main__":
    main()
