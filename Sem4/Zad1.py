# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    # Получаем количество строк и столбцов исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с переставленными строками и столбцами
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix

# Пример
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)
