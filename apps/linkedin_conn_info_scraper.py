import undetected_chromedriver as webdriver
# import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

import os
import time
from dotenv import load_dotenv
from pathlib import Path

from utilities.loaders import load_file
from utilities.utilities import element_exists, augment_df



def extract_conn_info(driver: webdriver.Chrome, lookup_file: pd.DataFrame, dump: pd.DataFrame):
    """
    args:
        driver - 
        lookup_file - 
        dump - 
    """

    for index, df in lookup_file.iterrows():
        try:
            # login first
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
            # driver.switch_to.window(windows[-1])

            # # whsOnd zHQkBf

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

            # now loop through all links to connections and extract their contact info
            # if this somehow crashes the dataframe has already saved data and will go to finally
            # block for post processing
            
            # if any of the columns of dump is not null then skip row
            # if an email is present but no number or if a number is present but no email skip the row
            # i.e. klsldf@gmail.com detected will return false and be negated resulting in true
            # and there is no mobile number which will also result in true
            
            # if either the email or mobile number is null or a "0" string then skip the row

            # if email exists but mobile number is not present 
            if not pd.isnull(dump.loc[index, 'email']) and (dump.loc[index, 'mobile_no'] == "0"):
                print("not pd.isnull(dump.loc[index, 'email']) and (dump.loc[index, 'mobile_no'] == '0')")
                print(dump.loc[index, 'email'])
                print(dump.loc[index, 'mobile_no'])
                print(type(dump.loc[index, 'email']))
                print(type(dump.loc[index, 'mobile_no']))
                print(f"skipping {dump.loc[index, 'conn_name']}", end='\n\n')
                continue

            # if email does not exist but mobile number is present 
            elif pd.isnull(dump.loc[index, 'email']) and not ((dump.loc[index, 'mobile_no'] == "0") or pd.isnull(dump.loc[index, 'mobile_no'])):
                print("pd.isnull(dump.loc[index, 'email']) and not (dump.loc[index, 'mobile_no'] == '0')")
                print(dump.loc[index, 'email'])
                print(dump.loc[index, 'mobile_no'])
                print(type(dump.loc[index, 'email']))
                print(type(dump.loc[index, 'mobile_no']))
                print(f"skipping {dump.loc[index, 'conn_name']}", end='\n\n')
                continue

            
            elif not pd.isnull(dump.loc[index, 'company_name']):
                print(dump.loc[index, 'email'])
                print(dump.loc[index, 'mobile_no'])
                print(type(dump.loc[index, 'email']))
                print(type(dump.loc[index, 'mobile_no']))
                print(f"skipping {dump.loc[index, 'conn_name']}", end='\n\n')
                continue

            elif not pd.isnull(dump.loc[index, 'email']) and not ((dump.loc[index, 'mobile_no'] == "0") or pd.isnull(dump.loc[index, 'mobile_no'])):
                print("not pd.isnull(dump.loc[index, 'email']) and not (dump.loc[index, 'mobile_no'] == '0')")
                print(dump.loc[index, 'email'])
                print(dump.loc[index, 'mobile_no'])
                print(type(dump.loc[index, 'email']))
                print(type(dump.loc[index, 'mobile_no']))
                print(f"skipping {dump.loc[index, 'conn_name']}", end='\n\n')
                continue

            else:

                # extract link from dataframe and navigate to it
                curr_link = df['conn_link']
                curr_name = df['conn_name']
                driver.get(curr_link)
                print(curr_name)

                # wait until the document is loaded
                _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

                # scroll to half of page
                driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 3)")
                time.sleep(5)
                
                # get company name of connection through experience
                company_name = ""
                if element_exists(driver, By.CSS_SELECTOR, "div#experience"):
                    exp_div = driver.find_element(By.CSS_SELECTOR, "div#experience")
                    parent = exp_div.find_element(By.XPATH, "./..")

                    # there are two waysthe company is layed out on the page
                    # either through
                    if element_exists(parent, By.XPATH, "div[3]/ul/li[1]/div/div[2]/div[1]/div/span[1]/span[1]"):
                        company_name_con = parent.find_element(By.XPATH, "div[3]/ul/li[1]/div/div[2]/div[1]/div/span[1]/span[1]")

                    elif element_exists(parent, By.XPATH, "div[3]/ul/li[1]/div/div[2]/div[1]/a/div/div/div/div/span[1]"):
                        company_name_con = parent.find_element(By.XPATH, "div[3]/ul/li[1]/div/div[2]/div[1]/a/div/div/div/div/span[1]")
                    
                    # if experience section does exist rename blank to company name
                    company_name = company_name_con.text
                    
                
                # after scrolling to 1/3 of page move back to top again
                driver.execute_script("window.scrollTo(0, 0)")
                time.sleep(5)
                
                # extract contact info button
                # click contact info button after extracting company nane
                con_info_btn = driver.find_element(By.CSS_SELECTOR, "#top-card-text-details-contact-info")
                con_info_btn.click()
                time.sleep(5)

                # check if the element containing the email and mobile number exists
                # because if it does not then just append nan to the array of emails or
                # mobile nubmers
                email = driver.find_element(By.CSS_SELECTOR, 'svg[data-test-icon="envelope-medium"] ~ div').text \
                    if element_exists(driver, By.CSS_SELECTOR, 'svg[data-test-icon="envelope-medium"] ~ div') \
                    else ""
                mobile_no = driver.find_element(By.CSS_SELECTOR, 'svg[data-test-icon="phone-handset-medium"] ~ ul').text \
                    if element_exists(driver, By.CSS_SELECTOR, 'svg[data-test-icon="phone-handset-medium"] ~ ul') \
                    else 0            

                # if dataframe is empty or has some rows we can just concatenate an empty dataframe
                print(f"email, mobile number, and company name: {email} {mobile_no} {company_name}")
                dump.loc[index, 'email'] = email
                dump.loc[index, 'mobile_no'] = mobile_no
                dump.loc[index, 'company_name'] = company_name
                dump.loc[index, 'conn_name'] = curr_name
                dump.loc[index, 'conn_link'] = curr_link
                
        except TimeoutError as error:
            print("Error {} has occured".format(error))

        # catch both NoSuchElementException and StaleElementReferenceException errors
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as error:
            print("Error {} has occured".format(error))

        finally:
            # if somehow the current index fails to collect connection info then
            # current index is just left blank and loop moves on
            """but what happens when the dataframe is read again?"""
            print("Done!")
            dump.reset_index(drop=True, inplace=True)
            dump.to_csv('../documents/conn_info.csv')

