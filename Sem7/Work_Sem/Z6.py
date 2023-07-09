import os
import random
import string


def create_files_with_extension(extension, directory, min_name_length=6, max_name_length=30,
                               min_file_size=256, max_file_size=4096, num_files=42):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_size = random.randint(min_file_size, max_file_size)

        name = ''.join(random.choices(string.ascii_lowercase, k=name_length))
        file_name = f"{name}.{extension}"
        file_path = os.path.join(directory, file_name)

        if os.path.exists(file_path):
            continue

        with open(file_path, 'wb') as file:
            random_bytes = os.urandom(file_size)
            file.write(random_bytes)


def create_files_with_multiple_extensions(extensions, num_files_per_extension, directory, min_name_length=6,
                                          max_name_length=30, min_file_size=256, max_file_size=4096):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for extension, num_files in zip(extensions, num_files_per_extension):
        create_files_with_extension(extension, directory, min_name_length, max_name_length,
                                    min_file_size, max_file_size, num_files)


# Пример использования
extensions = ['txt', 'csv', 'jpg']
num_files_per_extension = [10, 5, 8]
directory = 'generated_files'
create_files_with_multiple_extensions(extensions, num_files_per_extension, directory)
