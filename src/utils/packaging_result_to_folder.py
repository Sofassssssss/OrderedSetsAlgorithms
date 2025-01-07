import os
import shutil


def package_result_to_folder(source_graph_file_path: str, result_file_path: str):
    folder_path = 'result'

    os.makedirs(folder_path, exist_ok=True)  # exist_ok=True не вызовет ошибку, если папка уже существует

    # путь для перемещенных файлов
    new_path_for_source_file = os.path.join(folder_path, os.path.basename(source_graph_file_path))
    new_path_for_result = os.path.join(folder_path, os.path.basename(result_file_path))
    files_paths = [new_path_for_source_file, new_path_for_result]

    if os.listdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)

    shutil.copy(source_graph_file_path, new_path_for_source_file)
    shutil.move(result_file_path, new_path_for_result)
    print("Исходный граф и результат алгоритма сохранены в папку result.")
