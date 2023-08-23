from selenium import webdriver

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
from bs4 import BeautifulSoup
import requests
import pandas as pd

from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

import time


def collect_recruiter_info(driver: webdriver.Chrome, links: list[str]):
    """
    the links contain links to all recruiter profiles pages
    collected by beautiful soup statemetns
    """

    for link in links:
        try:
            driver.get(link)
            wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

        except TimeoutError as error:
            print("Error {} has occured".format(error))
            driver.quit() # or .close()

        # catch both NoSuchElementException and StaleElementReferenceException errors
        except (NoSuchElementException, StaleElementReferenceException) as error:
            print("Error {} has occured".format(error))

        finally:
            print("will go to next link")



def concurrently_extract_con_links(driver: webdriver.Chrome | webdriver.Edge, last_paginator_num: int):
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

    rules = ["recruiter", "recruitment", "recruiting", "hr", "talent", "talent", "acquisition", "human", "resources", "hiring"]

    links_to_profiles = []

    conn_page_link = "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page={}"
    # paginator_links = [conn_page_link.format(paginator_num) for paginator_num in range(1, last_paginator_num + 1)]

    for paginator_num in range(1, last_paginator_num + 1):
        try:
            driver.get(conn_page_link.format(paginator_num))

            _ = WebDriverWait(driver, timeout=20).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

            _ = WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located([By.CSS_SELECTOR, ".reusable-search__result-container"]))
    
            # finds the clickable link elements in connections page of linked in
            div_tag_con_profs = driver.find_elements(By.CSS_SELECTOR, ".reusable-search__result-container .entity-result .mb1")

            #  .app-aware-link

            # get value of href in each link
            link_to_con_profs = [div_tag_con_prof.get_attribute('href') for div_tag_con_prof in div_tag_con_profs if div_tag_con_prof.find_element(By.CSS_SELECTOR, ".linked-area.flex-1.cursor-pointer .entity-result__primary-subtitle.t-14.t-black.t-normal").text.lower()]
            links_to_profiles.extend(link_to_con_profs)
            # print(links_to_profiles)

        except TimeoutError as error:
            print("Error {} has occured".format(error))

        # catch both NoSuchElementException and StaleElementReferenceException errors
        except (NoSuchElementException, StaleElementReferenceException) as error:
            print("Error {} has occured".format(error))

        finally:
            print("Done!")

    # def helper(link):
    #     pass

    # with ThreadPoolExecutor() as thread:
    #     thread.map()

    # print(paginator_links)

    return links_to_profiles


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
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        _ = WebDriverWait(driver, timeout=20).until(EC.visibility_of_all_elements_located([By.CSS_SELECTOR, ".reusable-search__result-container"]))

        # grab paginator of page to determine last pagination number
        paginator = driver.find_element(By.CSS_SELECTOR, ".artdeco-pagination__pages")
        num_lists = paginator.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view")

        # grab last li element of paginator
        last_num = num_lists[-1].text
        print(paginator)
        print(num_lists)
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

    

def main():
    # if using chrome
    chrome_options = ChromeOptions()
    
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-setuid-sandbox") 
    # chrome_options.add_argument("--remote-debugging-port=5000")
    # chrome_options.add_argument("--disable-dev-shm-using") 
    # chrome_options.add_argument("--disable-extensions") 
    # chrome_options.add_argument("--disable-gpu") 
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/")
    chrome_options.add_argument("profile-directory=Default")
    
    chrome_options.add_experimental_option('detach', True)
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(executable_path=ChromeDriverManager().install())
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
    # # service = EdgeService(executable_path="C:/Program Setups.Exe/msedgedriver/msedgedriver.exe")
    # driver = webdriver.Edge(service=service, options=edge_options)

    

    last_paginator_num = collect_last_paginator_num(driver=driver, link="https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=KSa")
    links_to_profiles = concurrently_extract_con_links(driver=driver, last_paginator_num=last_paginator_num)
    print(links_to_profiles)
    print(len(links_to_profiles))
    
    driver.close()
    driver.quit()


    # collect_recruiter_info(driver, links)

    

    
