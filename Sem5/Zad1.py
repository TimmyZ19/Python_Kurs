# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def split_path(file_path):
    file_dir, file_name = os.path.split(file_path)
    file_name, file_ext = os.path.splitext(file_name)
    return file_dir, file_name, file_ext


# Пример использования функции
file_path = "/python_les/to/file.txt"
directory, filename, extension = split_path(file_path)
print("Директория:", directory)
print("Имя файла:", filename)
print("Расширение файла:", extension)
