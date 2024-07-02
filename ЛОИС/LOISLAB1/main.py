"""
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнили Демидовец Д.В., Тагиева П.К.
Дата выполнения 25.05.2024

Основной файл для запуска программы
"""

from general import *
from true_table import *
import time

def main():
    while True:
        # вводим формулу
        formula=input("Введите формулу(максимум 16 переменных): ")

        # проверяем формулу на корректность
        while not check_input(formula):
            print("Неправильный ввод, попробуйте снова")
            print("_" * 60)
            formula=input("\nВведите формулу(максимум 16 переменных): ")

        start = time.time()

        # выводим результат
        table, variables = true_table(formula)
        print("\nПолученная СКНФ: " + create_sknf(table, variables))

        end = time.time() - start
        print("Время выполнения: " + str(end) + "с\n")

        print("_" * 60)


if __name__ == "__main__":
    main()


# для тестов
# (((((((((((((((A\/B)\/C)\/D)\/E)\/F)\/G)\/H)\/I)\/J)\/K)\/L)\/M)\/N)\/O)\/P)
# ((A\/B)/\C)
# (D~(V->E))
# ((A/\(B\/C))->(D\/(!E)))