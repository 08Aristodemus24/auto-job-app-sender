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

import os
import time
from dotenv import load_dotenv
from pathlib import Path

from utilities.loaders import load_file
from utilities.utilities import element_exists



def extract_conn_info(driver: webdriver.Chrome | webdriver.Edge, lookup_file: pd.DataFrame):
    emails = []
    mobile_nums = []
    company_names = []

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

        # now loop through all links to connections and extract their contact info
        for index, df in lookup_file.iterrows():
            # extract link from dataframe and navigate to it
            curr_link = df['conn_link']
            driver.get(curr_link)

            # wait until the document is loaded
            _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))
            
            # scroll to half of page
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 3)")
            time.sleep(5)

            # get parent window
            parent_window = driver.current_window_handle
            # print(parent_window)

            # there are two waysthe company is layed out on the page
            # either through
            div = driver.find_element(By.CSS_SELECTOR, "div#experience ~ div.pvs-list__outer-container li:first-child div.display-flex")
            print(div.text)
            # company_name = div.find_element(By.CSS_SELECTOR, "div > div > div > div > div > div > span:first-child").text \
            #     if element_exists(driver, "ul.pvs-list li:first-child div.display-flex > div > div > span:nth-child(2) > span:first-child") \
            #     else div.find_element(By.CSS_SELECTOR, "div > a.optional-action-target-wrapper > div > div > div > span:first-child").text
            
            # # extract button and click it
            # con_info_btn = driver.find_element(By.CSS_SELECTOR, "#top-card-text-details-contact-info")
            # con_info_btn.click()
            # time.sleep(5)

            # # check if the element containing the email and mobile number exists
            # # because if it does not then just append nan to the array of emails or
            # # mobile nubmers
            # email = driver.find_element(By.CSS_SELECTOR, 'svg[data-test-icon="envelope-medium"] ~ .pv-contact-info__ci-container').text \
            #     if element_exists(driver, 'svg[data-test-icon="envelope-medium"] ~ .pv-contact-info__ci-container') \
            #     else ""
            # mobile_no = driver.find_element(By.CSS_SELECTOR, 'svg[data-test-icon="phone-handset-medium"] ~ ul').text \
            #     if element_exists(driver, 'svg[data-test-icon="phone-handset-medium"] ~ ul') \
            #     else 0            
            
            # print(f"email, mobile number, and company name: {email} {mobile_no} {company_name}")
            
            # emails.append(email)
            # mobile_nums.append(mobile_no)
            # company_names.append(company_name)
            
    except TimeoutError as error:
        print("Error {} has occured".format(error))

    # catch both NoSuchElementException and StaleElementReferenceException errors
    except (NoSuchElementException, StaleElementReferenceException) as error:
        print("Error {} has occured".format(error))

    finally:
        print("Done!")

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
    # chrome_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/")
    # chrome_options.add_argument("profile-directory=Profile 3")
    
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(executable_path="C:/Program Setups.Exe/chromedriver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # extract all connections info
    dump = load_file()
    extract_conn_info(driver=driver, lookup_file=dump)