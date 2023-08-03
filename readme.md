# **STILL IN PRODUCTION**

# A mini-project that automates sending my cv/resume and cover letter to companies and job recruiters en masse.

# Usage:
1. clone repository with `git clone https://github.com/08Aristodemus24/auto-job-app-sender`
2. navigate to directory with `readme.md` and `requirements.txt` file
3. run command; `conda create -n <name of env e.g. auto-job-app-sender> python=3.11.4`. Note that 3.11.4 must be the python version otherwise packages to be installed would not be compatible with a different python version
4. once environment is created activate it by running command `conda activate`
5. then run `conda activate auto-job-app-sender`
6. check if pip is installed by running `conda list -e` and checking list
7. if it is there then move to step 8, if not then install `pip` by typing `conda install pip`
8. if `pip` exists or install is done run `pip install -r requirements.txt` in the directory you are currently in

# Replication:
1. generate app password on your google account: https://myaccount.google.com/apppasswords
2. to use it open the *Mail* app.
3. Open the *Settings* menu.
4. Select *Accounts* and then select your Google Account.
5. Replace your password with the 16-character password shown above.
6. Just like your normal password, this app password grants complete access to your Google Account. You won't need to remember it, so don't write it down or share it with
7. use generated password for `smtplib`

# Implemenation ideas:
1. maybe instead of loop use multithreading or concurrent execution to deliver emails at faster speeds

# Concepts:
This automated job application sender will consist of about three phases: sending automated cover letters and cvs/resumes to recruiter and HR emails, sending follow up letters about the applied position to the company after sending the cover letters and cvs/resumes to said companies through each recruiter and HRs emails, and lastly would be sending an "ask the recruiter" letter for inquiries if a certain role/position is available to the company.

Some ideas also that I can also implement will be to automate the manual process of filling up online forms on LinkedIn, Glassdoor, Indeed, Kalibrr, Jobyoda, Jobstreet, Foundit, and Company Websites.

# Problems:
1. for some reason long hyphen character in cover letter when read and then decoded gives error `UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 2036: ordinal not in range(128)`. Solution was to replace it with a tilde `~` character.
