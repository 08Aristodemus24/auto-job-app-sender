# **STILL IN PRODUCTION**

# A mini-project that automates sending my cv/resume and cover letter to companies and job recruiters en masse.
<p align="center"><img src="https://github.com/08Aristodemus24/auto-job-app-sender/blob/master/assets/mediafiles/We%20Are%20Not%20The%20Same%206395.jpg" alt="gus" style="max-width: 100% max-height: 100%"/></p>


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
**Usage:**
1. if you don't want to send cover letter and cv directly to emails use `"localhost"` for `--host` arg and `1025` for `--port` arg
2. python main.py --host localhost --port 1025 --position "Data Analyst"
**Ideas:**
1. 

**Problems:**
1. for some reason long hyphen character in cover letter when read and then decoded gives error `UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 2036: ordinal not in range(128)`. Solution was to replace it with a tilde `~` character.

## Automated follow up letter sender
**Ideas:**
**Problems:**

## Automated letter of inquiry sender
**Ideas:**
**Problems:**

## Automated scraper of recruiter emails
**Ideas:**
1. places where to find recruiter and HR emails:
a. contacts section of website of company applied to 
b. LinkedIn profile of company applied to, see people and add every recruiter you can see, go to recuiters profile and extact email if any
c. go to LinkedIn profile of recruiters, see their connections and add every recruiter you can see, then go to each of these recruiters profile and extract email if any

2. keywords for potential recruiters are: "talent", "acquisition", "hiring", "recruitment"
3. main app:
a. use selenium webdriver and ChromDriverManager().install()
a. 
4. identify if name is male or female through genderize.io api. Below is an example of using the API and using a batch of names to process whether male or female which can be up to 10. Note that requests per day can be up to 1000 names/day
```
>>> import requests
>>>
>>> response = requests.get('https://api.genderize.io/?name=larry')
>>> response = requests.get('https://api.genderize.io/?name[]=larry&name[]=lalai')
>>> response.status_code
200
>>> response.json()
[{'count': 269573, 'name': 'larry', 'gender': 'male', 'probability': 1.0}, {'count': 24, 'name': 'lalai', 'gender': 'female', 'probability': 0.71}]
>>> response.headers
{'Server': 'nginx/1.16.1', 'Date': 'Fri, 29 Sep 2023 02:32:43 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '132', 'Connection': 'keep-alive', 'access-control-allow-credentials': 'true', 'access-control-allow-origin': '*', 'access-control-expose-headers': 'x-rate-limit-limit,x-rate-limit-remaining,x-rate-limit-reset', 'cache-control': 'max-age=0, private, must-revalidate', 'x-rate-limit-limit': '1000', 'x-rate-limit-remaining': '995', 'x-rate-limit-reset': '77237', 'x-request-id': 'F4k930HDta9MRfMVIdEx'}
```

note that if x-rate-limit-remaining is 0 then you must wait for x-rate-limit-reset to count down to zero since it represents the seconds left until a new set of x-rate-limit-remaining's is refreshed. 47505 seconds or 13 hours is the amount of time left until I can make requests again.

The headers also contain information about how much names we have left to process for a given time period. X-Rate-Limit-Limit is the amount of names available in current time window, X-Rate-Limit-Remaining is the number of names left in the current time window

SOme errors that we can handle are 401 unauthorized, 402 payment required, 422 unprocessable entity, 429 too many requests, a

**To do:**
1. Because linked sent notice for suspicions of my using of automation tools like selenium, I'll have to go under for a while and just complete running the connection info scraper application next time, and collect all connection info. For now just merge what dataframes you have along the index, since both dataframes containing profile names and their respective emails, mobile num, and company name are all aligned by index.


**Problems:**
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

e. kill all chrome or edge tasks and processes
f. arg combinations:
chrome_options.add_argument('--headless')
chrome_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/")
chrome_options.add_argument("profile-directory=Default")

chrome_options.add_experimental_option('detach', True)

g. solution combination was to use chrome, using chrome with my google account profile signed in, and killing all task processes

h. get number of last number of paginator to determine how many times you loop and use the driver to request these pages and then get the links then move on

i. so each page in paginator will eventually give out an error because an element that you select does not exist. Which basically kills all the chances that other profiles could even exist and yet is skipped unfortunately. Potential solution is to implement a fallback not to skip the current page in the paginator but to find the next element that could exist

j. selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 114
Current browser version is 119.0.6045.160 with binary path C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
Stacktrace:

