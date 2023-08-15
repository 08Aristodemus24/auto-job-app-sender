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

# Applications to be integrated:
1. automated sender of cover letters and cvs/resumes about certain position in a company to recruiter and HR emails
2. automated sender of follow up letters about applied position in a company to recruiters and HRs emails
3. automated sender of letter of inquiry about certain position in a company to recruiter and HR emails
4. web scraper of recruiter emails and addresses in linked in **TBD**
5. Some ideas also that I can also implement will be to automate the manual process of filling up online forms on LinkedIn, Glassdoor, Indeed, Kalibrr, Jobyoda, Jobstreet, Foundit, and Company Websites. **TBD**

## Automated cover letter and CV sender
### Usage:
1. if you don't want to send cover letter and cv directly to emails use `"localhost"` for `--host` arg and `1025` for `--port` arg

### Ideas:
1. 

### Problems:
1. for some reason long hyphen character in cover letter when read and then decoded gives error `UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 2036: ordinal not in range(128)`. Solution was to replace it with a tilde `~` character.

## Automated follow up letter sender
### Ideas:
### Problems:

## Automated letter of inquiry sender
### Ideas:
### Problems:

## Automated scraper of recruiter emails
### Ideas:
1. places where to find recruiter and HR emails:
a. contacts section of website of company applied to 
b. LinkedIn profile of company applied to, see people and add every recruiter you can see, go to recuiters profile and extact email if any
c. go to LinkedIn profile of recruiters, see their connections and add every recruiter you can see, then go to each of these recruiters profile and extract email if any

2. keywords for potential recruiters are: "talent", "acquisition", "hiring", "recruitment"
3. main app:
a. use selenium webdriver and ChromDriverManager().install()
a. 
### Problems:
1. can't sign in in google account using webdriver. Possible solution: https://stackoverflow.com/questions/60117232/selenium-google-login-block

ff. solutions do not work:
a.
edge_options.add_argument("--disable-web-security")
edge_options.add_argument("--allow-running-insecure-content")
edge_options.add_argument("--user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/Profile 1")

b. turning off 2-factor authentication

c. tried turning on less secure apps but I've researched that google already has removed the option to allow connections from less secure apps starting from May 30 2022. That you have to enable 2-step verification on your Google account and generate an app password123 to use Google SMTP server or other third-party apps that require Google sign-in, which is a direct contradiction to **solution b.**

d. JavaScript is always turned on in my Edge browser

ff. are my error messages:
[<some token>/184906.747:ERROR:chrome_browser_cloud_management_controller.cc(162)] Cloud management controller initialization aborted as CBCM is not enabled.
[<some token>/184906.769:ERROR:assistance_home_client.cc(32)] File path C:\Users\Mig\AppData\Local\Temp\scoped_dir1308_592920665\Default

DevTools listening on ws://127.0.0.1:<some token>
[<some token>/184908.140:ERROR:fallback_task_provider.cc(124)] Every renderer should have at least one task provided by a primary task provider. If a "Renderer" fallback task is shown, it is a bug. If you have repro steps, please file a new bug and tag it as a dependency of crbug.com/739782.
[<some token>/184909.398:ERROR:smartscreen_dns_resolver.cc(110)] SmartScreenDnsResolver::OnComplete Error: -7 DidTimeOut: 1 URL: https://www.linkedin.com/mynetwork/invite-connect/connections/
done!
[<some token>/184912.991:ERROR:gpu_disk_cache.cc(216)] Failed to create blob cache entry: -2

(gmail-automations) D:\Projects\To Github\auto-job-app-sender>[<some token>/184918.305:ERROR:device_event_log_impl.cc(222)] [18:49:18.305] Bluetooth: bluetooth_adapter_winrt.cc:1058 Getting Default Adapter failed.