from utils import *

SIZE = 16


class Matrix:
    def __init__(self):
        self.memory = [[False for _ in range(SIZE)] for _ in range(SIZE)]

    def __str__(self):
        result = ""
        for i in range(SIZE):
            for j in range(SIZE):
                result += str(int(self.memory[i][j])) + " "
            result += "\n"
        return result

    def write(self, word, address):  #запись слова по адресу
        for i in range(address, SIZE):
            self.memory[i][address] = word[i - address]
        for j in range(0, address):
            self.memory[j][address] = word[SIZE - address + j]

    def read(self, address):         #чтение слова по адресу
        word = []
        for i in range(address, SIZE):
            word.append(self.memory[i][address])
        for i in range(0, address):
            word.append(self.memory[i][address])
        return word

    def get_normal_matrix(self):
        return [self.read(i) for i in range(SIZE)]

    def get_diagonal_matrix(self, matrix):
        for i in range(len(matrix)):
            self.write(matrix[i], i)
        return self.memory

    @staticmethod
    def binary_addition(A, B):   #сложение двоичное для третьего пункта
        ostatok = False
        S = []
        for i in range(3, -1, -1):
            a = A[i]
            b = B[i]
            temp_sum = a ^ b ^ ostatok
            S.insert(0, temp_sum)
            ostatok = (a & ostatok) | (b & ostatok) | (a & b)
        S.insert(0, ostatok)
        return S

    def sum(self, V):       # всё то же сложение, но обертка
        for i in range(SIZE):
            current_word = self.read(i)
            Vj = current_word[:3]
            if Vj == V:
                print(f"Vj = V in word {i}: {V}")
                print("Original word:  ", end="")
                print_list(current_word)
                Aj = current_word[3:7]
                Bj = current_word[7:11]
                Sj = self.binary_addition(Aj, Bj)
                current_word[11:] = Sj
                print("Changed word:   ", end="")
                print_list(current_word)
                self.write(current_word, i)

    def function_4(self, address_1, address_2, address_3):   # F4 = (!x1*x2)
        word_1 = self.read(address_1)
        word_2 = self.read(address_2)
        print_list(word_1)
        print_list(word_2)
        result_word = [not word_1[i] and word_2[i] for i in range(SIZE)]
        self.write(result_word, address_3)
        return result_word

    def function_6(self, address_1, address_2, address_3):   # F6 = (!x1*x2)+(x1*!x2)
        word_1 = self.read(address_1)
        word_2 = self.read(address_2)
        print_list(word_1)
        print_list(word_2)
        result_word = [(not word_1[i] and word_2[i]) or (word_1[i] and not word_2[i]) for i in range(SIZE)]
        self.write(result_word, address_3)
        return result_word

    def function_9(self, address_1, address_2, address_3):  # F9 = (x1*x2)+(!x1*!x2)
        word_1 = self.read(address_1)
        word_2 = self.read(address_2)
        print_list(word_1)
        print_list(word_2)
        result_word = [(word_1[i] and word_2[i]) or (not word_1[i] and not word_2[i]) for i in range(SIZE)]
        self.write(result_word, address_3)
        return result_word

    def function_11(self, address_1, address_2, address_3):  # F11 = (x1+!x2)
        word_1 = self.read(address_1)
        word_2 = self.read(address_2)
        print_list(word_1)
        print_list(word_2)
        result_word = [word_1[i] or not word_2[i] for i in range(SIZE)]
        self.write(result_word, address_3)
        return result_word

    def sort(self, reverse=False):    # обертка сортировки и перестановка элементов местами
        for i in range(SIZE):
            for j in range(i+1, SIZE):
                word_i = self.read(i)
                word_j = self.read(j)
                comparison_result = self.comparison(word_j, word_i, SIZE - 1)["g"]
                if (not reverse and comparison_result) or (reverse and not comparison_result):
                    self.write(word_j, i)
                    self.write(word_i, j)

    @staticmethod
    def comparison(word1, word2, i):   # логика сортировки слов по нарастанию
        result = {}
        previous_result = {}
        if i == 0:
            previous_result["g"] = False
            previous_result["l"] = False
        else:
            previous_result = Matrix.comparison(word1, word2, i - 1)

        if previous_result["g"] or (word1[i] == 0 and word2[i] == 1 and not previous_result["l"]):
            result["g"] = True
        else:
            result["g"] = False

        if previous_result["l"] or (word1[i] == 1 and word2[i] == 0 and not previous_result["g"]):
            result["l"] = True
        else:
            result["l"] = False

        return result