def main(args):
    # load environment variables path
    env_dir = Path('../').resolve()
    load_dotenv(os.path.join(env_dir, '.env'))
    print('loading env vars...')

    # if using chrome
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--no-sandbox")
    # # chrome_options.add_argument("--disable-setuid-sandbox") 
    # # chrome_options.add_argument("--remote-debugging-port=5000")
    # chrome_options.add_argument("--disable-dev-shm-usage") 
    # chrome_options.add_argument("--disable-extensions") 
    # chrome_options.add_argument("--disable-gpu") 
    # # chrome_options.add_argument('--headless')

    # # to check what profile to use when set to profile-directory argument 
    # # passed toself.add_argument() enter edge://version/ in search address 
    # # of edge to see the meta data. There you will see the Profile Path of the 
    # # account signed in in your browser, in this Profile Path you will see
    # # C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\<folder of the 
    # # profile being used> just assign this to the profile-directory argument 
    # # and pass the string in the self.add_argument() method
    chrome_options.add_argument("--user-data-dir=C:/Users/LARRY/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("--profile-directory=Profile 4")
    # chrome_options.add_experimental_option('detach', True)
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(executable_path="C:/Executables/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options, service=service)
    # # for undetected chrome driver
    # driver = webdriver.Chrome(options=chrome_options)

    # extract all connections info
    print('loading file...')
    lookup_file = load_file(
        '../documents/profiles_dump.csv',
        pd.DataFrame({'email': [], 'mobile_no': [], 'company_name': [], 'conn_link': [], 'conn_name': [], 'gender': []})
    )

    # load preexisting dataframe or create and/or augment it
    dump = augment_df(lookup_file, '../documents/conn_info.csv')
    print(dump.dtypes)
    # extract connection info
    print('extracting connections information...')
    extract_conn_info(driver=driver, lookup_file=lookup_file, dump=dump)