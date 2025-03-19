from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import pickle
import json

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

def load_file(file_name: str, df_template: pd.DataFrame=None):
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

def load_lookup_array(path: str):
    """
    reads a text file containing a list of all unique values
    and returns this. If no file is found a false boolean is
    returned
    """

    try:
        with open(path, 'r') as file:
            feature_set = file.read()
            feature_set = feature_set.split('\n')
            file.close()

        return feature_set
    except FileNotFoundError as e:
        print("file not found please run needed script first to produce file")
        return False

def save_lookup_array(path: str, uniques: list):
    """
    saves and writes all the unique list of values to a
    a file for later loading by load_lookup_array()
    """
    uniques = [uniques[i] + '\n' for i in range(len(uniques) - 1)] + [uniques[-1]]

    with open(path, 'w') as file:
        file.writelines(uniques)
        file.close()

def save_meta_data(path: str, meta_data: dict):
    """
    saves dictionary of meta data such as hyper 
    parameters to a .json file
    """

    with open(path, 'w') as file:
        json.dump(meta_data, file)
        file.close()

def load_meta_data(path: str):
    """
    loads the saved dictionary of meta data such as
    hyper parameters from the created .json file
    """

    with open(path, 'r') as file:
        meta_data = json.load(file)
        file.close()

    return meta_data

def save_model(model, path: str):
    """
    saves partcularly an sklearn model in a .pkl file
    for later testing
    """

    with open(path, 'wb') as file:
        pickle.dump(model, file)
        file.close()

def load_model(path: str):
    """
    loads the sklearn model, scaler, or encoder stored
    in a .pkl file for later testing and deployment
    """

    with open(path, 'rb') as file:
        model = pickle.load(file)
        file.close()

    return model