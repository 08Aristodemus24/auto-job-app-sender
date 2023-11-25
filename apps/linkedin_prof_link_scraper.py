from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

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



def concurrently_extract_con_links(driver: webdriver.Chrome | webdriver.Edge, last_paginator_num: int, excluded_profiles: list[str]):
    """
    given each pagination link concurrently extract the clickable link elements
    of each connection in each paginator number

    a single connection page at paginator 1 can look like this
    "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page=1
    "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=KSa"
    
    page 2 can look like this
    "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page=2&sid=D8T"

    that means we can create a list of links with this links structure 
    https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page=2&sid=D8T
    and assign merely the argument value of page to be equal to numbers 1 to last paginator number. Meaning if page 1 is like
    the above then https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page=<last
    paginator number> will be the last link to visit
    """

    links_to_profiles = []
    profile_names = []

    conn_page_link = "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page={}"
    # paginator_links = [conn_page_link.format(paginator_num) for paginator_num in range(1, last_paginator_num + 1)]

    for paginator_num in range(1, last_paginator_num + 1):
        try:
            driver.get(conn_page_link.format(paginator_num))

            # wait until the document is loaded
            _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

            # wait until the whole UL containing all the list of profiles 
            # is loaded and wait again for 3 seconds
            _ = WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located([By.CSS_SELECTOR, ".reusable-search__entity-result-list"]))
            time.sleep(3)

            # scroll to the bottom and wait for three seconds again
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
            time.sleep(3)
    
            # finds the clickable link elements in connections page of linked in
            div_tag_con_profs = driver.find_elements(By.CSS_SELECTOR, ".reusable-search__result-container .entity-result .mb1")

            # get value of href in each link if and only if 
            # name is not included in excluded profiles
            link_to_con_profs = []
            con_profs_name = []
            idx_where_err_occured = 0
            for index, div_tag_con_prof in enumerate(div_tag_con_profs):
                # show current profile index to execute
                print(f'executing profile {index}')

                # set current index to this variable in case
                # error is raised we can track which profile index
                # it occured and still continue searching through profiles
                idx_where_err_occured = index

                # check if element exists and if it does get its span 
                # containing name and exclude those elements included 
                # in the excluded profiles list
                profile_name = div_tag_con_prof.find_element(By.CSS_SELECTOR, ".entity-result__title-text") \
                .find_element(By.CSS_SELECTOR, "span[dir='ltr']") \
                .find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text.lower()

                # print profile name
                print(f'profile {profile_name}')

                if profile_name not in excluded_profiles:
                    # print profile index
                    print(f'profile {index}: {div_tag_con_prof}')

                    # extract link
                    link = div_tag_con_prof.find_element(By.CSS_SELECTOR, ".entity-result__title-text") \
                    .find_element(By.CSS_SELECTOR, ".app-aware-link") \
                    .get_attribute('href')

                    # append link to profile to list
                    link_to_con_profs.append(link)
                    con_profs_name.append(profile_name)

            links_to_profiles.extend(link_to_con_profs)
            profile_names.extend(con_profs_name)

        except TimeoutError as error:
            print("Error {} has occured".format(error))

        # catch both NoSuchElementException and StaleElementReferenceException errors
        except (NoSuchElementException, StaleElementReferenceException) as error:
            print("Error {} has occured".format(error))

        finally:
            print("Done!")

    return links_to_profiles, profile_names


def collect_last_paginator_num(driver: webdriver.Chrome | webdriver.Edge, link: str):
    """
        this function has to be operated by chrome webdriver because linked
        in page has dynamic elements
        args:
            driver
    """

    links_to_profiles = []
    last_num = -1

    try:
        driver.get(link)
        _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

        _ = WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located([By.CSS_SELECTOR, ".reusable-search__result-container"]))

        # grab paginator of page to determine last pagination number
        paginator = driver.find_element(By.CSS_SELECTOR, ".artdeco-pagination__pages")
        num_lists = paginator.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view")

        # grab last li element of paginator
        last_num = num_lists[-1].text
        # print(paginator)
        # print(num_lists)
        print(last_num)

    except TimeoutError as error:
        print("Error {} has occured".format(error))

    # catch both NoSuchElementException and StaleElementReferenceException errors
    except (NoSuchElementException, StaleElementReferenceException) as error:
        print("Error {} has occured".format(error))

    # except:
    #     print('ERROR HAS OCCURED')

    finally:
        print("Done!")
        return int(last_num)


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
    # chrome_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/")
    # chrome_options.add_argument("profile-directory=Profile 3")
    
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(executable_path="C:/Program Setups.Exe/chromedriver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # if using edge
    
    # to check what profile to use when set to profile-directory argument 
    # passed toself.add_argument() enter edge://version/ in search address 
    # of edge to see the meta data. There you will see the Profile Path of the 
    # account signed in in your browser, in this Profile Path you will see
    # C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\<folder of the 
    # profile being used> just assign this to the profile-directory argument 
    # and pass the string in the self.add_argument() method

    # edge_options = EdgeOptions()
    # edge_options.add_experimental_option('detach', True)
    # edge_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Microsoft/Edge/User Data/")
    # edge_options.add_argument("profile-directory=Default")

    # # edge_options.add_experimental_option('useAutomationExtension', False)
    # # edge_options.add_argument("--headless")
    # # edge_options.add_argument("--disable-web-security")
    # # edge_options.add_argument("--allow-running-insecure-content")
    # service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    # service = EdgeService(executable_path="C:/Program Setups.Exe/msedgedriver/msedgedriver.exe")
    # driver = webdriver.Edge(service=service, options=edge_options)

    driver.get("https://www.linkedin.com/uas/login/")

    # wait until the document is loaded
    _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

    # get parent window
    parent_window = driver.current_window_handle
    print(parent_window)

    # click sign in with google
    time.sleep(5)
    gsign_in_btn = driver.find_element(By.CSS_SELECTOR, ".alternate-signin__btn--google")
    gsign_in_btn.click()
    time.sleep(5)

    # get all windows currently open
    windows = driver.window_handles
    print(windows)
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
    print(driver.window_handles)
    time.sleep(5)

    # go to new link where connections live
    driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    time.sleep(5)

    test = driver.find_elements(By.CSS_SELECTOR, ".artdeco-list")
    print("test", test)


    # excluded_profiles = load_excluded('./documents/excluded_profiles.txt')
    # last_paginator_num = collect_last_paginator_num(driver=driver, link="https://www.linkedin.com/mynetwork/invite-connect/connections/")
    # profiles = concurrently_extract_con_links(driver=driver, last_paginator_num=last_paginator_num, excluded_profiles=excluded_profiles)

    # # save current links collected to .csv file and continue script
    # dump = pd.DataFrame({'links_to_profiles': profiles[0], 'profile_names': profiles[1]})
    # dump.to_csv('./documents/profiles_dump.csv')

    # driver.close()
    # driver.quit()


    # collect_recruiter_info(driver, links)

    

    
