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
## A vague plan for getting a job

### other information regarding applying to jobs
* Use fiverr and accept clients only that are within reason of your work sched, project scope i.e. no chat gpt related, research how clients pay you for your services
* Create accounts for each career website if you have to
* Tune your resume/cv tailored for Machine Learning, Data Science, and Software Engineering because this is what you're good at.
* Tune your cover letter for the aforementioned roles
* Ready your premade answers to job application questions like **why do want to work at this company?** Which will be found at `behavioral-interview-questions.md`
* Prepare for technical interviews especially in Sql, machine learning, data structures, and take home projects if any, but attempt to do first an interview even if you feel your rusty or unknowledgeable you never know what awaits you so jist try, and if you don't know it means you have learning to do, it's time that yous top always preparing and feeling like you're not ready, because you never know you are unless you really try. Take the leap now and be courageous
* Prepare excel sheet that will contain list of all applied companies, their email, and the role your applying for, and its current status
- when submitting job applications usually there will be application fields like:
- attach your CV or resume
- Minimum salary. 50000php/$850 per month or 600000php/$10000 per month 

* so if I am to work in Pacific Standard Time? (dayshift), i.e. start time of work is 9:00am in the us what tiem would I work in the philippines?

If you're working a 9 AM to 5 PM Pacific Standard Time (PST) shift, considering the 16-hour time difference between PST and Philippine Standard Time (PST), your work hours in the Philippines would be:

9:00 AM PST = 9:00 PM PST (Philippines)
5:00 PM PST = 5:00 AM PST (Philippines, the next day)

So, you'd be working an overnight shift from 9:00 PM to 5:00 AM Philippine Standard Time.

Philippine Standard Time: Tuesday, Wednesday, Thursday at 9am-12pm and 1pm-5pm 



### Main techniques for applying to jobs
* Exhaust networking by messaging each of my classmates if a spot is open in their company, or if they have an email of their recruiter
* Go to *healthy gamer* discord server or *data engineering pilipinas* server and ask for websites where to apply for a software engineering job or any data related job
* Apply at the ff. job sites according to rank in terms of probability of success (list of websites are in `behavioral-interview-questions.md` file)
* Referral from colleague. This strategy you will message each of your remotely close colleagues and old classmates and see if they have their HRs email, and then email that HR regarding if there is an open position at their `<company name>` and that your `<friend or colleage who works at said company>` can vouch for your skills and accomplished projects
* cold emailing recruiters personally by using the *3 - AUTOMATED LETTER OF INQUIRY SENDER*, *4 - RECRUITER LINK & NAME SCRAPER*, and *5 - RECRUITER CONTACT INFO SCRAPER* in tandem.
* cold messaging recruiters on linked in personally usign other account with connections that are mostly recruiters and sending them the `cold_message_li.txt` template

* Notify recruiter that you've applied to them once done with applying via LinkedIn, Glassdoor, Kalibrr, or by the recruiters you've messaged asking you to apply to their company website, by doing the ff. steps: 
1. find a recruiter via the company you've applied to in any job application website by typing out the company seeing who works in the company, and then filter by job title specifically *HR*,
2. messaging that HR or recruiter immediately telling them you've applied for a `<role>` at their `<company>` e.g.  
`Hello and Good day Maam Edna I've answered the application form you've sent me, about the AI Engineer position. I also look forward to your response to me back. Best, regards.`

* with this you should always have your `generate_cover_letter` script always ready, and the `message body to professionals` document always ready which is part of `project Solzhenitsyn`, so you can move and apply quickly. This is a numbers game and it all depends hwo much input you put in during the day. Recall that `generate_cover_letter.py` usage requires `position` and `company` args

* use simplify chrome extension para di kana mahirapan mag manually fill up lagi ng application ddahil yung job details and experience you have like your projects work experience education skills etc. ito na ipprovide mo dito sa chrome extension na to para the next time you apply and you are met with a page with blank fields the simplify will use the work information you provided and use it to autofill the fields mostly if not all so you don't hae to do everything from scratch. https://simplify.jobs/

