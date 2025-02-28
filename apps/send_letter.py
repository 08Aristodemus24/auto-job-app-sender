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
    BASE_DIR = Path('./').resolve().parent
    print(BASE_DIR)
    load_dotenv(os.path.join(BASE_DIR, '.env'))


def load_company_list(path: str) -> pd.DataFrame:
    """
    
    """
    
    df = pd.read_csv(path, index_col=0) if ".csv" in path else pd.read_excel(path)

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


def create_application_emails(company_list: pd.DataFrame):
    """
    will create the email objects for each and every recruiter
    collected email as a means of application
    """
    

    def _helper(row):
        load_resume = {
            "Data Engineer": lambda: load_files('../documents/Larry_Miguel_R_Cueva_DE_CV.pdf'),
            "Machine Learning Engineer": lambda: load_files('../documents/Larry_Miguel_R_Cueva_ML_CV.pdf')
        }

        load_cover_letter = {
            "Data Engineer": lambda: load_files('../documents/DE_cover_letter_2.txt', is_txt=True),
            "Machine Learning Engineer": lambda: load_files('../documents/MLE_cover_letter_2.txt', is_txt=True)
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

def create_inquiry_emails(company_list: pd.DataFrame, position: str):
    """
    will create the email objects for each and every recruiter
    collected email that inquires if a certain position is available

    position/roles arg can be 'Machine Learning Engineer', 
    'Machine Learning Engineer related' since letter of inquiry has context
    'Is there an available {position} role?' or perhaps 'I want to apply in a
    {position} role'
    """

    def _helper(row, position):
        load_resume = {
            "Data Engineer": lambda: load_files('../documents/Larry_Miguel_R_Cueva_DE_CV.pdf'),
            "Machine Learning Engineer": lambda: load_files('../documents/Larry_Miguel_R_Cueva_ML_CV.pdf')
        }
        
        load_letter_of_inq = lambda: load_files('../documents/cold_email.txt', is_txt=True)

        # load cover letter and resume
        resume, resume_name = load_resume[position]()
        letter_of_inq, _ = load_letter_of_inq()

        # extract info of each row in dataframe to loadi nto text files
        first_name = row['conn_name'].split()[0]
        company_name = row['company_name']
        email = row['email']
        subject = "Inquiry regarding {position} roles/opportunities at {company_name}".format(position=position, company_name=company_name)
        salutation = "Sir." if row['gender'] == "male" else "Ms."
        body = letter_of_inq.format(position=position, company_name=company_name, salutation=salutation, first_name=first_name)
        print(body)

        # create email objects. Add file also
        # as attachment to email object
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['To'] = email
        msg.set_content(body)
        msg.add_attachment(resume, maintype='application', subtype='octet-stream', filename=resume_name)

        return msg
    
    messages = company_list.apply(_helper, args=(position, ), axis=1)
    
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
    position = args.position
    
    # load path to .env file
    load_env_file()

    # extract env variables
    SENDER_EMAIL = os.environ['SENDER_EMAIL']
    SENDER_PASSWORD = os.environ['SENDER_PASSWORD']

    # load csv of company meta data
    company_list = load_company_list('../documents/conn_info.csv')
    print(company_list)

    # drop rows without emails
    new_list = company_list[~pd.isnull(company_list["email"])]
    new_list = new_list.sample(frac=1).reset_index(drop=True)

    # create emails based on company meta data
    # messages = create_application_emails(company_list)
    messages = create_inquiry_emails(new_list, position)
    print(messages, end='\n')

    # bulk send all messages
    bulk_send(SENDER_EMAIL, SENDER_PASSWORD, messages=messages, host=host, port=port)