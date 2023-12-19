import re
import requests

def preprocess(name: str):
    """
    preprocesses name in the profiles dataframe to remove uneccessary
    strings like CRSP, CHRA, RPm, non-alphanumeric characters, middle initials
    e.g. R., D.C., capitalizes first names middle names and last names,
    """

    # # remove quotation marks
    # temp = rem_quotes(name)

    # remove other non-alpha numeric chars
    temp = rem_nonalphanum(temp)
    print(temp)

    # partition full profile name
    temp = partition_full_name(temp)

    return temp

def is_valid_name(name: str):
    """
    a function that returns a boolean to tell
    whether name is valid or not
    """

    pass

def partition_full_name(name: str):
    """
    splits full linked in profile name into individual strings
    """

    return name.split()

def rem_quotes(name: str):
    return name.strip('"')

def rem_nonalphanum(name: str):
    return re.sub(r"[^0-9a-zA-Z.\"]+", '', name)

def rem_mi(name: str):
    pass

def capitalize(name: str):
    return name.capitalize()


def assign_gender(name: str):
    pass