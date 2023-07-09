import random

def append_random_pairs(num_lines, file_name):
    with open(file_name, 'a') as file:
        for _ in range(num_lines):
            first_num = random.randint(-1000, 1000)
            second_num = random.uniform(-1000, 1000)
            file.write(f"{first_num}|{second_num}\n")

# Пример использования
num_lines = 10
file_name = "random_pairs.txt"
append_random_pairs(num_lines, file_name)
