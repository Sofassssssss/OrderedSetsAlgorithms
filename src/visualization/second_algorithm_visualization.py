import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph


def hierarchical_layout(graph: Graph) -> dict:
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


def save_and_return_graph_with_matrix_node_to_file(graph: Graph, width: int, matrix_with_max_zero_rows: str) -> str:
    result_filename = "result.png"
    plt.figure(figsize=(15, 20))
    pos = hierarchical_layout(graph)
    nx.draw(graph, pos, with_labels=False, node_color='pink', edge_color='gray', font_size=10, node_size=3000)
    nx.draw_networkx_labels(graph, pos, labels=nx.get_node_attributes(graph, 'label'))
    plt.text(1, 1, f'Ширина графа равна {width}, её определяет матрица {matrix_with_max_zero_rows}',
             fontsize=24, ha='right', va='top', color='black',
             transform=plt.gca().transAxes)
    plt.savefig(result_filename, dpi=300, bbox_inches='tight')
    return result_filename
