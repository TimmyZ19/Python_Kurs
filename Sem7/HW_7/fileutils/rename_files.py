import os


def batch_rename_files(directory, target_name, source_extension, target_extension):
    # Проверяем существование и доступность директории
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не существует.")
        return
    if not os.path.isdir(directory):
        print(f"Путь '{directory}' не является директорией.")
        return

    # Получаем список файлов в директории
    file_names = os.listdir(directory)

    # Перебираем каждый файл
    for index, file_name in enumerate(file_names):
        # Проверяем расширение файла
        if file_name.endswith(source_extension):
            # Формируем новое имя файла с порядковым номером
            new_file_name = f"{target_name}{index + 1}.{target_extension}"

            # Полные пути к исходному и конечному файлам
            source_path = os.path.join(directory, file_name)
            target_path = os.path.join(directory, new_file_name)

            # Переименовываем файл
            os.rename(source_path, target_path)
            print(f"Файл '{file_name}' переименован в '{new_file_name}'.")

    print("Групповое переименование файлов завершено.")


# # Пример использования
# directory = "images"
# target_name = "photo_"
# source_extension = ".jpg"
# target_extension = "png"
# batch_rename_files(directory, target_name, source_extension, target_extension)
