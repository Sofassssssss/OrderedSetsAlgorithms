import networkx as nx
import matplotlib.pyplot as plt
from networkx import DiGraph


def hierarchical_layout(graph: DiGraph) -> dict:
    """
    Создает иерархическую раскладку графа сверху вниз.
    """
    # получаем уровни узлов
    levels = nx.get_node_attributes(graph, 'level')

    # устанавливаем уровень как атрибут subset для каждого узла
    for node, level in levels.items():
        graph.nodes[node]['subset'] = level

    # используем multipartite_layout для расположения узлов
    pos = nx.multipartite_layout(graph, subset_key="subset")

    # преобразуем раскладку для вертикального отображения
    for node in pos:
        x, y = pos[node]
        pos[node] = (y, -x)

    return pos


def draw_graph(graph: DiGraph, width: int, matrix_with_max_zero_rows: str):
    plt.figure(figsize=(15, 20))
    pos = hierarchical_layout(graph)
    nx.draw(graph, pos, with_labels=False, node_color='pink', edge_color='gray', font_size=10, node_size=3000)
    nx.draw_networkx_labels(graph, pos, labels=nx.get_node_attributes(graph, 'label'))
    plt.text(1, 1, f'Ширина графа равна {width}, её определяет матрица {matrix_with_max_zero_rows}',
             fontsize=24, ha='right', va='top', color='black',
             transform=plt.gca().transAxes)
    plt.show()
