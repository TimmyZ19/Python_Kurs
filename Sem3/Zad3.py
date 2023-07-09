# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import itertools

def find_items(items, max_capacity):
    all_combinations = []
    for r in range(1, len(items) + 1):
        combinations = itertools.combinations(items, r)
        for combination in combinations:
            if sum_weights(combination) <= max_capacity:
                all_combinations.append(combination)
    return all_combinations

def sum_weights(items):
    return sum([weight for _, weight in items])

# Пример использования
items = [
    ("Тент", 2),
    ("Спальник", 1),
    ("Палатка", 4),
    ("Котелок", 1),
    ("Фонарик", 0.5),
    ("Ложка", 0.2),
    ("Спички", 0.1)
]

max_capacity = 5
result = find_items(items, max_capacity)
for combination in result:
    print(combination)
