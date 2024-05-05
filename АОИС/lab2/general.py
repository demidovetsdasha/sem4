from constant import *
from typing import Dict


def check_input(formula: str) -> bool:
    valid_characters = "abcde|&!~->()"
    for i in formula:
        if valid_characters.find(i) == -1:
            return False
    return True  # 'a' in formula and 'b' in formula and 'c' in formula and 'd' in formula and 'e' in formula


def create_sknf(table: Dict[int, list], variables: list) -> str:
    sknf = ''
    for i in range(len(table)):
        if table[i][LAST] == 0:
            sknf += '('
            for j in range(len(table[i]) - 1):
                if table[i][j] == 0:
                    sknf += f'{variables[j]}|'
                else:
                    sknf += f'(!{variables[j]})|'
            sknf = sknf[:LAST]
            sknf += ')&'
        else:
            continue
    if sknf[LAST] == '&':
        sknf = sknf[:LAST]
    return sknf


def create_sdnf(table: dict[int, list], variables: list) -> str:
    sdnf = ''
    for i in range(len(table)):
        if table[i][LAST] == 1:
            sdnf += '('
            for j in range(len(table[i]) - 1):
                if table[i][j] == 0:
                    sdnf += f'(!{variables[j]})&'
                else:
                    sdnf += f'{variables[j]}&'
            sdnf = sdnf[:LAST]
            sdnf += ')|'
        else:
            continue
    if sdnf[LAST] == '|':
        sdnf = sdnf[:LAST]
    return sdnf


def binary_num_sknf(table: dict[int, list], variables: list) -> str:
    bi_sknf = '&('
    for i in range(len(table)):
        if table[i][LAST] == 0:
            for j in range(len(variables)):
                bi_sknf += str(table[i][j])
            bi_sknf += ','
    if bi_sknf[LAST] == ',':
        bi_sknf = bi_sknf[:LAST] + ')'
    return bi_sknf


def decimal_num_sknf(table: dict[int, list], variables: list) -> str:
    d_sknf = '&('
    for i in range(len(table)):
        if table[i][LAST] == 0:
            interval = ''
            for j in range(len(variables)):
                interval += str(table[i][j])
            interval = index_form_decimal(interval)
            d_sknf += interval
            d_sknf += ','
    if d_sknf[LAST] == ',':
        d_sknf = d_sknf[:LAST] + ')'
    return d_sknf


def binary_num_sdnf(table: dict[int, list], variables: list) -> str:
    bi_sdnf = '|('
    for i in range(len(table)):
        if table[i][LAST] == 1:
            for j in range(len(variables)):
                bi_sdnf += str(table[i][j])
            bi_sdnf += ','
    if bi_sdnf[LAST] == ',':
        bi_sdnf = bi_sdnf[:LAST] + ')'
    return bi_sdnf


def decimal_num_sdnf(table: dict[int, list], variables: list) -> str:
    d_sdnf = '|('
    for i in range(len(table)):
        if table[i][LAST] == 1:
            interval = ''
            for j in range(len(variables)):
                interval += str(table[i][j])
            interval = index_form_decimal(interval)
            d_sdnf += interval
            d_sdnf += ','
    if d_sdnf[LAST] == ',':
        d_sdnf = d_sdnf[:LAST] + ')'
    return d_sdnf


def index_form(table: dict[int, list]) -> str:
    index = ''
    for i in range(len(table)):
        index += str(table[i][LAST])
    return index


def index_form_decimal(x: str) -> str:
    total = 0
    step = 0
    for i in range(len(x) - 1, -1, -1):
        if x[i] == "1":
            total += pow(2, step)
        step += 1

    return str(total)
