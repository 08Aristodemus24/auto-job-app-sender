from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pandas as pd
import numpy as np

def element_exists(driver: webdriver.Chrome, by, path:str):
    """
    should .find_element() raise a NoSuchElement or StaleElementReference
    exception return false because the element being searched does not exist
    """
    try:
        driver.find_element(by, path)
    except:
        return False
    return True


def click_until_permitted(driver: webdriver.Chrome, css_path: str, num_tries: int=50):
    """
    clicks an element over and over if it is stale

    if click is successful function will return true 
    """
    while num_tries > 0:

        try:
            """THIS DOESN"T WORK BECAUSE EVEN IF THE ELEMTN EXISTS THE FACT THAT IT IS DYNAMIC
            WILL MAKES IT STALE AND THEREFORE CLICKING ON IT WILL RAISE A STALE ELEMENT REFERENCE
            ERROR"""
            load_more_btn = driver.find_element(By.CSS_SELECTOR, css_path)
            load_more_btn.click()
            return True
        except (StaleElementReferenceException, NoSuchElementException) as e:
            print(f'error {e} has occured')
            num_tries -= 1
    
    # if after num_tries the function has not returned true then
    # return a false flag
    return False

def augment_df(df: pd.DataFrame, path: str):
    """
    loads and/or creates a .csv file if one does not already exist
    """
    # create new dataframe template of n_rows from profile.csv
    # dataframe
    n_rows_dump = df.shape[0]

    try:
        temp = pd.read_csv(path, index_col=0)
        n_rows_temp = temp.shape[0]
        template = pd.DataFrame({
            'email': [""] * (n_rows_dump - n_rows_temp),
            'mobile_no': [0] * (n_rows_dump - n_rows_temp),
            'company_name': [""] * (n_rows_dump - n_rows_temp),
            'conn_link': [""] * (n_rows_dump - n_rows_temp), 
            'conn_name': [""] * (n_rows_dump - n_rows_temp), 
            'gender': [""] * (n_rows_dump - n_rows_temp), 
            'salutation': [""] * (n_rows_dump - n_rows_temp), 
        })
        temp = pd.concat([temp, template], axis=0)
        temp.reset_index(drop=True, inplace=True)
        temp.to_csv(path)

        return temp

    except FileNotFoundError as e:
        # if no file has been found creawte a new dataframe and return it
        # in order to be populated by the connection information extractor
        print(f'{e} has occured. Creating a new dataframe...')

        
        template = pd.DataFrame({
            'email': [""] * n_rows_dump, 
            'mobile_no': [0] * n_rows_dump, 
            'company_name': [""] * n_rows_dump,
            'conn_link': [""] * n_rows_dump, 
            'conn_name': [""] * n_rows_dump, 
            'gender': [""] * n_rows_dump, 
            'salutation': [""] * n_rows_dump, 
        })
        template.to_csv(path)

        return template

    