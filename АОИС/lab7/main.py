from Matrix import Matrix
from utils import *
import random


def main():
    memory = Matrix()
    V = [1, 0, 0]
    random.seed()
    for i in range(16):
        binary_word = bin(random.randint(0, 65535))[2:].zfill(16)
        word = [int(bit) for bit in binary_word]
        memory.write(word, i)
    print("Matrix:")
    print_matrix(memory.get_diagonal_matrix(memory.get_normal_matrix()))
    print("For example, 11th word of the matrix:", end=" ")
    print_list(memory.read(11))
    print()
    print(21 * "_" + "Logical operations" + 21 * "_")
    print("Matrix before logical operations:")
    print_matrix(memory.get_diagonal_matrix(memory.get_normal_matrix()))
    print("Function #4 (Takes 0 and 1 rows, writes to 2):")
    print_list(memory.function_4(0, 1, 2))
    print("Function #6 (Takes 3 and 4 rows, writes to 5):")
    print_list(memory.function_6(3, 4, 5))
    print("Function #9 (Takes 6 and 7 rows, writes to 8):")
    print_list(memory.function_9(6, 7, 8))
    print("Function #11 (Takes 9 and 10 rows, writes to 11):")
    print_list(memory.function_11(9, 10, 11))
    print("Matrix after logical operations:")
    print_matrix(memory.get_diagonal_matrix(memory.get_normal_matrix()))
    print()
    print(27 * "_" + "Sorting" + 27 * "_")
    memory.sort()
    print_matrix(memory.get_diagonal_matrix(memory.get_normal_matrix()))
    print()
    print(19 * "_" + "Arithmetic operations" + 19 * "_")
    print("Matrix before arithmetic operations:")
    print_matrix(memory.get_diagonal_matrix(memory.get_normal_matrix()))
    memory.sum(V)
    print("Matrix after arithmetic operations:")
    print_matrix(memory.get_diagonal_matrix(memory.get_normal_matrix()))
    print(f"Diagonal matrix after arithmetic operations:")
    print(memory)
    print()


if __name__ == "__main__":
    main()
