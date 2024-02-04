from generate_cover_letter import main as app_2
from send_letter import main as app_3
from linkedin_conn_scraper import main as app_4
from linkedin_conn_info_scraper import main as app_5

from argparse import ArgumentParser




if __name__ == "__main__":
    parser = ArgumentParser()

    # for app 1
    # port argument and server
    parser.add_argument('--host', type=str, default='smtp.gmail.com')
    parser.add_argument('--port', type=int, default='465')
    parser.add_argument('--department', type=str, default='Data Analytics')

    # for app 2
    parser.add_argument('--position', type=str, default='Data Analyst')
    parser.add_argument('--company_name', type=str, default='Accenture')
    args = parser.parse_args()

    option = int(input("""
        1 - AUTOMATED COVER LETTER AND CV/RESUME SENDER
        2 - AUTOMATED COVER LETTER GENERATOR
        3 - AUTOMATED LETTER OF INQUIRY SENDER
        4 - RECRUITER LINK & NAME SCRAPER
        5 - RECRUITER CONTACT INFO SCRAPER
        CHOOSE WHICH APPLICATION TO USE:
    """))

    apps = {
        1: 0,
        2: app_2,
        3: app_3,
        4: app_4,
        5: app_5
    }
    
    apps[option](args)