```
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-setuid-sandbox") 
# chrome_options.add_argument("--remote-debugging-port=5000")
# chrome_options.add_argument("--disable-dev-shm-using") 
# chrome_options.add_argument("--disable-extensions") 
# chrome_options.add_argument("--disable-gpu") 
# chrome_options.add_argument('--headless')

# to check what profile to use when set to profile-directory argument 
# passed toself.add_argument() enter edge://version/ in search address 
# of edge to see the meta data. There you will see the Profile Path of the 
# account signed in in your browser, in this Profile Path you will see
# C:\Users\<user>\AppData\Local\Microsoft\Edge\User Data\<folder of the 
# profile being used> just assign this to the profile-directory argument 
# and pass the string in the self.add_argument() method
# chrome_options.add_argument("user-data-dir=C:/Users/Mig/AppData/Local/Google/Chrome/User Data/")
# chrome_options.add_argument("profile-directory=Profile 3")

# chrome_options.add_experimental_option('detach', True)
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_experimental_option('useAutomationExtension', False)
```

k.
```
 raise SMTPServerDisconnected("Connection unexpectedly closed")
smtplib.SMTPServerDisconnected: Connection unexpectedly closed
```
in reality it is rate limiting you due to the bulk requests you are sending to send your email

```
 retcode (421); Msg: 4.7.0 [ip.octets.listed.here      15] Our system has detected an unusual rate of
    4.7.0 unsolicited mail originating from your IP address. To protect our
    4.7.0 users from spam, mail sent from your IP address has been temporarily
    4.7.0 rate limited. Please visit
    4.7.0  https://support.google.com/mail/answer/81126 to review our Bulk Email
    4.7.0 Senders Guidelines. qa9si9093954wjc.138 - gsmtp
```

# Insights
**A vague plan for getting a job**
1. Exhaust networking by messaging each of my classmates if a spot is open in their company, or if they have an email of their recruiter
2. Go to healthy gamer and ask for websites where to apply for a software engineering job or any data related job
3. Apply at the ff. according to rank in terms of probability of success (list of websites are in `.env` file)

* referral from colleague. This strategy you will message each of your remotely close colleagues and old classmates and see if they have their HRs email, and then email that HR regarding if there is an open position at their <comapny name> and that your <friend or colleage who works at said company> can vouch for your skills and accomplished projects

4. Use fiverr and accept clients only that are within reason of your work sched, project scope i.e. no chat gpt related, research how clients pay you for your services
5. Create accounts for each career website if you have to
6. Tune your resume/cv tailored for Machine Learning, Data Science, and Software Engineering because this is what you're good at.
7. Tune your cover letter for the aforementioned roles
8. Ready your premade answers to application questions like "why do want to work at this company?" Which will be found at project Solzhenitsyn
9. Prepare for technical interviews especially in Sql, machine learning, data structures, and take home projects if any, but attempt to do first an interview even if you feel your rusty or unknowledgeable you never know what awaits you so jist try, and if you don't know it means you have learning to do, it's time that yous top always preparing and feeling like you're not ready, because you never know you are unless you really try. Take the leap now and be courageous
10. Prepare excel sheet that will contain list of all applied companies, their email, and the role your applying for, and its current status
11. when submitting job applications usually there will be application fields like:
* why do you want to work at this company?
* attach your CV or resume
* Minimum salary. 50000php/$850 per month or 600000php/$10000 per month 
* 
12. so if I am to work in Pacific Standard Time? (dayshift), i.e. start time of work is 9:00am in the us what tiem would I work in the philippines?

If you're working a 9 AM to 5 PM Pacific Standard Time (PST) shift, considering the 16-hour time difference between PST and Philippine Standard Time (PST), your work hours in the Philippines would be:

9:00 AM PST = 9:00 PM PST (Philippines)
5:00 PM PST = 5:00 AM PST (Philippines, the next day)

So, you'd be working an overnight shift from 9:00 PM to 5:00 AM Philippine Standard Time.

Philippine Standard Time: Tuesday, Wednesday, Thursday at 9am-12pm and 1pm-5pm 
13. reply to recruiters after application: 
`Hello and Good day Maam Edna I've answered the application form you've sent me, about the AI Engineer position. I also look forward to your response to me back. Best, regards.`


with this you should always have your `generate_cover_letter` script always ready, and the `message body to professionals` document always ready which is part of `project Solzhenitsyn`, so you can move and apply quickly. This is a numbers game and it all depends hwo much input you put in during the day. Recall that `generate_cover_letter.py` usage requires `position` and `company` args

