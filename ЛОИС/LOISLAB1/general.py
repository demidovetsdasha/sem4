"""
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнили Демидовец Д.В., Тагиева П.К.
Дата выполнения 25.05.2024

Файл с реализацией ключевых методов для работы с логическими формулами
"""

from constant import *
from typing import Dict
import re

# подсчет количества символа в строке
def calculate_chars(line, s_char):
    count = 0

    for char in line:
        if s_char == char:
            count += 1

    return count

# проверка правильности формулы по схожему алгоритму с формированием польской записи
def is_valid_logic_formula(formula):
    # стек для проверки корректности вложенности скобок
    stack = []

    prev_char = None
    i = 0

    while i < len(formula):
        char = formula[i]

        if char in variables:
            if prev_char in variables or prev_char == ')':
                return False  # Два подряд идущих символа переменных или переменная сразу после закрывающей скобки
            prev_char = char
        elif char == '(':
            if prev_char in variables or prev_char == ')':
                return False  # Открывающая скобка сразу после переменной или закрывающей скобки
            stack.append(char)
            prev_char = char
        elif char == ')':
            if prev_char in operators or prev_char == '(' or prev_char is None:
                return False  # Закрывающая скобка сразу после оператора, открывающей скобки или в начале строки
            if not stack:
                return False  # Закрывающая скобка без открывающей
            stack.pop()
            prev_char = char
        elif char in unary_operators:
            if prev_char in variables or prev_char == ')':
                return False  # Унарный оператор сразу после переменной или закрывающей скобки
            prev_char = char
        elif i + 1 < len(formula) and formula[i:i + 2] in binary_operators:
            if prev_char in operators or prev_char is None or prev_char == '(':
                return False  # Бинарный оператор сразу после другого оператора, в начале строки или после открывающей скобки
            prev_char = formula[i:i + 2]
            i += 1
        elif i + 2 < len(formula) and formula[i:i + 3] == '->':
            if prev_char in operators or prev_char is None or prev_char == '(':
                return False  # Бинарный оператор сразу после другого оператора, в начале строки или после открывающей скобки
            prev_char = '->'
            i += 2
        elif char in operators:
            if prev_char in operators or prev_char is None or prev_char == '(':
                return False  # Бинарный оператор сразу после другого оператора, в начале строки или после открывающей скобки
            prev_char = char
        else:
            return False  # Недопустимый символ

        i += 1

    if stack:
        return False  # Непарные скобки

    return prev_char not in operators and prev_char not in unary_operators

# проверка введенной строки
def check_input(formula: str) -> bool:
    # предварительно проверяем количество скобок, если не совпадает, то не правильно
    count_o = calculate_chars(formula, '(')
    count_c = calculate_chars(formula, ')')

    if count_o != count_c:
        return False
    
    valid_characters = "01ABCDEFGHHIJKLMNOPQRSTUVWXYZ\//\!~->()" 
    for i in formula:
        if valid_characters.find(i) == -1:
            return False
    # Проверяем количество переменных (не больше 16)
    char_count = len(sorted(set(re.findall(r"[A-Za-z]", formula))))

    if char_count > 16:
        print("A lot of variables")
        return False

    # проверяем на коррекность введенной формулы
    if not is_valid_logic_formula(formula):
        return False

    return True  

# построение таблицы истинности
def create_sknf(table: Dict[int, list], variables: list) -> str:
    sknf = '('

    # формируем части СКНФ для тех строк таблицы, в которых значение функции равно 0
    for i in range(len(table)):
        if table[i][LAST] == 0:
            sknf += '('
            for j in range(len(table[i]) - 1):
                if table[i][j] == 0:
                    sknf += f'{variables[j]}\\/'
                else:
                    sknf += f'(!{variables[j]})\\/'
            sknf = sknf[:(LAST-1)]
            sknf += ')/\\'
        else:
            continue
    sknf = sknf[:(LAST - 1)]

    # завершаем построение СКНФ
    if len(sknf) != 0:
        if len(variables) > 1:
            sknf += ")"            # добавляем последнюю скобку в СКНФ
        else:
           sknf = sknf[2:(LAST)]   
    else:
        if len(variables) > 0:
            sknf = f"{variables[0]}"
        else:
            sknf = "не существует"
    return sknf