* if you apply to job websites make sure you are not willy nilly applying without ever considering when was the job posted, how much applicants are there, and whether the recruiter or not is indeed active. To do this you need to enable strict filtering. Some filters you are to apply in the search engine will be the following based on possible roles you may have like *Data Engineer*, *Machine Learning Engineer*, *Software Engineer*, *Python Developer*, *AI Engineer*, *Data Scientist*, *Software Developer*, etc.
1. `date posted` must be in the range of either `past month`, `past week`, or `past 24 hours` in order to avoid ghost jobs
2. `experience level` can be any
3. `company` can be any
4. `remote` will either be onsite and hybrid
5. don't check easy apply because this significantly minimizes pool of potential jobs just because they don't have easy apply and you have to apply to their company website directly and fill out long fields etc. NO. Meron ka naman `simplify.jobs` at your disposal which we can assume you already filled up para pagdating dito mag auautofill ka nalang ng fields na meron sa company website na ito, thus making workflow 10x faster
6. take advantage of the url
- `f_TPR` query parameter can take on values `r2592000`, `r604800`, and `r86400` symbolizing the `past month`, `past week`, and `past 24 hours`, values for the `date posted` filter. HOWEVER we can virtually use this at our disposal and edit the number value to a much shorter one because this number of value is essentially the number of seconds since a job must be posted and in this case *2592000 seconds* is 1 month, *604800* is 1 week, and *86400* is 1 day. With this understanding we can manipulate it to our advantage and set it to the time frame we want since the job msut be posted meaning the shorter our chosen time frame i.e. 30 minutes, 20 minutes, 10 minutes, or even 5 minutes since the job our posted the less competition we will have in our job application. If we want a time frame of 30 minutes since the job was posted we need only convert 30 minutes to seconds using some kind of app or you could just google search it and know i.e. 30 minutes is 1800 seconds, and so we can replace the value of the f_TPR parameter to r1800 (note the `r` must always precede the number of seconds). Once we enter this in the address bar we will get results of all jobs we want that have been posted 30 minutes ago. Custom time frames we can choose from to ensure less competition could be 43200 (12 hours), 39600 (11 hours), 36000 (10 hours), 32400 (9 hours), 28800 (8 hours), 25200 (7 hours), 21600 (6 hours), 18000 (5 hours), 3600 (1 hour), 1800 (30 minutes), 1200, 600, 300
- `keywords` query parameter can be another important parameter as this can filter out the jobs we want by assigning it values like the ff:
* `data%20engineer`
* `machine%20learning%20engineer`
* `data%20scientist`
* `software%20engineer`
* `software%20engineer`
i.e. if we want a data engineer job that has just been posted 30 minutes ago we can have the `f_TPR` value be `r1800` and the `keywords` value be `data%20engineer` (`%20` is denotes a whitespace). Thus the full URL would be https://www.linkedin.com/jobs/search/?currentJobId=4138965537&f_TPR=r1800&f_WT=1%2C3&geoId=103121230&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true
* `junior%software%engineer`, `junior%data%engineer`, `junior%machine%learning%engineer`,
* the main filter you need to have is that it must be and kilangan junior role, a data/software/machine learning/data scientist engineer/developer, 30000php per month as base pay after tax, onsite or at least hybrid, around pasig, taguig, mandaluyong, ortigas, quezon city (except commonwealth), dayshift, 9-5  

7. post resume/cv on linkedin account with connections that are mostly recruiters. With the caption 
```
"This is my first time posting in a long time

but from a hiring manager or recruiters perspective what would a fresh graduate trying to land a junior data analytics role have to add or remove in this resume/CV

I created this using Canva so do you think it will grab recruiters attention? Any feedback would be appreciated.

If you need an editable version of this resume and create one for yourself you can comment your email id below. I'd be happy to share it with you.

#canva #jobsearch #recruitment #software #dataanalytics #jobhiring #jobseeking"
```
this post will as byproduct give you potential recruiters giving you potential opportunities to apply for the role you are looking for when they comment on your post

8. seaarching for posts by recruiters instead of jobs 
- search on linkedin for instance the keyword "software engineer" and add the "recruiter" keyword. The search results will give a list of recruiters possibly hiring for this role you typed as a keyword. Go to their linkedin profile connect with them and they probably have a recent post asking their connections to send them their CV for the role you want. 
- another way you could search for a role that's potentially hiring and where there is less competition is by searching on LinkedIn for instance the keyword "software engineer", the keyword "AND" (in all caps), and the keyword "hiring", which all in all is "software engineer 

9. testing out if CV/Resume will go through a sample ATS (application tracker system) that's more likely than not operated by AI. To do this go to https://app.jobscan.co/ and upload your resume and cv. It will ask you what role are you trying to go for e.g. data engineer, machine learning engineer, or what job description you have where you can supply its field e.g.

