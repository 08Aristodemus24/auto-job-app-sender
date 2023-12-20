from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def element_exists(driver: webdriver.Chrome, css_path: str,):
    """
    should .find_element() raise a NoSuchElement or StaleElementReference
    exception return false because the element being searched does not exist
    """
    try:
        driver.find_element(By.CSS_SELECTOR, css_path)
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