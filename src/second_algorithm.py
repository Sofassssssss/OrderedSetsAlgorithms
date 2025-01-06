import networkx as nx
from pandas import DataFrame
from networkx import Graph


def calculate_graph_width(matrix: DataFrame) -> tuple[Graph, int, str]:
    # инициализируем граф
    graph = nx.Graph()

    # добавляем корень графа
    root_name = "M"
    graph.add_node(root_name, label="M", level=0)

    # множество для отслеживания уже обработанных наборов удаленных элементов
    visited_removed_elements = []

    # переменная для отслеживания максимального числа детей(то есть по сути ширины графа),
    # а также матрицы, определяющей ширину графа
    max_children = 0
    matrix_with_max_zero_rows = None

    # рекурсивная функция для построения графа
    def process_node(current_matrix: DataFrame, parent_name: str, removed_elements: str, current_level: int):
        nonlocal max_children, matrix_with_max_zero_rows

        # создаем список с удаленными элементами на данном этапе
        curr_removed_elements = []
        for i in removed_elements:
            curr_removed_elements.append(i)

        # если точно такой же набор элементов уже посещали, не продолжаем ветку
        if any(set(lst) == set(curr_removed_elements) for lst in visited_removed_elements):
            return

        # добавляем набор в посещенные
        visited_removed_elements.append(curr_removed_elements)

        zero_rows = current_matrix[(current_matrix == 0).all(axis=1)].index.tolist()

        # находим ширину(максимальное число детей у узла в графе) и имя узла
        num_children = len(zero_rows)
        if num_children > max_children:
            max_children = num_children
            matrix_with_max_zero_rows = parent_name

        # для каждой нулевой строки создаем дочерний узел
        for element in zero_rows:
            child_matrix = current_matrix.drop(index=element).drop(columns=element)
            new_removed_elements = removed_elements + element
            child_name = f"M_{new_removed_elements}"

            # добавляем ребро в граф
            graph.add_node(child_name, label=child_name, level=current_level + 1)
            graph.add_edge(parent_name, child_name)

            # рекурсивно обрабатываем дочернюю матрицу
            process_node(child_matrix, child_name, new_removed_elements, current_level + 1)

    # запускаем обработку с корня
    process_node(matrix, root_name, "", 0)

    return graph, max_children, matrix_with_max_zero_rows