```
The Data Engineer is responsible for the creation, maintenance, and continuous improvement of data pipelines. Part of the responsibilities is to implement best practices in data management practices (i.e., cleaning, validation, and transformation of data) and make data into usable datasets that can easily be consumed by other teams.

What you will do:

Work on existing data pipelines, including development of data models, and data management may it be in a data warehouse, data/delta lake or lakehouse. Collaboratively work with upstream teams that pass data to the data architecture and with downstream teams that use data within it.
Helps in the maintenance of the overall data architecture, ensuring its scalability, high availability, on-time data ingestions, and ensuring operations are not disrupted.
Build data pipelines as new data comes in, applying best practices and DataOps principles.
Acquire and maintain an in-depth domain knowledge of the data within the assigned scope. This domain knowledge is crucial in the creation of data models and development of the said data models for Zone 2 and Zone 3 data (a.k.a. silver and gold layer, respectively). This expertise ensures that DE-transformed business datasets are usable for downstream teams.

What we are looking for:

BS or MS in Computer Science or equivalent
Proven years of experience with Data Engineering roles focusing on Data Architecture, Data Management, and DataOps practices
Has relevant experience in data modelling
Has good working knowledge on Shell (e.g. bash, zsh) scripting
Has good working knowledge on data manipulation (SQL statements, JSON, NOSQL query, etc.)
Has good working knowledge on AWS services (EC2, S3, Glue Crawlers, Jobs, Batch, Athena, Lambda, etc.) or equivalent cloud offerings a big plus
Has good working knowledge on Apache Spark using SQL/Python
Has good understanding of the concepts of Datawarehouse, Data Lake/Delta Lake and/or Lakehouse
Has good knowledge on Linux/Unix Administration
Has good working knowledge on data modeling
Able to work with other Leads to foster a culture of collaboration and teamwork
CI/CD experience using Terraform is a huge advantage
Experience working with Amazon Web Services / Cloud is a big plus
```

Once you scan the jobscan application will tell you the results of whether your CV passed the hypothetical ATS. If it didn't it will tell you what keywords you should add more to your CV based on the specified job description or just the general description of the role you're going for i.e. data engineer.

In your case missing keywords were Data Architecture, Unix Administration, Amazon Web Service. Other issues like searchability jobscan can give you an insight to, in this case a tip could be adding the address on top of your CV

10. so mas aligned ako sas data scientist role kasi marunong ako magprototype pero hindi magdeploy ng model in the real world

automated training of model done by ml engineer, automated extraction of data into cleaner data done by data engineer, but a data scientist does the prototyping first like yung transformation, preprocessing, dito siya marunong sa mga libraries, like tensorflow, pytorch, pandas, scikitlearn, matplitlib dito ka marunong, marunong ka sa prototyping

pero kung may live data hindi na dapat dumadaan na to sa jupyter notebooks o scripts na ginawa mo to train a model but to automate continuous training and continuous deployment at dito na kilangan na ng cloud services like aws azure, gcp to make these continuous integrations and deployments 

keywords for ML engineer: Azure, Ops, AWS, redshift, 

AI Engineer: LLM, GenAI, 

Junior Data Scientist: Scitkit-Learn, Hypothesis Testing, Exploratory Data Anlysis, SQL, Python, Tensorflow, 0-2 years experience, ad hoc, powerBI or tablaeu ()

banks have more junior data scientist role or data scientist intern. Philippine National Bank, Chinabank, Landbank, security bank, asian development bank, rizal commercial banking corps., union bank, banco de oro, 

for powerBI, kuha ka dataset na relevant sa domain mo like finance, healthcare, etc. 

eitheer client based or project based

kung puro excel sheet pa ang company, use power apps to migrate the excel sheet there, and devs can access their excel data from power apps

* after applying reach out to hiring manager or recruiter
* Di pwede nakabuklat lahat ng projects mo, you need to allow for some mystery at least and reveal it through your portfolio website

11. reach out to top data analysts in the field. Hindi uubra yung selling yourself and marketing yourself because it comes across as disingenious, instead talk to them like a normal human being trying to know genuinely what it takes to stand out as a data analyst, tell them the projects you've made and what you can improve, what data you can use next time, what data sources you can pool from next project etc. **If you ask for a job you get time and if you ask for time you get a job (through referrals)**.

12. the heirarchy of job applications from bottom to top according to I believe their interview conversion rate (probability that applying will lead to at least an HR phone interview) are the following:
* Tier 1:
- Applying on linked in using url technique e.g. https://www.linkedin.com/jobs/search/?currentJobId=4138965537&f_TPR=r1800&f_WT=1%2C3&geoId=103121230&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true making sure time elapsed since job posting is 12 hours or less makign sure competition is left out 
- indeed for some reason has landed me more calls so its part of this tier
- using job boards of company websites and applying to them directly. The way you do this is list companies you see on linkedin, usually big names or companies that have websites (usually a website is a good indication that the company is starting out in its data maturity)

* Tier 2:
- kalibrr
- jora jobs
- jobslin
-