from first_algorithm import calculate_heights
from second_algorithm import calculate_graph_width
from get_graph_data_from_file import file_to_dataframe
from visualization.second_algorithm_visualization import draw_graph


def get_algorithm_and_file_number(algorithm: None, file_number: None):
    print("Введите номер алгоритма, который хотите применить: ")

    while algorithm is None:
        number_of_algorithm = input()
        if not number_of_algorithm.isdigit():
            print("Чтобы выбрать алгоритм введите его номер.")
            continue

        if number_of_algorithm == "":
            print("Выход из программы.")
            break

        if int(number_of_algorithm) == 1:
            algorithm = calculate_heights

        elif int(number_of_algorithm) == 2:
            algorithm = calculate_graph_width
        else:
            print("Алгоритма с таким номером нет, введите существующий.")
            print("Если хотите выйти, нажмите Enter!")

    print("Введите номер графа, на котором хотите увидеть работу алгоритма "
          "(доступные графы можно посмотреть в папке data): ")
    while file_number is None:
        graph_number = input()
        if not graph_number.isdigit():
            print("Чтобы выбрать граф, введите его номер.")
            continue

        if graph_number == "":
            print("Выход из программы.")
            break
        # TODO: add new graph files and change number of graphs here
        if int(graph_number) < 4:
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
    graph = file_to_dataframe(f"../data/graph{file_number}.txt")
    if algorithm == calculate_heights:
        result = calculate_heights(graph)
        print(result)
        # TODO: make visualization for first algorithm
    if algorithm == calculate_graph_width:
        graph, width, matrix_defining_width = calculate_graph_width(graph)
        draw_graph(graph, width, matrix_defining_width)
        # TODO: make it so that result of algorithm and the original graph will saved to folder


if __name__ == '__main__':
    main()
