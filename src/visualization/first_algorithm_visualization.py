from pandas import DataFrame
import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph
from collections import defaultdict


def sort_matrix_by_elements_heights(unsorted_matrix: DataFrame, elements_heights: dict[str, int]) -> DataFrame:
    # добавляем колонку высот для сортировки
    unsorted_matrix["height"] = unsorted_matrix.index.map(elements_heights)

    # сортируем DataFrame по высоте
    sorted_matrix = unsorted_matrix.sort_values(by="height", ascending=False).drop(columns=["height"])

    return sorted_matrix


def correct_position_of_graph_nodes(heights: dict[str, int]) -> dict[str, tuple]:
    # позиции для узлов графа
    pos = {}

    # сортировка высот по убыванию для установки позиций по оси Y
    sorted_heights = sorted(set(heights.values()), reverse=True)

    # присваиваем Y-позиции на основе высоты
    y_pos = {height: idx * 2 for idx, height in enumerate(sorted_heights)}

    # присваиваем элементы их Y-позиции на основе их высоты
    for element, height in heights.items():
        pos[element] = (0, -y_pos[height])

    # чтобы избежать наложений, будем двигать элементы по оси X
    x_offset = 0
    for level in sorted_heights:
        x_pos = x_offset
        for element in sorted([e for e in heights if heights[e] == level]):
            pos[element] = (x_pos, pos[element][1])
            x_pos += 6
        x_offset += 2

    return pos


def build_graph(matrix: DataFrame, heights: dict[str, int]) -> [Graph, dict]:
    graph = nx.Graph()

    sorted_matrix = sort_matrix_by_elements_heights(matrix, heights)

    # словарь для хранения детей каждого элемента
    children_dict = {}

    # идем по строкам матрицы снизу вверх
    for element, row in sorted_matrix.iloc[::-1].iterrows():
        # инициализируем множество детей
        connect_set = {k for k, v in row.items() if v == 1}

        # получаем детей из словаря тех элементов, с которыми связан текущий
        connect_set_children = set()
        for child in connect_set:
            connect_set_children.update(children_dict.get(child, set()))

        # определяем текущих детей
        current_children = connect_set - connect_set_children

        # добавляем элемент и его детей в граф
        for child in current_children:
            graph.add_edge(element, child)

        # обновляем словарь детей
        children_dict[element] = current_children

    pos = correct_position_of_graph_nodes(heights)

    # добавляем высоты элементов как атрибуты узлов
    for node, height in heights.items():
        graph.nodes[node]['height'] = height

    return graph, pos


def save_and_return_drawn_graph_with_heights_to_file(graph: Graph, pos: dict, heights:dict[str, int]) -> str:
    result_filename = 'result.png'

    # рисуем граф
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='pink', font_size=10, font_weight='bold', alpha=0.8)

    # рисуем высоты узлов рядом с ними
    labels = {node: f"{node} ({data['height']})" for node, data in graph.nodes(data=True)}
    nx.draw_networkx_labels(graph, pos, labels, font_size=10, bbox=dict(facecolor='pink', edgecolor='none', boxstyle='round,pad=0.2'))
    plt.text(1, 0, f'Длина упорядоченного множества равна {max(heights.values())}',
             fontsize=16, ha='right', va='top', color='black',
             transform=plt.gca().transAxes)
    plt.savefig(result_filename, dpi=300, bbox_inches='tight')
    plt.figure(figsize=(40, 40))
    plt.tight_layout()

    return result_filename
