from concurrent.futures import ThreadPoolExecutor
import pandas as pd

def load_excluded(file_path: str):
    """
    returns a list of names from a text file of a list of names
    to exclude in email search
    """
    with open(file_path, 'r') as names_file:
        names = names_file.readline()
        names_file.close()

    with ThreadPoolExecutor() as executor:
        names = list(executor.map(lambda name: name.lower(), names))

    return names

def load_file(file_name: str, df_template: pd.DataFrame):
    """
    loads and/or creates a .csv file if one does not already exist
    """

    try:
        dump = pd.read_csv(file_name, index_col=0)
    except FileNotFoundError as e:
        # if no file has been found creawte a new dataframe and return it
        # in order to be populated by the connection information extractor
        print(f'{e} has occured. Creating a new dataframe...')
        dump = df_template

    return dump