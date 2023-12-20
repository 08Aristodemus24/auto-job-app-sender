import pandas as pd


def view_rows(df: pd.DataFrame, column: str):
    for _, row in df.iterrows():
        print(row[column])