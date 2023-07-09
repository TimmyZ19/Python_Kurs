# main.py

from chess import check_queens

queens = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 1), (6, 3), (7, 5), (8, 7)]
result = check_queens(queens)
print(result)  # Выводит True, так как ферзи не бьют друг друга
