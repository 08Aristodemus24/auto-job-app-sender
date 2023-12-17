from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

import re
import time
import os
from dotenv import load_dotenv
from pathlib import Path



def collect_recruiter_info(driver: webdriver.Chrome, links: list[str]):
    """
    the links contain links to all recruiter profiles pages
    collected by beautiful soup statemetns
    """

    for link in links:
        try:
            driver.get(link)
            _ = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

            # programmatically scroll to see experience section
            driver.execute_script("""
                window.location.hash = "experience"
            """)

        except TimeoutError as error:
            print("Error {} has occured".format(error))
            driver.quit() # or .close()

        # catch both NoSuchElementException and StaleElementReferenceException errors
        except (NoSuchElementException, StaleElementReferenceException) as error:
            print("Error {} has occured".format(error))

        finally:
            print("will go to next link")

def element_exists(driver: webdriver.Chrome, css_path: str, ):
    """
    should .find_element() raise a NoSuchElement or StaleElementReference
    exception return false because the element being searched does not exist
    """
    try:
        driver.find_element(By.CSS_SELECTOR, css_path)
    except:
        return False
    return True


def click_until_permitted(driver: webdriver.Chrome):
    """
    clicks an element over and over if it is stale
    """

    pass


def extract_con_links(driver: webdriver.Chrome | webdriver.Edge, lookup_file: pd.DataFrame):
    """
    because of pages infinite scroll capability we need to scroll 
    at the very bottom of the page until connection list is exhausted

    if .csv already exists extract dataframe info and add only the ones not in the
    dataframe that have been scraped 
    """

    # will store all non existent connections for concatenation to
    # new or existing dataframe lookup_file
    conn_links = []
    conn_names = []

    try:
        # login first
        driver.get("https://www.linkedin.com/uas/login/")

        # wait until the document is loaded
        _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

        # get parent window
        parent_window = driver.current_window_handle

        # click sign in with google
        time.sleep(5)
        gsign_in_btn = driver.find_element(By.CSS_SELECTOR, ".alternate-signin__btn--google")
        gsign_in_btn.click()
        time.sleep(5)

        # get all windows currently open
        windows = driver.window_handles
        driver.switch_to.window(windows[1])

        # select the username input in popup authentication window of google
        username = driver.find_element(By.CSS_SELECTOR, "input[type='email'].whsOnd")
        username.send_keys(os.environ['GOOGLE_EMAIL'])
        username.send_keys(Keys.ENTER)
        time.sleep(5)

        # select the password input in popup authentication window of google
        password = driver.find_element(By.CSS_SELECTOR, "input[type='password'].whsOnd")
        password.send_keys(os.environ['GOOGLE_PASS'])
        password.send_keys(Keys.ENTER)
        
        # switch again to current window
        driver.switch_to.window(parent_window)
        time.sleep(5)

        # go to new link where connections live
        driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
        time.sleep(5)

        # scroll to the very bottom until there is none left to scroll
        n_connections_header = driver.find_element(By.CSS_SELECTOR, "header.mn-connections__header")
        n_connections = int(re.findall(r"\d+", n_connections_header.text)[0])

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(1.5)
        for _ in range(n_connections // 10):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
            time.sleep(1.5)

            # sometimes infinite scrollling will stop and instead show 
            # load more button. If this is the case check if such an 
            # element exists and just click on it then continue scrolling down
            if element_exists(driver=driver, css_path=".scaffold-layout__main .scaffold-finite-scroll__load-button") == True:
                print("element exists")
                driver.refresh()
                time.sleep(5)
                
                """THIS DOESN"T WORK BECAUSE EVEN IF THE ELEMTN EXISTS THE FACT THAT IT IS DYNAMIC
                WILL MAKES IT STALE AND THEREFORE CLICKING ON IT WILL RAISE A STALE ELEMENT REFERENCE
                ERROR"""
                load_more_btn = driver.find_element(By.CSS_SELECTOR, ".scaffold-layout__main .scaffold-finite-scroll__load-button")
                load_more_btn.click()
                time.sleep(1.5)
        
        connections = driver.find_elements(By.CSS_SELECTOR, ".artdeco-list")
        # print("test", connections)
        # print(len(connections))
        
        for connection in connections:
            card_link = connection.find_element(By.CSS_SELECTOR, ".mn-connection-card__link")
            conn_link = card_link.get_attribute('href')

            card_name = connection.find_element(By.CSS_SELECTOR, ".mn-connection-card__name")
            conn_name = card_name.text
            
            # if connection link and connection name already exists
            # exclude it in dataframe
            if ((lookup_file['conn_link'] == conn_link) & (lookup_file['conn_name'] == conn_name)).any() or conn_name == 'Michael Cueva':
                continue

            # if dataframe is empty or has some rows we can just concatenate an empty dataframe
            conn_links.append(conn_link)
            conn_names.append(conn_name)

    except TimeoutError as error:
        print("Error {} has occured".format(error))

    # catch both NoSuchElementException and StaleElementReferenceException errors
    except (NoSuchElementException, StaleElementReferenceException) as error:
        print("Error {} has occured".format(error))

    finally:
        print("Done!")

    # concatenate collected connection names and respective links
    print(conn_links)
    temp = pd.DataFrame({'conn_link': conn_links, 'conn_name': conn_names})
    dump = pd.concat([temp, lookup_file], axis=0)
    dump.to_csv('./documents/profiles_dump.csv')

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

def load_file():
    """
    loads and/or creates a .csv file if one does not already exist
    """

    try:
        dump = pd.read_csv('./documents/profiles_dump.csv', index_col=0)
    except FileNotFoundError as e:
        # if no file has been found creawte a new dataframe and return it
        # in order to be populated by the connection information extractor
        print(f'{e} has occured. Creating a new dataframe...')
        dump = pd.DataFrame({'conn_link': [], 'conn_name': []})

    return dump
    
    

def main(args):
    # load environment variables path
    env_dir = Path('./').resolve()
    load_dotenv(os.path.join(env_dir, '.env'))

    # if using chrome
    chrome_options = ChromeOptions()
    
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-setuid-sandbox") 
    # chrome_options.add_argument("--remote-debugging-port=5000")
    # chrome_options.add_argument("--disable-dev-shm-using") 
    # chrome_options.add_argument("--disable-extensions") 
    # chrome_options.add_argument("--disable-gpu") 
    # chrome_options.add_argument('--headless')

    # to check what profile to use when set to profile-directory argument 
    # passed toself.add_argument() enter edge://version/ in search address 
    # of edge to see the meta data. There you will see the Profile Path of the 
    # account signed in in your browser, in this Profile Path you will see
    # C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\<folder of the 
    # profile being used> just assign this to the profile-directory argument 
    # and pass the string in the self.add_argument() method
    # chrome_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/")
    # chrome_options.add_argument("profile-directory=Profile 3")
    
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(executable_path="C:/Program Setups.Exe/chromedriver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # extract all connections info
    dump = load_file()
    profiles = extract_con_links(driver=driver, lookup_file=dump)

    # save current links collected to .csv file and continue script
    
    # dump = pd.DataFrame({'links_to_profiles': profiles[0], 'profile_names': profiles[1]})
    # dump.to_csv('./documents/profiles_dump.csv')

    # driver.close()
    # driver.quit()


    # collect_recruiter_info(driver, links)

    

    
