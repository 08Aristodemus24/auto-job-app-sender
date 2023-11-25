import os
import sys
import requests
import smtplib
from email.message import EmailMessage
from argparse import ArgumentParser

from typing import List
from dotenv import load_dotenv
from pathlib import Path

import pandas as pd


def load_env_file() -> None:
    """
    
    """
    BASE_DIR = Path('./').resolve()
    load_dotenv(os.path.join(BASE_DIR, '.env'))


def load_company_list(path: str) -> pd.DataFrame:
    """
    
    """
    # df = pd.read_csv(path, index_col=0)
    df = pd.read_excel(path)
    return df


def load_files(path: str, is_txt=False) -> tuple:
    """
    
    """
    with open(path, 'rb') as file:
        # read binary data of file. If file is .txt then deocde to normal string
        file_data = file.read() if is_txt is False else file.read().decode('ascii')

        # get base name of file before sending
        file_name = os.path.basename(file.name)

    return file_data, file_name


def create_emails(company_list: pd.DataFrame):
    """
    
    """
    

    def _helper(row):
        load_resume = {
            "Data Analyst": lambda: load_files('./documents/Cueva, Larry Miguel_Resume_B.pdf'),
            "Machine Learning Engineer": lambda: load_files('./documents/Cueva, Larry Miguel_Resume_A.pdf')
        }

        load_cover_letter = {
            "Data Analyst": lambda: load_files('./documents/DA_cover_letter_2.txt', is_txt=True),
            "Machine Learning Engineer": lambda: load_files('./documents/MLE_cover_letter_2.txt', is_txt=True)
        }

        company_name = row['company_name']
        email = row['email']
        position = row['position']
        subject = "{} Application".format(row['position'])

        # load cover letter and resume
        resume, resume_name = load_resume[position]()
        cover_letter, _ = load_cover_letter[position]()
        print(cover_letter.format(position=position, company_name=company_name))

        # create email objects. Add file also
        # as attachment to email object
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['To'] = email
        msg.set_content(cover_letter.format(position=position, company_name=company_name))
        msg.add_attachment(resume, maintype='application', subtype='octet-stream', filename=resume_name)

        return msg
    
    messages = company_list.apply(_helper, axis=1)
    
    return messages


def bulk_send(SENDER_EMAIL: str, SENDER_PASSWORD: str, messages: pd.Series, host: str, port: int) -> None:
    """
    
    """
    for index in range(messages.shape[0]):
        # this block will send the email message to either a local 
        # host or the email address it was intended to go
        if host == "localhost" or host == "127.0.0.1":
            with smtplib.SMTP(host, port) as smtp:
                # send message to local host at port 1025
                smtp.send_message(msg=messages.iloc[index])
        else:
            with smtplib.SMTP_SSL(host, port) as smtp:
                # login with credentials
                smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
                smtp.send_message(msg=messages.iloc[index])



def main(args):
    """
    
    """
    host = args.host
    port = args.port
    
    # load path to .env file
    load_env_file()

    # extract env variables
    SENDER_EMAIL = os.environ['SENDER_EMAIL']
    SENDER_PASSWORD = os.environ['SENDER_PASSWORD']

    # load csv of company meta data
    company_list = load_company_list('./documents/dummy.xlsx')
    print(company_list)

    # create emails based on company meta data
    messages = create_emails(company_list)
    # print(type(messages), end='\n')

    # bulk send all messages
    bulk_send(SENDER_EMAIL, SENDER_PASSWORD, messages=messages, host=host, port=port)
    
