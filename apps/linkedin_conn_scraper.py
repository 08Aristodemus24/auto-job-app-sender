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

import re
import time
import os
from dotenv import load_dotenv
from pathlib import Path

from utilities.loaders import load_file
from utilities.utilities import click_until_permitted, augment_df


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
    genders = []
    salutations = []
    emails = []
    mobile_nums = []
    company_names = []
    is_scraped = []

    click_permitted = False

    try:
        # # login first
        # driver.get("https://www.linkedin.com/uas/login/")

        # # wait until the document is loaded
        # _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

        # # get parent window
        # parent_window = driver.current_window_handle

        # # click sign in with google
        # time.sleep(5)
        # gsign_in_btn = driver.find_element(By.CSS_SELECTOR, ".alternate-signin__btn--google")
        # gsign_in_btn.click()
        # time.sleep(5)

        # # get all windows currently open
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])

        # # select the username input in popup authentication window of google
        # username = driver.find_element(By.CSS_SELECTOR, "input[type='email'].whsOnd")
        # username.send_keys(os.environ['GOOGLE_EMAIL'])
        # username.send_keys(Keys.ENTER)
        # time.sleep(5)

        # # select the password input in popup authentication window of google
        # password = driver.find_element(By.CSS_SELECTOR, "input[type='password'].whsOnd")
        # password.send_keys(os.environ['GOOGLE_PASS'])
        # password.send_keys(Keys.ENTER)
        
        # # switch again to current window
        # driver.switch_to.window(parent_window)
        # time.sleep(5)

        # go to new link where connections live
        driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
        time.sleep(5)

        # scroll to the very bottom until there is none left to scroll
        n_connections_header = driver.find_element(By.CSS_SELECTOR, "header.mn-connections__header")
        num_string = "".join(re.findall(r"\d+", n_connections_header.text))
        num_string_cleaned = num_string.replace(",", "")
        n_connections = int(num_string_cleaned)
        print(n_connections)

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(1.5)
        for _ in range(n_connections // 10):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
            time.sleep(1.5)

            # sometimes infinite scrollling will stop and instead show 
            # load more button. If this is the case check if such an 
            # element exists and just click on it then continue scrolling down
            # call this function over and over until it returns a flag indicating it has 
            # finished clicking
            if click_permitted == False:
                click_permitted = click_until_permitted(driver=driver, css_path=".scaffold-finite-scroll .scaffold-finite-scroll__load-button")
                
        
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
            genders.append("")
            salutations.append("")
            emails.append("")
            mobile_nums.append(0)
            company_names.append("")
            is_scraped.append(False)


    except TimeoutError as error:
        print("Error {} has occured".format(error))

    # catch both NoSuchElementException and StaleElementReferenceException errors
    except (NoSuchElementException, StaleElementReferenceException) as error:
        print("Error {} has occured".format(error))

    finally:
        print("Done!")

    # concatenate collected connection names and respective links
    print(conn_links)
    temp = pd.DataFrame({'conn_link': conn_links, 'conn_name': conn_names, 'gender': genders, 'salutation': salutations, 'email': emails, 'mobile_no': mobile_nums, 'company_name': company_names, 'is_scraped': is_scraped})
    dump = pd.concat([temp, lookup_file], axis=0)
    dump.reset_index(drop=True, inplace=True)
    dump.to_csv('../documents/profiles_dump.csv')
    


def main(args):
    # load environment variables path
    env_dir = Path('../').resolve()
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
    chrome_options.add_argument("--user-data-dir=C:/Users/LARRY/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("--profile-directory=Profile 4")
    
    # chrome_options.add_experimental_option('detach', True)
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = ChromeService(executable_path="C:/Executables/chromedriver-win64/chromedriver.exe")
    # service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # extract all connections info
    dump = load_file(
        '../documents/profiles_dump.csv',
        pd.DataFrame({'conn_link': [], 'conn_name': [], 'gender': [], 'salutation': [], 'email': [], 'mobile_no': [], 'company_name': [], 'is_scraped': []})
    )

    # extract connection links and names
    extract_con_links(driver=driver, lookup_file=dump)

    # close driver
    # driver.close()
    # driver.quit()

    

    
