import re
import requests
import numpy as np
import pandas as pd

def preprocess(name: str):
    """
    preprocesses name in the profiles dataframe to remove uneccessary
    strings like CRSP, CHRA, RPm, non-alphanumeric characters, middle initials
    e.g. R., D.C., capitalizes first names middle names and last names,
    """
    temp = name

    # remove other non-alpha numeric chars
    temp = rem_nonalphanum(temp)
    # print(temp)

    # capitalize all strings in profile name
    temp = capitalize(temp)

    # partition full profile name
    temp = partition_full_name(temp)

    # remove all invalid words in partitioned profile names
    temp = filter_valid(temp)
    print(temp)

    return temp

def rem_nonalphanum(name: str):
    return re.sub(r"[^0-9a-zA-ZñÑ.\"]+", ' ', name)

def capitalize(name: str):
    return name.title()

def partition_full_name(name: str):
    """
    splits full linked in profile name into individual strings
    """

    return name.split()

def filter_valid(sequence: list):
    """
    a function that filters only valid names and
    joins only the words that is valid in the profile
    name e.g. ['Christian', 'Cachola', 'Chrp', 'Crsp']
    results only in Christian Cachola
    """

    # filter and remove the words in the sequence
    # included in list of words that are invalid
    filt_sequence = list(filter(lambda word: word not in [
        'Crsp', 
        'Rpm', 
        'Mapsy', 
        'Cssgb',
        'Chra',
        'Mba',
        'Es',
        'Csswb',
        'Cphr',
        'Clssyb',
        'Cssyb',
        'Mdrt',
        'Ceqp',
        'Msp',
        'Chrp'
        'Icyb'], sequence))
    
    # join the filtered words
    temp = " ".join(filt_sequence)

    return temp

def rem_mi(name: str):
    pass

def assign_gender(row, api_key):
    # extract gender if any
    gender = row['gender']
    print(gender)

    # check if null
    if pd.isnull(gender):
        name = row['conn_name']
        response = requests.post(f"https://genderapi.io/api/?key={api_key}&name={name}")
        headers = response.headers
        data = response.json()
        print(data)
        print(headers)

        # if request gives a request limit reached error
        # thus returning a json without hte gender key, just
        # use an alternative return value of the null value 
        # of the empty cell
        return data.get('gender', gender)
    else:
        return row['gender']
