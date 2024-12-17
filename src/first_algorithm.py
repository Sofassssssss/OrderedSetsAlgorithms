import numpy as np
from pandas import DataFrame
# from get_graph_data_from_file import file_to_dataframe

def calculate_heights(M: DataFrame) -> dict:
    # проверка исключений
    if set(M.index) != set(M.columns):
        mismatch = set(M.index).symmetric_difference(set(M.columns))
        raise ValueError(f"Ошибка: Несоответствие индексов и столбцов. Проблемные элементы: {mismatch}")

    if M.shape[0] != M.shape[1]:
        raise ValueError("Ошибка: Матрица должна быть квадратной")

    #алгоритм
    M = M.copy()
    M['Height'] = np.nan
    heights = {}

    # шаг индукции: пока есть строки в матрице
    current_height = 0
    while not M.drop(columns=['Height']).empty:
        zero_rows = M.drop(columns=['Height']).sum(axis=1) == 0
        for idx in M[zero_rows].index:
            heights[idx] = current_height
        current_height += 1

        columns_to_drop = M[zero_rows].index
        M = M.drop(index=columns_to_drop, columns=columns_to_drop, errors='ignore')
    return heights
