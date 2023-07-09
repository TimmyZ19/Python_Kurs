# Дорабатываем функции из предыдущих задач.
# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import shutil


def sort_files_by_category(source_directory):
    # Создаем список категорий и соответствующих расширений файлов
    categories = {
        'videos': ['.mp4', '.avi', '.mov'],
        'images': ['.jpg', '.png', '.gif'],
        'documents': ['.txt', '.docx', '.pdf'],
        # добавьте другие категории и соответствующие расширения
    }

    # Проверяем существование и доступность исходной директории
    if not os.path.exists(source_directory):
        print(f"Исходная директория '{source_directory}' не существует.")
        return
    if not os.path.isdir(source_directory):
        print(f"Путь '{source_directory}' не является директорией.")
        return

    # Создаем целевую директорию для категорий файлов
    destination_directory = 'sorted_files'
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Получаем список всех файлов в исходной директории
    file_names = os.listdir(source_directory)

    # Перебираем каждый файл и перемещаем его в соответствующую категорию
    for file_name in file_names:
        file_extension = os.path.splitext(file_name)[1].lower()  # получаем расширение файла
        moved = False  # флаг для отслеживания перемещения файла

        # Перебираем каждую категорию и проверяем, соответствует ли расширение файла
        for category, extensions in categories.items():
            if file_extension in extensions:
                category_directory = os.path.join(destination_directory, category)

                # Создаем директорию категории, если она не существует
                if not os.path.exists(category_directory):
                    os.makedirs(category_directory)

                source_path = os.path.join(source_directory, file_name)
                destination_path = os.path.join(category_directory, file_name)

                # Перемещаем файл в соответствующую категорию
                shutil.move(source_path, destination_path)
                print(f"Файл '{file_name}' перемещен в категорию '{category}'.")
                moved = True
                break

        # Если файл не подходит для сортировки, оставляем его в исходной директории
        if not moved:
            print(f"Файл '{file_name}' не подходит для сортировки. Оставлен в исходной директории.")

    print("Сортировка файлов завершена.")


# Пример использования
source_directory = 'generated_files'
sort_files_by_category(source_directory)
