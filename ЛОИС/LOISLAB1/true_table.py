"""
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнили Демидовец Д.В., Тагиева П.К.
Дата выполнения 25.05.2024

Файл с реализацией ключевых методов для построения таблиц истинности
"""

from constant import *
from typing import List
import re


# преобразование логической формулы в обратную польскую запись 
def reversed_polish_notation(formula: str) -> str:
    result = []
    stack = []
    operation_signs = ["\\", "!", "/", "~", ">", "(", ")"]
    
    # для упрощения алгоритма заменяем символы дизьюнкции и коньюнции на равнозначные им символы
    formula = formula.replace("/\\", "/")
    formula = formula.replace("\\/", "\\")

    # формируем формулу с помощью стека операций по их приоритету
    for element in formula:
        if element == "-":
            continue

        if element != " ":
            if element == "(":
                stack = [element] + stack
            elif element in operation_signs:
                if not stack:
                    stack = [element]
                else:
                    iconic_element(stack, element, result)
            else:
                result += [element]

    # освобождаем оставшиеся операции из стека в формулу 
    while stack:
        first_el = stack[0]
        result += [first_el]
        stack = stack[1:]
    polish_notation = "".join(result)
 
    return polish_notation

# добавление операций в стек по приоритету либо освобождение, если текущий элемент ")"
def iconic_element(stack, element, result):
    if element == ")":
        while True:
            first_el = stack[0]
            stack.pop(0)

            if first_el == "(":
                break
            result += [first_el]
    elif priority_search(stack[0]) < priority_search(element):
        stack.insert(0, element)
    else:
        while True:
            if not stack:
                break
            first_el = stack[0]
            result += [first_el]
            stack.pop(0)
            if priority_search(first_el) == priority_search(element):
                break
        stack.insert(0, element)

# получение приоритета операции
def priority_search(value: str) -> int:
    for key, v in PRIORITY.items():
        if value in v:
            return key
    return -1

# формирование таблицы истинности
def true_table(formula: str, can_print: bool = True) -> (dict, List): # type: ignore
    formula = reversed_polish_notation(formula)
    # формируем массив переменных формулы
    variables = sorted(set(re.findall(r"[A-Za-z]", formula)))

    # строим таблицу истинности 
    table = {}
    for i in range(pow(2, len(variables))):
        table[i] = list()
    result = ZERO
    for i in range(len(table)):
        table[i].extend(result[-len(variables):])
        table[i].append(find_result((table[i]), formula))
        result = interval(result, ONE)

    return table, variables

# получение результата для текущего набора значений строки переменных таблицы истинности в зависимости от операций в формуле
def find_result(table: List, formula: str) -> int:
    index = 0

    # заменяем переменные на текущий набор значений строки таблицы истинности
    for char in abc:
        if char in formula:
            formula = formula.replace(char, str(table[index]))
            index += 1

    result = []
    for i in formula:
        if i.isdigit():
            result.append(i)
        elif i == '\\': # Дизъюнкция
            last_el, pre_last_el = result.pop(), result.pop()
            if int(last_el) or int(pre_last_el):
                result.append(1)
            else:
                result.append(0)
        elif i == '/': # Конъюнкция
            last_el, pre_last_el = result.pop(), result.pop()
            if int(last_el) and int(pre_last_el):
                result.append(1)
            else:
                result.append(0)
        elif i == '!': # Отрицание
            last_el = result.pop()
            if int(last_el):
                result.append(0)
            else:
                result.append(1)
        elif i == '>': # Импликация
            last_el, pre_last_el = result.pop(), result.pop()
            if not int(last_el) or int(pre_last_el):
                if int(last_el) != int(pre_last_el):
                    result.append(0)
                else:
                    result.append(1)
            elif int(last_el) or not int(pre_last_el):
                if int(last_el) != int(pre_last_el):
                    result.append(1)
                else:
                    result.append(0)
        elif i == '~': # Эквиваленция
            last_el, pre_last_el = result.pop(), result.pop()
            if int(last_el) == int(pre_last_el):
                result.append(1)
            else:
                result.append(0)
    return result.pop()

# формирование текущего набора значений переменных таблицы истиности, путем добавления единицы к предыдущему набору
def interval(first_el: List[int], second_el: List[int]) -> List[int]:
    result = list()
    count = 0
    for i in range(len(first_el) - 1, -1, -1):
        if int(first_el[i]) + int(second_el[i]) + count == 3:
            result.insert(0, 1)
            count = 1
        elif int(first_el[i]) + int(second_el[i]) + count == 2:
            result.insert(0, 0)
            count = 1
        elif int(first_el[i]) + int(second_el[i]) + count == 1:
            result.insert(0, 1)
            count = 0
        else:
            result.insert(0, 0)
            count = 0
    if count == 1:
        result.insert(0, 1)
    return result