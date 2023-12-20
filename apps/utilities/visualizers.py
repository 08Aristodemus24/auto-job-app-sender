import pandas as pd


def view_rows(df: pd.DataFrame):
    for _, row in df.iterrows():
        print(row['conn_name'])