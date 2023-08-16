from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from bs4 import BeautifulSoup
import requests
import pandas as pd

from concurrent.futures import ProcessPoolExecutor
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



def collect_links_to_connections(driver: webdriver.Chrome, link: str):
    """
        this function has to be operated by chrome webdriver because linked
        in page has dynamic elements
        args:
            driver
    """
    try:
        driver.get(link)
        wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

        # div = driver.find_element(By.CSS_SELECTOR, 'html > body > div:nth-of-type(5) > div:nth-of-type(3) > div > div > div > div > div:nth-of-type(2) > div > div > main > div > section > div:nth-of-type(2)')
        # print(div)

    except TimeoutError as error:
            print("Error {} has occured".format(error))
            driver.quit() # or .close()

    # catch both NoSuchElementException and StaleElementReferenceException errors
    except (NoSuchElementException, StaleElementReferenceException) as error:
        print("Error {} has occured".format(error))

    except:
        print('ERROR HAS OCCURED')

    finally:
        print("done!")


def main():
    # if using chrome
    # chrome_options = ChromeOptions()
    # chrome_options.add_experimental_option('detach', True)
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # service = ChromeService(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    # if using edge
    
    # to check what profile to use when set to profile-directory argument 
    # passed toself.add_argument() enter edge://version/ in search address 
    # of edge to see the meta data. There you will see the Profile Path of the 
    # account signed in in your browser, in this Profile Path you will see
    # C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\<folder of the 
    # profile being used> just assign this to the profile-directory argument 
    # and pass the string in the self.add_argument() method

    edge_options = EdgeOptions()
    edge_options.add_experimental_option('detach', True)
    edge_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Microsoft/Edge/User Data/")
    edge_options.add_argument("profile-directory=Default")

    # edge_options.add_experimental_option('useAutomationExtension', False)
    # edge_options.add_argument("--headless")
    # edge_options.add_argument("--disable-web-security")
    # edge_options.add_argument("--allow-running-insecure-content")
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    # service = EdgeService(executable_path="C:/Program Setups.Exe/msedgedriver/msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=edge_options)


    
    links_to_connections = collect_links_to_connections(driver=driver, link="https://www.linkedin.com/mynetwork/invite-connect/connections/")
    # collect_recruiter_info(driver, links)

    

    
