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
    BASE_DIR = Path('./').resolve()
    load_dotenv(os.path.join(BASE_DIR, '.env'))

def load_company_list(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0)
    return df

def load_files(path: str, is_txt=False) -> tuple:
    with open(path, 'rb') as file:
        # read binary data of file. If file is .txt then deocde to normal string
        file_data = file.read() if is_txt is False else file.read().decode('ascii')

        # get base name of file before sending
        file_name = os.path.basename(file.name)

    return file_data, file_name

def create_emails(company_list: pd.DataFrame, position: str='Data Analytics', subject='Data Analytics application') -> List[EmailMessage]:
    # initialize list to contain all email objects
    # messages = []

    # load cover letter and resume
    resume, resume_name = load_files('./documents/Cueva, Larry Miguel_Resume_A.pdf')
    cover_letter, _ = load_files('./documents/DA_cover_letter_2.txt', is_txt=True)

    def helper(row):
        company_name = row['company_name']
        email = row['email']
        # print(cover_letter.format(position='Data Analytics', company_name=company_name))

        # create email objects. Add file also
        # as attachment to email object
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['To'] = email
        msg.set_content(cover_letter.format(position=position, company_name=company_name))
        msg.add_attachment(resume, maintype='application', subtype='octet-stream', filename=resume_name)
        
        return email
    
    messages = company_list.apply(helper, axis=1)

    # # extract company emails
    # for row in company_list.index:
    #     data = company_list.loc[row, :]
    #     print(data)

    #     company_name = data['company_name']
    #     email = data['email']
    #     print(cover_letter.format(position='Data Analytics', company_name=company_name))

    #     # create email objects. Add file also
    #     # as attachment to email object
    #     msg = EmailMessage()
    #     msg['Subject'] = 'test'
    #     msg['To'] = email
    #     msg.set_content(cover_letter.format(position='Data Analytics', company_name=company_name))
    #     msg.add_attachment(resume, maintype='application', subtype='octet-stream', filename=resume_name)

    #     # append msg object to messages list
    #     messages.append(msg)
    
    return messages

if __name__ == "__main__":
    # port argument and server
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default='smtp.gmail.com')
    parser.add_argument('--port', type=int, default='465')

    args = parser.parse_args()
    host = args.host
    port = args.port
    
    # load path to .env file
    load_env_file()

    # extract env variables
    SENDER_EMAIL = os.environ['SENDER_EMAIL']
    SENDER_PASSWORD = os.environ['SENDER_PASSWORD']

    # load csv of company meta data
    company_list = load_company_list('./documents/dummy.csv')
    print(company_list.head())

    messages = create_emails(company_list)


    # # this block will send the email message to either a local 
    # # host or the email address it was intended to go
    # if host == "localhost" or host == "127.0.0.1":
    #     with smtplib.SMTP(host, port) as smtp:
    #         # send message to local host at port 1025
    #         smtp.send_message(msg=msg)
    #         smtp.send
    # else:
    #     with smtplib.SMTP_SSL(host, port) as smtp:
    #         # login with credentials
    #         smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    #         smtp.send_message(msg=msg)
