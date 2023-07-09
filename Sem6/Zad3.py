# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import random

def generate_random_arrangements(num_arrangements):
    successful_arrangements = []
    count = 0

    while count < num_arrangements:
        queens = random.sample(range(1, 9), 8)
        if check_queens(queens):
            successful_arrangements.append(queens)
            count += 1

    return successful_arrangements


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                return False

    return True


if __name__ == '__main__':
    num_successful = 4
    successful_arrangements = generate_random_arrangements(num_successful)

    print(f"Первые {num_successful} успешные расстановки:")
    for index, arrangement in enumerate(successful_arrangements, 1):
        print(f"Расстановка {index}:")
        for row in range(1, 9):
            print(f"Ферзь на позиции ({row}, {arrangement[row-1]})")
        print()
