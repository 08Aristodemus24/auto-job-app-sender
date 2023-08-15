from apps.recruiter_email_scraper import main






if __name__ == "__main__":
    option = int(input("""
        1 - AUTOMATED COVER LETTER AND CV/RESUME SENDER
        2 - AUTOMATED COVER LETTER GENERATOR
        3 - AUTOMATED LETTER OF INQUIRY SENDER
        4 - RECRUITER EMAIL SCRAPER
        CHOOSE WHICH APPLICATION TO USE:
    """))

    apps = {
        1: 0,
        2: 0,
        3: 0,
        4: main
    }
    
    apps[option]()