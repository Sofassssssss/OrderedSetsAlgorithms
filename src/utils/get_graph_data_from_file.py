import pandas as pd
from pandas import DataFrame


def file_to_dataframe(file_path: str) -> DataFrame:
    try:
        df = pd.read_csv(file_path, sep=r'\s+', index_col=0)
        if df.empty:
            raise ValueError("Ошибка: Файл пустой или не содержит данных, пригодных для загрузки.")
        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл по пути '{file_path}' не найден")
    except pd.errors.EmptyDataError:
        raise ValueError("Ошибка: Файл пустой")
    except Exception as e:
        raise ValueError(f"Ошибка при загрузке файла: {e}")