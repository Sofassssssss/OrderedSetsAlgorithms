import os

from src.first_algorithm import calculate_heights
from src.second_algorithm import calculate_graph_width
from src.utils.get_graph_data_from_file import file_to_dataframe
from src.visualization.second_algorithm_visualization import save_and_return_graph_with_matrix_node_to_file
from src.visualization.first_algorithm_visualization import save_and_return_drawn_graph_with_heights_to_file, build_graph
from src.utils.packaging_result_to_folder import package_result_to_folder


def get_algorithm_and_file_number(algorithm: None, file_number: None):
    print("Введите номер алгоритма, который хотите применить: ")

    while algorithm is None:
        number_of_algorithm = input()
        if number_of_algorithm == "":
            print("Выход из программы.")
            break

        if not number_of_algorithm.isdigit():
            print("Чтобы выбрать алгоритм введите его номер.")
            continue

        if int(number_of_algorithm) == 1:
            algorithm = calculate_heights

        elif int(number_of_algorithm) == 2:
            algorithm = calculate_graph_width
        else:
            print("Алгоритма с таким номером нет, введите существующий.")
            print("Если хотите выйти, нажмите Enter!")

    print("Введите номер графа, на котором хотите увидеть работу алгоритма "
          "(доступные графы можно посмотреть в папке data/graphs): ")
    while file_number is None:
        graph_number = input()
        if graph_number == "":
            print("Выход из программы.")
            break

        if not graph_number.isdigit():
            print("Чтобы выбрать граф, введите его номер.")
            continue

        lst = os.listdir("data/graphs")
        number_files = len(lst)
        if int(graph_number) < number_files:
            file_number = graph_number
        else:
            print("Файла с таким номером нет, введите существующий.")
            print("Если хотите выйти, нажмите Enter!")
    return algorithm, file_number


def main():
    algorithm = None
    file_number = None
    print("Эта программа предназначена для демонстрации алгоритмов, "
          "связанных с упорядоченными множествами( далее у.м. )\n"
          "Есть 2 доступных алгоритма:\n"
          "1 - Алгоритм нахождения длины элементов у.м.\n"
          "2 - Алгоритм нахождения ширины у.м.")
    algorithm, file_number = get_algorithm_and_file_number(algorithm, file_number)
    if file_number is None:
        return
    graph_matrix = file_to_dataframe(f"data/graphs_data/graph{file_number}.txt")
    if algorithm == calculate_heights:
        result_heights = calculate_heights(graph_matrix)
        graph, pos = build_graph(graph_matrix, result_heights)
        result_file_path = save_and_return_drawn_graph_with_heights_to_file(graph, pos, result_heights)
    if algorithm == calculate_graph_width:
        graph_matrix, width, matrix_defining_width = calculate_graph_width(graph_matrix)
        result_file_path = save_and_return_graph_with_matrix_node_to_file(graph_matrix, width, matrix_defining_width)
    package_result_to_folder(f"data/graphs/graph{file_number}.png", result_file_path)


if __name__ == '__main__':
    main()
