import pandas as pd
from pandas import DataFrame


def file_to_dataframe(file_path: str) -> DataFrame:
    df = pd.read_csv(file_path, sep=r'\s+', index_col=0)
    return df
