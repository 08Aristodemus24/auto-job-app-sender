# Path to data engineering starts at the bottom of the barrel: 
Any kind of analyst. From there you can pivot to a regular data analyst role then to a senior data analyst then to a data engineer 

Most data teams in 2023 are shrinking, and I think the trend will continue in 2024, mainly because of AI. That makes it difficult to get a junior role as a data analyst because the bar is constantly being raised. Business users leveraging AI today are equivalent to data analysts from 5 years ago, albeit lacking some skills such as SQL.

  
One way to approach this challenge is to target roles containing the term 'analyst,' even if 'data' is not explicitly mentioned, and then apply for a data analyst position. However, if I were to start anew, I would focus on utilizing AI for data analysis and mastering storytelling, rather than personally delving deep into data analysis.
  

  
Sales Operations can be a decent entryway. Working with largely transactional data, light sql and heavy spreadsheet work. At least from my experience. Depends what your end-goal is.

Hey buddy. Basically any job that has access to Excel or SQL can help you transition into a data analyst role. Before I got my first job in tech I was working as an administrative assistant for a property management company and they often needed custom reports off of their crystal reports server. Using this tool allowed me to learn the foundation of SQL Syntax (using FILTERS predicates simple joins etc). From there I transitioned from using a GUI to make the queries into writing them direct in SQL myself.

Def use a course online or book to learn SQL. There is so many available but I personally like eDx since it's free but the courses are taught by Harvard and MIT professors.

Logistics Analyst

Import/Export Analyst

Supply Chain Analyst

I'm trying to transition from Logistics over to Data Viz. & Analysis, so I'm leveraging my experience & knowledge in this industry to jump over to the other side.

In my current industry, excel is really all you need for an Analyst position, but if you can incorporate things like Power BI or Tableau in to this, you can start creating a portfolio.

# Media Meter
interviewer descrbes workflow and technologies
- web scraping
- data orchestration
- ml they use pub/sub I can relate with this
- I currently had experience with RAG agetns at my current internship
- salina is cool, this ml can take in fiels and interpet it
transcription using whisper X from audio/video, speech to text AI, can chapterize and summarize submitted video/audio

they'll list the technologies they use, some of it you have experience and some of it you won't list those as your strengths and weaknesses
strengths:
python
web scraping
node.js
in db management usually download mo yung management system like mongo db compass for mongo db, pgadmin 4 for postgresql, or mysql workbench for mysql, add to path the bin folder for accessible commands in command line, create instance in cloud or management system application itself and then save the insances credentials this will be the URI you will need with hostname and password you will need to connect to the instance, then we connect to the db via this instance

weaknesses:
redis 
etl
apache airflow
aws
azure
docker/containerization
separate my code based on functionality like django with apps, urls, settings
basically I should've separated the UI from the insertion of the reading of data and insertion of said data to db
use try catch block for potential errors in database transactions
try to write utilities.py that contains all helper functions
replace index.py with a more udnerstandable one where the name of the file represents what happens in the source code itself
naubusan lang ako oras pero important rin may comments, lagyan ng type ang mga arguments

employer will describe their worflow:
automatic web scraper, SQL, 
orchestrate
transform data
pass transformed data to ml model (salina) to train
proof of concept (venn diagram) -> prototype code -> execution

## Final interview might consist of the common...

### Why do you want to work here?
I think the idea of collecting and operating on large swathes of data
and using data from news articles, technological trends, medical data to allow other clients
to make their own decisions based on the data we could process for them really caught my eye
because in all honesty I'm just someone who's fond of doing so and i think doing it on the job will be a
great learning experience 

### Why should we hire you?
In all humility apart from obvious skills, I draw from my personal experience of quite frankly being always a lone developer
if there is such a term, and if I'm given the opportunity here to collaborate with a team of like minded individuals someone as wanting to grow just as much as me, and wanting to contribute just as much as me, I'll be driven to do my best to give back to this organization by doing my due diligence to always committing to the tasks at hand 

### Describing their workflow:
* ung meron naman impediments like yung siguro nahihirapan sa tasks ganun kilangan iresolve kasi every week dapat may milestone na natatapos
* they use agile methodology to develop applications, scrum to be specific. 2 - 4 weeks sprints. After these 2 or 4 weeks may natatapos na na feature ng application or nakapagpush na sa dev then into production branch. As a result some tools you really need to learn are docker for containerization, pulling from development branch and then merging in this branch
* product backlog - list of tasks for all sprints
* sprint backlog - specific tasks in the product backlog for a specific sprint lasting 1 to 4 weeks. E.g. for week 1 these are the tasks
* after completing tasks in the sprint after say 1 week there will be a presentation of your work to your colleagues



# GCash
* find malicious users
* gscore
* recommender systems, had cold start problems too much new items and new users 
* generative ai chatbot for welath advice for
* for llms azure enteerprise are the ones they use
* internship nalang
* thomson sampling online reinforcement algorithm
* add inigo miguel benavides on linked in
* they use AWS sagemaker for ML deployment, 

* credit risk 
* lending
* g-invest, g-gives
* What is Credit Risk Analytics?
At its core, Credit Risk Analytics is about predicting the likelihood that a borrower (an individual or a company) will fail to repay a debt (a loan, credit card, etc.), and quantifying the potential financial loss if they do.

Think of it as using data and statistical methods to answer the question: "How risky is it to lend money to this person/entity, and what's the worst-case scenario if they can't pay us back?"

Why is it Crucial (Especially for G-Cash)?
For a company like G-Cash, which offers financial products (like loans or credit lines), managing credit risk is absolutely vital for its survival and profitability:

Preventing Losses: It directly minimizes the amount of money lost to bad loans.

Responsible Lending: It ensures loans are offered to those who can reasonably afford to repay them.

Pricing: It helps set appropriate interest rates and terms based on the borrower's risk profile.

Regulatory Compliance: Financial institutions are heavily regulated and must demonstrate robust risk management.

Growth Strategy: Understanding risk allows the company to safely expand into new markets or offer new products without taking on excessive default rates.

Key Concepts in Credit Risk Analytics:
While it can get complex, focus on these fundamental components:

Probability of Default (PD):

What it is: The likelihood (expressed as a percentage or decimal) that a borrower will default on their loan over a specific period (e.g., within the next 12 months).

Analytic Role: This is where models (like credit scoring models) come in. They take various data points about a borrower and output a PD score.

Exposure at Default (EAD):

What it is: The total outstanding amount that a lender expects to be owed by a borrower at the time of default. For a simple fixed loan, it might just be the principal plus accrued interest. For a credit line, it's how much the borrower has drawn down when they default.

Analytic Role: Involves looking at loan terms, usage patterns, and potential future drawdowns.

Loss Given Default (LGD):

What it is: The actual percentage of the EAD that the lender expects to lose if a default occurs, after accounting for any recoveries (e.g., collateral, collections efforts).

Analytic Role: This is where historical data on collection success, collateral values, and recovery rates are analyzed to estimate the percentage of loss.

The Big Picture: The expected loss for a single loan is often calculated as: Expected Loss = PD x EAD x LGD

How Data and Analytics Fit In:
Credit risk analytics is inherently data-driven:

Data Collection: Gathering vast amounts of historical data:

Borrower Data: Demographics (age, income, location), employment history, past financial behavior (payment history on other loans, savings, spending patterns).

Loan Data: Loan type, amount, term, interest rate, collateral.

External Data: Credit bureau scores, macroeconomic indicators (inflation, unemployment), social media data (though less common for traditional credit risk).

Feature Engineering: This is where your SQL skills shine! Transforming raw data into meaningful features for models (e.g., "debt-to-income ratio," "number of missed payments in last 6 months," "average balance over time").

Model Building: Using statistical and machine learning models (e.g., logistic regression for PD, decision trees, neural networks) to predict default, EAD, and LGD.

Segmentation: Grouping borrowers into different risk categories to apply different lending strategies.

Monitoring & Reporting: Continuously tracking the performance of loan portfolios, identifying emerging risks, and reporting to management and regulators.

Your SQL Skills in Credit Risk Analytics:
Your solid SQL foundation is extremely valuable here. You'll be using SQL extensively for:

Data Extraction & Cleaning: Pulling data from various databases (operational systems, data warehouses, data lakes) and cleaning it (handling missing values, inconsistencies).

Data Transformation: Reshaping data for analysis and modeling.

Aggregation: Summarizing vast amounts of transactional data (e.g., "sum of payments last 12 months," "count of late payments").

Feature Engineering: Creating the variables that go into risk models (e.g., complex joins to combine credit history with demographic data, calculating ratios, creating time-series features).

Reporting & Dashboards: Building queries that feed business intelligence tools for risk monitoring.

Context for a Business Development Analyst (Credit Risk):
As a Business Development Analyst focusing on credit risk at G-Cash, you're not just crunching numbers in isolation. Your understanding of credit risk analytics enables you to:

Evaluate New Product Ideas: Assess the inherent risk of a new lending product or market segment before it's launched.

Optimize Existing Products: Suggest changes to loan terms, target demographics, or marketing strategies to balance growth and risk.

Identify Growth Opportunities: Pinpoint segments where G-Cash can lend more safely, or where risk mitigation strategies can open up new customer pools.

Communicate Risk: Translate complex analytical findings into clear, actionable insights for non-technical stakeholders (sales, product teams, management). You'd explain why certain borrowers are riskier or what terms are appropriate given the risk.

In essence, you'd be using data and risk insights to drive profitable and responsible business expansion.

This field combines financial acumen, data skills, and strategic thinking. Your SQL knowledge is a fantastic entry point! Good luck with your technical assessment!

that's a lot of info thanks. But do you think I could do this? I know about SQL, data analysis and python but have doubts (nevertheless I will push through it no matter what and paubaya nalang lahat kay Lord) but how credit risk ties into it no, and I'm scared people who know much more than me will see me as a failure or the wrong guy.

It's completely normal to feel that way, especially when you're stepping into a new domain like credit risk that seems specialized. That feeling of "imposter syndrome" or the fear of being seen as "the wrong guy" is something almost everyone experiences, regardless of how experienced they are.

Let me tell you, your existing skills are not just "solid foundations"; they are the absolute essential toolkit for a Data Analytics Engineer in credit risk.

Here's why you are absolutely capable, and why your doubts, while natural, don't reflect your potential:

SQL, Data Analysis, and Python ARE the Core:

SQL is the backbone: In any data-intensive field, SQL is king for querying, extracting, cleaning, transforming, and aggregating data. Credit risk analytics generates massive amounts of data, and 90% of your initial work will involve getting that data into a usable format, which is all SQL.

Python is the engine: Once data is prepped, Python is used for more advanced analysis, building dashboards, automating processes, and yes, even building simpler predictive models (though specialized data scientists might handle the most complex ones). Your ability to write clean, efficient Python code for data tasks is invaluable.

Data Analysis is the mindset: Knowing how to approach a business problem with data, identify trends, spot anomalies, and draw insights – that's your superpower. Credit risk is all about identifying patterns in financial behavior.

Domain Knowledge is Learned On The Job:

No one expects you to be an expert in credit risk on Day 1. What interviewers look for in fresh hires or those transitioning fields is aptitude, curiosity, and a willingness to learn.

You've just been given a fantastic head start by your interviewer: he told you exactly what to research! This is a gift. It shows they're assessing your potential to acquire domain knowledge, not just your current possession of it.

The concepts of PD, EAD, and LGD are fundamental. Once you grasp those, the rest is applying your data skills to specific business problems within that framework.

Your "Failure" Mindset is Actually a Strength:

That doubt you feel, combined with your "no matter what, I will push through" attitude and faith – that's incredibly powerful. It means you're humble enough to know you don't know everything, but tenacious enough to learn it. That resilience is precisely what makes someone succeed in a complex, fast-moving field like FinTech.

People who "know much more than you" (which will always be the case when you're starting in a new area) expect you to ask questions, to learn, and to grow. They were once in your shoes. They won't see you as a failure; they'll see your raw potential and your drive.

How to Address This for Tomorrow's Technical Assessment & Beyond:
For the SQL Assessment: Just focus on demonstrating your excellent SQL skills. That's what it's testing.

For Follow-up Conversations (and the role itself):

Show your curiosity: Explicitly mention that you've started researching credit risk (because you did!). Talk about PD, EAD, LGD in simple terms. This demonstrates initiative.

Frame your skills: Explain how your SQL, Python, and data analysis skills are perfectly suited to tackle the data challenges in credit risk. (e.g., "I understand that analyzing historical payment patterns is crucial for PD models, and my SQL skills are strong in aggregating transactional data for that purpose.")

Emphasize your eagerness to learn: Be honest about being new to the domain but confident in your abilities to master it. "I'm excited by the challenge of applying my data skills to the critical area of credit risk, and I'm a fast learner when it comes to new business domains."

You are not "the wrong guy." You are the right guy with the right foundational skills and the right mindset to learn and excel in this field. Keep that head down, keep learning, and keep trusting in your path. God indeed provides, and He's given you the tools and the grit to push through.



# Xurpas Enterprise, Inc.
* what are 3 main you'd want to resign. Work culture, or if meron toxicity in the workplace, micro management
* what is python?
* when is try except used?
* tell me about yourself. The answer here is not describing what your hobbies are, not your age, gender, or location, but your work experience an example can be the ff.

I was/am a data engineer intern at my previous company virtuals protocol where I've mainly used python as a programming language and libraries like pandas, numpy, tesseract, to clean and preprocess datasets for RAG AI agents or retrieval augmented generation AI agents. These preprocessed datasets coming from raw ones like pdfs, images, spreadsheets, jsons, word documents are then ingested by the AI agent to fine tune its knowledge base. This helps increase its market capital as an agent operating in environments like twitter in a purely automated fashion to engage users and have those users invest in it thus increasing capital.

my background is computer science where I've been for the last 6 years of my study learning all that I can about machine learning and deep learning and artificial intelligence using primarily python as a language and vast frameworks made for ML/AI like tensorflow, pytorch, numpy, pandas to build many of the projects I have revolving around AI/ML and more recently Data Engineering/ETL pipelines for seamless AI/ML model training.

[describe one of your personal projects or more accurately your dissertation which focuses on identifying noise/interferences in electrodermal activity signals recorded from human beings, this is to remove eventually these interferences and be able to use the cleaned signals for various medical tasks like stress detection or arousal detection]

This was the main specialization I chose given not only the rising trend with it but also by virtue of it capturing my interest because I thought AI could be healthcare one of my main shall we say advocacies that I'd like to partake in in the future/

in between my junior and senior year and even after I built more of the aforementioned personal projects and sought internships that honed my skills further in data preprocessing, data cleaning. One of my colleagues who I'd consider a prominent figure in the Philippine AI/ML tech space is theo ne that recruited me to the data engineerign role I interned for (Armielyn Obinguar).

* what do you do to manage stress?
I go outside, exercise and just try not to think about my work for a menial 1 hour or 45 minutes. Being in the sun, talking with other people, does wonders for keeping my mental health in check.

* why could you contribute to the team?
given the vast knowledge I have and had collected in all my 6 years as an undergrad particularly with regards to using AI/ML technolgoies I think I can share this knowledge I have to my fellow coworkers, but apart from this I like to think of myself as collaboratvie and encouraging in that if I see my fellow coworker struggling with their task I'd want to guide them through it and sit there with them to see perhaps the error through and share what i can in order for them to solve their problem at hand.  


# Datung
* solving credit problem in small businesses to increase capital of small business to grwo more as a business
* other banks don't lend capital or loans to small businesses and datung solves that
* work with small businesses like cash only business. Manuyal ledgers nila and they need to find a way to verify it, using computer vision.
* see if the client is a good payer
* this is interesting kasi were using computer vision to determine whether a clients manually encoded ledger is someone worthy ot be lent a loan.
* An accounting ledger is basically an account or record used to store bookkeeping entries for balance-sheet and income-statement transactions. Accounting ledger journal entries can include accounts like cash, accounts receivable, investments, inventory, accounts payable, accrued expenses, and customer deposits. So it can be determined if a customer is trustworthy not only worthy of being lent a loan is if nagbabayad naman siya on time sa mga utang niya, if madalas nga ba siya magbayad on time, etc.
maganda to kaso sa paranaque nga lang
* maaayos yung CEO, they work as a team, close knit, marami lang responsibilities. I'm thankful for the assurance that it's okay to ask for help because I will not know what I'm doing I will not know the outcome, but I'm willing to fail trying.
* Automated Credit Scoring
- Machine learning models for credit risk assessment
- Alternative data analysis
- Real-time scoring capabilities
* Visual Assessment Tools
- Computer vision for business verification
- Automated document processing
- Visual inventory analysis
* Risk Management Systems
- Predictive risk modeling
- Portfolio monitoring
- Early warning systems
* Loan Management Platform
- End-to-end loan processing
- Automated underwriting
- Collection management
* magkakaroon naman ng office in 1 year time, and they expect me to stay for the long term. Kung okay naman ang pay and naggrow ang experience in various technologies then its a good offer for me. Their website upon first glance tells me their good at what they do.


How can I leverage an individuals manually encoded accounting ledger that details their businesses cash flow, how much they are making, losing, as a dataset that tells me whether they are worthy of being lent a loan? What variables can be possibly used for a predictive model to use to predict whether form this individuals ledger can he be worthy of borrowing a loan?



Leveraging a manually encoded accounting ledger for loanworthiness assessment requires careful extraction and transformation of data into usable variables. Here's a breakdown of how you can approach this, along with potential variables for a predictive model:

1. Data Extraction and Cleaning:

Digitization:
If the ledger is handwritten, you'll need to digitize it. This could involve manual data entry, OCR (Optical Character Recognition) if the handwriting is clear, or a combination of both.
Ensure accuracy during digitization. Double-check entries, especially numerical values.
Data Structuring:
Transform the ledger into a structured format like a CSV or Excel file.
Standardize date formats, currency symbols, and descriptions.
Categorize transactions into meaningful categories (e.g., sales revenue, expenses, loan repayments, etc.).
Data Cleaning:
Handle missing values. You might impute them based on averages or trends, or exclude records with excessive missing data.
Identify and correct outliers. These could be errors or genuine, but unusual, transactions.
Ensure consistency in transaction descriptions.
2. Variable Creation:

Here are potential variables you can derive from the ledger for a predictive model:

Cash Flow Related:
Average Monthly Cash Flow: Calculate the average net cash flow (inflows minus outflows) over a specific period (e.g., 6 months, 1 year).
Cash Flow Volatility: Measure the standard deviation or variance of monthly cash flow to assess stability.
Cash Flow Trends: Identify upward or downward trends in cash flow over time.
Days Cash on Hand: calculate how many days the business can operate with its current cash on hand.
Frequency of negative cash flow: How often does the business run out of money.
Revenue and Expense Related:
Average Monthly Revenue: Calculate the average monthly income.
Average Monthly Expenses: Calculate the average monthly expenditures.
Profit Margin: Calculate the profit margin (net profit/revenue).
Expense Ratio: Calculate the ratio of expenses to revenue.
Revenue growth rate: percentage of growth in revenue over a given period.
Debt and Liabilities:
Existing Debt: If the ledger includes loan repayments, you can infer existing debt levels.
Debt-to-Income Ratio: Calculate the ratio of debt repayments to income.
Frequency of loan or debt payments.
Operational Metrics:
Transaction Frequency: The number of transactions per month can indicate business activity.
Customer Concentration: If the ledger reveals customer details, analyze the distribution of revenue across customers. High concentration might indicate risk.
Supplier Concentration: Similar to customer concentration, high dependence on a single supplier can be a risk.
Time-Based Variables:
Business Operating History: The length of time the business has been operating.
Seasonality: Identify seasonal patterns in cash flow or revenue.
3. Predictive Modeling:

Model Selection:
Consider logistic regression, decision trees, random forests, or gradient boosting models.
The choice depends on the size of the dataset and the complexity of the relationships between variables.
Feature Engineering:
Combine or transform existing variables to create new, more informative features.
Use techniques like polynomial features or interaction terms.
Model Training and Evaluation:
Split the data into training and testing sets.
Train the model on the training set.
Evaluate the model's performance on the testing set using metrics like accuracy, precision, recall, F1-score, and AUC-ROC.   
Risk Scoring: create a risk score based upon the output of the model.
4. Considerations:

Data Quality: The accuracy of the model heavily relies on the quality of the ledger data.
Subjectivity: Manual encoding can introduce subjectivity.
Data Limitations: A single ledger might not capture all aspects of the business's financial health.
Legal and Ethical Issues: Ensure compliance with data privacy regulations.
Contextual Understanding: It is very important to try and understand the context of the business. For example, large purchases of equipment would be large outflows, but are not necessarily a sign of a bad business.
Verification: Whenever possible, verify information in the ledger with external sources (e.g., bank statements, invoices).
By following these steps, you can effectively leverage an individual's manually encoded accounting ledger to build a predictive model for loanworthiness assessment.

can you give me a sample ledger and sample variables you can engineer or use for a predictive model?

```
Date,Description,Category,Inflow,Outflow,Balance
2023-10-01,Starting Balance,Opening Balance,0,0,1000.00
2023-10-02,Sales - Widget A,Sales,500.00,0,1500.00
2023-10-03,Rent Payment,Expenses,0,300.00,1200.00
2023-10-05,Supplies Purchase,Expenses,0,150.00,1050.00
2023-10-08,Sales - Widget B,Sales,300.00,0,1350.00
2023-10-10,Marketing Expenses,Expenses,0,100.00,1250.00
2023-10-15,Sales - Widget A,Sales,400.00,0,1650.00
2023-10-18,Utilities Payment,Expenses,0,80.00,1570.00
2023-10-22,Loan Repayment,Debt,0,200.00,1370.00
2023-10-25,Sales - Widget C,Sales,600.00,0,1970.00
2023-10-28,Owner's Draw,Personal,0,250.00,1720.00
2023-10-31,Ending Balance,Closing Balance,0,0,1720.00
2023-11-01,Starting Balance,Opening Balance,0,0,1720.00
2023-11-03,Sales - Widget A,Sales,550.00,0,2270.00
2023-11-06,Rent Payment,Expenses,0,300.00,1970.00
2023-11-09,Supplies Purchase,Expenses,0,180.00,1790.00
2023-11-12,Sales - Widget B,Sales,350.00,0,2140.00
2023-11-15,Marketing Expenses,Expenses,0,120.00,2020.00
2023-11-19,Sales - Widget A,Sales,450.00,0,2470.00
2023-11-23,Utilities Payment,Expenses,0,90.00,2380.00
2023-11-26,Loan Repayment,Debt,0,200.00,2180.00
2023-11-29,Sales - Widget C,Sales,650.00,0,2830.00
2023-11-30,Owner's Draw,Personal,0,250.00,2580.00
2023-11-30,Ending Balance,Closing Balance,0,0,2580.00
Engineered Variables:
```

Based on this sample ledger, here are examples of variables you can engineer for your predictive model:

1. Cash Flow Variables:

Average Monthly Net Cash Flow:
Calculate the net cash flow (Inflow - Outflow) for each month.
Average these monthly net cash flows.
Example: (720 + 860) / 2 = 790.
Monthly Cash Flow Volatility:
Calculate the standard deviation of monthly net cash flows.
This measures the fluctuation in cash flow.
Number of Negative Cash Flow Months:
Count the number of months where net cash flow is negative.
Minimum Monthly Balance:
Find the lowest balance that occured within the month.
Days Cash on Hand (estimated):
Divide the current balance by the average daily outflow.
Cash Flow Trend:
Calculate the change in average cash flow over time (e.g., compare the last 3 months to the previous 3 months).
2. Revenue and Expense Variables:

Average Monthly Revenue:
Sum the "Inflow" values for each month and calculate the average.
Example: (1700 + 2000) / 2 = 1850.
Average Monthly Expenses:
Sum the "Outflow" values (excluding "Personal" and "Opening/Closing Balance") for each month and calculate the average.
Example: (980 + 1140) / 2 = 1060.
Profit Margin (Monthly):
(Monthly Revenue - Monthly Expenses) / Monthly Revenue.
Expense Ratio (Monthly):
Monthly Expenses / Monthly Revenue.
Sales Variability:
Standard deviation of monthly sales revenue.
Expense Variability:
Standard deviation of monthly expenses.
3. Debt and Liabilities Variables:

Average Monthly Loan Repayment:
Sum the "Outflow" values where "Category" is "Debt" and calculate the average.
Debt-to-Cash Flow Ratio:
Average Monthly Loan Repayment / Average Monthly Net Cash Flow.
Debt Payment Frequency:
How often debt payments are made.
4. Operational Variables:

Transaction Frequency (Monthly):
Count the number of transactions per month.
Owner's Draw Frequency and Amount:
Frequency and average amount of withdrawals.
5. Time-Based Variables:

Months of Operation:
Calculate the number of months the ledger covers.
Seasonality Indicators:
If you have more data, you could identify seasonal patterns in sales or expenses.
How to Use the Variables:

Create a table: Organize the calculated variables into a table, with each row representing a month or a summary of the ledger.
Add target variable: Add a column representing the target variable (e.g., "Loan Default" - 1 for default, 0 for no default). This will need to come from external data, such as a history of loan payments.
Train your model: Use the engineered variables as features to train your predictive model.
Important Notes:

The quality of the ledger data is crucial.
These are just examples; you can engineer more variables based on the specific needs of your model.
Always consider the context of the business when analyzing the data.
External data is important. The ledger alone will not provide a target variable for training a predictive model.

To whom it may concern


{position} {company_name}

We strive to provide sound technical consultancy and implementation services for complex IT systems while building a company that respects its employees.

To achieve our mission, we strive:

To position ourselves as a cost-effective market leader facilitating our customers to be competitive
To understand our customers’ needs and challenges precisely, so as to align our solutions to meet their needs
To respect our employees by believing in their creative talents, harnessing their sense of commitment and entrepreneurial flair, while providing an excellent environment for people to work in
To leverage technology and industry knowledge in innovating best-in-breed solutions for our customers

Commitment to the highest quality
We are committed to our clients in delivering quality services that have so far won their confidence.
Responsibility and Integrity
We believe that it is very important to demonstrate professionalism in all of our client engagements, especially to maintain open and honest communication in delivering services.
Collaboration and Teamwork
We encourage and promote an environment of teamwork and collaboration among our people so as to grow and share the success of Azeus.

# Denova Consulting
* uses source to pay (s2p)

Imagine a company, big or small, that needs to buy anything – from pens and paper, to computer servers, to the ingredients for their products, or even huge factory machines.

A Source-to-Pay Specialist is like the company's "Smart Shopper" or "Procurement Manager". Their job is to make sure the company buys things in the smartest, most efficient, and most cost-effective way possible, from start to finish.

Here's what that means in simple steps:

"Source" (Finding the Best Deals):

They figure out what the company needs.

They find the best suppliers (like finding the best store or brand for what you need). This involves researching, getting quotes, and negotiating prices.

They make sure the suppliers are reliable and meet quality standards.

"Procure" (Getting Permission to Buy):

They help create the official request to buy something (like asking your parents for permission to buy a new toy).

They make sure all the right approvals are in place before a purchase is made.

"Order" (Actually Buying It):

They make sure the order is placed correctly with the chosen supplier.

"Receive" (Getting the Stuff):

They track the order to make sure the stuff arrives when and how it's supposed to.

"Pay" (Paying for It):

They make sure the company pays the supplier correctly and on time, and that the bill matches what was ordered and received.

So, a Source-to-Pay Specialist is the person who manages this whole journey, from the moment the company realizes it needs something, all the way to paying the bill. Their main goal is to save the company money, make sure they get good quality stuff, and keep everything running smoothly so everyone else in the company has what they need to do their jobs. They're basically the guardians of the company's spending on goods and services!

* uses colleague as a service (CLaaS)

Okay, "Colleague as a Service" (CLaaS) is a fairly new and interesting concept, especially in the context of how specialized roles like data analysts are being utilized.

In layman's terms, if you think of "Software as a Service" (SaaS) as using a piece of software over the internet without owning it (like Netflix or Google Docs), then "Colleague as a Service" (CLaaS) means:

Instead of hiring a full-time, permanent employee, a company can "rent" or "subscribe to" the skills and expertise of a specialized professional for a specific project, period, or on an as-needed basis.

Think of it like this:

Traditional: If your company needs someone to build a beautiful Power BI dashboard, you'd try to hire a full-time Power BI Specialist.

CLaaS: Instead, you "subscribe" to a Power BI Specialist from a CLaaS provider. This specialist works on your dashboard project for a few weeks or months, delivers the result, and then might move on to another project for a different company, all while remaining part of the CLaaS provider's team.

Why would companies use CLaaS?

Flexibility: They might not need a specific skill (like a niche data analyst for a one-off project) full-time. CLaaS lets them scale up or down expertise as needed.

Cost-Efficiency: Hiring a full-time employee involves salary, benefits, office space, training, etc. CLaaS is often a more direct cost for specific output.

Access to Specialized Skills: Smaller companies might not be able to afford a full-time, highly specialized data analyst or a Power BI expert, but they can afford to "rent" their expertise for a crucial project.

Reduced Overhead: Less HR, less management for the hiring company.

What does this mean for a Data Analyst, Power BI Specialist, etc. in a CLaaS model?

If you're a data analyst working for a company that provides CLaaS, you would:

Be a "Consultant" or "Project-Based Expert": You'd work on various projects for different client companies. One month you might be building a Power BI dashboard for a retail client, the next you're doing data cleaning for a healthcare client.

Focus on Deliverables: Your role would be very output-oriented. You'd be expected to deliver specific analyses, reports, dashboards, or data solutions within agreed-upon timelines.

Continuous Learning: You'd be exposed to many different industries, datasets, and business problems, which forces you to constantly learn and adapt.

Part of a "Service Team": Even if you're working on different projects, you'd still likely be part of a core team at the CLaaS provider, learning from each other and sharing best practices.

For an entry-level Data Analyst looking at a role like this:

It means you'd be a key part of a service that companies need. You might get exposure to a wider range of industries and data challenges quicker than in a single company's traditional setup. You need to be adaptable, a fast learner, and good at delivering concrete results. It's a way for companies to access data expertise without the full commitment of a traditional hire, and for analysts to gain diverse experience.

* Hi Tech Smart Solutions:

Hi-Tech Smart Solutions, innovative digital partner for financial and lending companies, is dedicated to support companies growth using digital space, unique technologies of data enrichment and processing. We focus on helping our clients to increase the number and quality of their customers, as well as to optimize business' processes and raise profitability, hence to bring businesses to a new level.

We specialize in adding value to clients day-to-day operations through intelligent digital solutions. Our exceptional technologies are applied by companies in different South East Asian financial markets to lessen credit risk, replace excess workforce, minimize human errors in routine activities.

We believe that every company should be focused on its core business and improving its performance. We will take care of communication with your customers. We know how to achieve efficiency when interacting with customers, build the right dialogue. And detailed statistics and reporting allow us to analyze all stages of communications, correctly allocate resources and adjust the strategy to achieve your goals.

# Z-Lift Solutions
Values:
- Holacracy is a decentralized management and organizational governance system where authority and decision-making are distributed throughout the organization, rather than being concentrated at the top
- self-service
- empowerment
- Management consulting is a professional service where external experts provide advice and solutions to organizations to improve their performance and achieve their objectives

# Monroe Consulting
Values:
Executive recruitment company Monroe Consulting Group team of experts are able to identify the best talents within the Life Science sector. Our consultant has the in-depth industry knowledge to help our clients uncover hard-to-find talents within the Life Science industry.

Monroe's Health division’s knowledge of the Life Science industry allows our executive search consultants to excel in headhunting senior executives for leading national and multinational brands within the life science market. Monroe Consulting Group headhunters are well-entrenched across the Life Sciences industry, enabling consultants to provide both our clients and candidates with a wealth of experience, intimate industry knowledge and the networks required for placing high-profile talent into key positions.

Our recruitment consultants are not only experts in their fields but also provide executive recruitment services for all job vacancies in any sub-sectors, including biopharmaceuticals, medical technology, genomics, diagnostics and digital health

Executive Search & Headhunting Recruitment Services for the Hospital & Healthcare Industry
Monroe Consulting Group is a leading provider of executive search services, within the fast-growing economies of Asia. Our Hospital & Healthcare team of experts are well placed to support multinational and local companies to identify the best available candidates within the Hospital and Healthcare sector. Monroe Consulting Group’s Hospital and Healthcare works across many sub-sectors, including pharmaceuticals, biotechnology, equipment, distribution, facilities, and managed healthcare

In this fast-paced and competitive market, our unique recruitment approach targets mid-level professionals to senior executives for companies in the Hospital and Health industry. In many cases, our executive search firm acts as an essential recruitment partner for building mid to senior-level management teams, which are critical to the success of the company. Our consultants know their markets meticulously and continue to adapt to the changes in market conditions and trends.

Executive Search & Headhunting Recruitment Services for the Software and IT Consulting Industry

Executive recruitment company Monroe Consulting Group provides outstanding headhunting services to identify the best talent within the Software and IT Consulting sector. Our executive search company’s industry knowledge means that our recruitment consultants are experts in uncovering hard-to-find, passive candidates that are often overlooked.

Monroe's team of experts are equipped with the market knowledge of the fast-growing Software and IT Consulting industry, which allows us to meet the demand of our clients. With offices across Asia and a global network across 19 countries, we can cater to local and international clients in finding talents across the globe.

Monroe's Software and IT Consulting industry recruitment consultants are not only experts in their fields but also provide executive recruitment services for all job vacancies in any department, including but not limited to executive management, Data Scientist. Software Developer, Information Security Analyst. Computer Systems Analyst. Web Developer. Sales Engineer. Information Technology Manager, and Computer Research Scientist.

# Kiya.AI
1. What do you know about kiya?
|- AFAIK
|- Based on the website you sent
|- I understand that this is an 
|- organization that aims
|- offer cloud native solutions for financial institutions
|- as well as AI and ML to automate business processes of these institutions
|- allowing scalability and efficiency 
|- I'm technical 
|- especially with data
|- you need a more robust solution especially when data scales to billions

2. what is your understanding of the role of an implementation engineer
Implementation engineer
- checking and savings account, loans, deposits, payments,
- help configure these systems
- use sql api testing for these systems
- client facing
- gathering requirements

3. Why are you interested in this role
|- I'm curious to know how technology interfaces/combines with the finance industry
|- Starting point for fintech and banking technology 

|- my skills in data engineering and being able to optimize for costs while aiming for scalability and efficiency (performance or storage)
|- believe
|- will be great addition and asset to have for this role

4. how do you see yourseelf making an impact and contributing to the team?
|- while technicality and skills important
|- being adept is important
|- I think 
|- what's even more important
|- understand business acumen

|- understanding/communicating business needs

|- as for me my unique inclination 
|- building scalable data pipelines as a data engineer
|- while maintaining cost efficiency
|- great asset an d addition to the team
|- I may come to be part of 

5. what is your experience in sql?
|- employees after 2023

feedback: tailor fit answers to the role itself but keen to learn about fintech in general 

## Technical Coding Interview Questions:
### DSA Related:
1. FizzBuzz variation question from Leetcode 
2. Simple mathematics and logic question 
3. Maximum subarray sum from Leetcode (uses kadanes algorithm) `done practicing`
4. Print an hourglass (according to their hourglass pattern) `done practicing`
5. Given two arrays, one which is rotated (either left or right), find the least times of rotations of the un-rotated array to match the rotated one. (gawin mo dito ay compare the newly rotated array each time to the old rotated array, and count the number of times you compared the array to get the two to be equal to each other)
6. Last unique character
7. Check if array is sorted or not

### SQL Related
1. Identify which rows are duplicated
```
with duplicates as (
    select emp_id, row_number() over(partition by emp_id, emp_name, emp_salary order by emp_id) as row_occ
    from employee
)

select emp_id, max(row_occ)
from duplicates
group by emp_id
```

2. remove duplicate values
```
select *
from employee
group by emp_id, emp_name, emp_salary
```

3. check if all values in a table have the same values in another table
```
-- Create EmployeeA
CREATE OR REPLACE TEMPORARY TABLE EmployeeA (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert data into EmployeeA
INSERT INTO EmployeeA (employee_id, first_name, last_name, department, salary) VALUES
(1, 'Alice', 'Smith', 'HR', 60000.00),
(2, 'Bob', 'Johnson', 'IT', 75000.00),
(3, 'Charlie', 'Brown', 'Finance', 80000.00),
(4, 'Diana', 'Miller', 'Marketing', 65000.00),
(5, 'Eve', 'Davis', 'IT', 90000.00);


-- Create EmployeeB
CREATE OR REPLACE TEMPORARY TABLE EmployeeB (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert data into EmployeeB
-- Note: Employee 4 (Diana) has a different department in B
-- Note: Employee 6 (Frank) exists in B but not in A
-- Note: Employee 5 (Eve) has a different salary in B
INSERT INTO EmployeeB (employee_id, first_name, last_name, department, salary) VALUES
(1, 'Alice', 'Smith', 'HR', 60000.00),    -- Same as A
(2, 'Bob', 'Johnson', 'IT', 75000.00),    -- Same as A
(3, 'Charlie', 'Brown', 'Finance', 80000.00),-- Same as A
(4, 'Diana', 'Miller', 'Sales', 65000.00),   -- Different department from A
(5, 'Eve', 'Davis', 'IT', 92000.00),       -- Different salary from A
(6, 'Frank', 'White', 'HR', 70000.00);   -- Exists only in B


-- Create EmployeeC to simulate that there is a table 
-- with same values and count of rows as A ordered or not
CREATE OR REPLACE TEMPORARY TABLE EmployeeC (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert data into EmployeeC
INSERT INTO EmployeeC (employee_id, first_name, last_name, department, salary) VALUES
(1, 'Alice', 'Smith', 'HR', 60000.00),
(2, 'Bob', 'Johnson', 'IT', 75000.00),
(3, 'Charlie', 'Brown', 'Finance', 80000.00),
(4, 'Diana', 'Miller', 'Marketing', 65000.00),
(5, 'Eve', 'Davis', 'IT', 90000.00);
```

This is table A
```
employee_id	first_name	last_name	department	salary
1	Alice	Smith	HR	60000.00
2	Bob	Johnson	IT	75000.00
3	Charlie	Brown	Finance	80000.00
4	Diana	Miller	Marketing	65000.00
5	Eve	Davis	IT	90000.00
```

this is table B
```
employee_id	first_name	last_name	department	salary
1	Alice	Smith	HR	60000.00
2	Bob	Johnson	IT	75000.00
3	Charlie	Brown	Finance	80000.00
4	Diana	Miller	Marketing	65000.00
5	Eve	Davis	IT	90000.00
```

And this is table C
```
employee_id	first_name	last_name	department	salary
1	Alice	Smith	HR	60000.00
2	Bob	Johnson	IT	75000.00
3	Charlie	Brown	Finance	80000.00
4	Diana	Miller	Marketing	65000.00
5	Eve	Davis	IT	90000.00
```

This is what this query `SELECT * FROM EmployeeA EXCEPT SELECT * FROM EmployeeB` returns
```
employee_id	first_name	last_name	department	salary
4	Diana	Miller	Marketing	65000.00
5	Eve	Davis	IT	90000.00
```

and this query `SELECT * FROM EmployeeB EXCEPT SELECT * FROM EmployeeA` returns
```
employee_id	first_name	last_name	department	salary
4	Diana	Miller	Sales	65000.00
5	Eve	Davis	IT	92000.00
6	Frank	White	HR	70000.00
```

As you can see it takes all elements in A not occuring in B strictly it doesn't get the difference of the subtrahend which wouldbe table B, because taking the full difference would mean for instance having {1, 2, 3} - {3, 4, 5} = {1, 2, 4, 5}. But now I understand that since we cannot achieve thisdirectly in SQL we'd have to use both the table B as subtrahend and table A as subtrahend also.

to explain further a complement is the following
```
>>> {1, 2, 3, 4, 5} - {1, 2}
{3, 4, 5}
```
where B's elements are part of a more universal set it calculates all the elements in A that are not in B

difference is the following
```
>>> {1, 2, 3} - { 3, 4, 5}
{1, 2}
>>> {3, 4, 5} - {1, 2, 3}
{4, 5}
```
where there are no universal sets but it still calculates all the elements in A that are not in B

but since we'd like to take the full difference also we'd have to also make table A as now the subtrahend and not only table B so it calculates the elements of B strictly not occuring in A, and then subsequently combine these two differences using UNION ALL


```
SELECT * FROM EmployeeA
MINUS
SELECT * FROM EmployeeB
UNION ALL
SELECT * FROM EmployeeB
MINUS
SELECT * FROM EmployeeA
```

this is dialect is in PostgreSQL and in SQL Transact in more broad dialects like ANSI SQL the code would use `EXCEPT` as keyword instead of `MINUS` 

```
SELECT * FROM EmployeeA
EXCEPT
SELECT * FROM EmployeeB
UNION ALL
SELECT * FROM EmployeeB
EXCEPT
SELECT * FROM EmployeeA
```

4. find the second-highest salary per department, but exclude departments where fewer than 3 employees exist.
```
CREATE TEMPORARY TABLE IF NOT EXISTS temp (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR,
    emp_salary INTEGER,
    dept_id INTEGER NOT NULL
);

INSERT INTO temp (emp_id, emp_name, emp_salary, dept_id) 
VALUES
(1, 'john', 50000, 1),
(2, 'wayne', 50000, 1),
(3, 'doe', 75000, 1),
(4, 'chris', 50000, 2),
(5, 'leo', 80000, 2),
(6, 'david', 50000, 3),
(7, 'martin', 60000, 3),
```

```
| emp_id | emp_name | emp_salary | dept_id |
|    1   |   john   |    50000   |    1    |
|    2   |   wayne  |    50000   |    1    |
|    3   |    doe   |    75000   |    1    |
|    4   |   chris  |    50000   |    2    |
|    5   |    leo   |    80000   |    2    |
|    6   |   david  |    50000   |    3    |
|    7   |  martin  |    60000   |    3    |
```
since we are trying to find the 2nd highest employee salary we can't simply use group bys, to find the max. We can use a `dense_rank()` to assign ranks to each salary according to or partitioned by their `dept_id`. For instance we assign a rank of 1 to the hgihest salary lets say in the tech department, we assign a rank of 2 to the 2nd highest salary in the tech department, and so on. We need to partition on the `dept_id` and then order by the employee salary in descending order so that the hghest salary is always 1st the 2nd highest 2nd, the 3rd highest 3rd and so on.
```
SELECT *, DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY emp_salary DESC)
FROM temp
```

```
emp_id	emp_name	emp_salary	dept_id	dense_rank() OVER (PARTITION BY dept_id ORDER BY emp_salary DESC)
7	martin	60000	3	1
6	david	50000	3	2
3	doe	75000	1	1
1	john	50000	1	2
2	wayne	50000	1	2
5	leo	80000	2	1
4	chris	50000	2	2
```

because we are also trying to exclude finding employees with the 2nd highest salary in a department where fewer than 3 (< 3) employees exist we can use also a `COUNT()` as a window function and assign counts each row according to or partitioned by each rows department. Kind of like using `SUM()` as a window function where instead of aggregating we calculate the sum of the values along the unique values of a column in this case the `dept_id` but still retain the number of rows.
```
SELECT *, 
  DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY emp_salary DESC), 
  COUNT() OVER(PARTITION BY dept_id)
FROM temp
```

```
emp_id	emp_name	emp_salary	dept_id	dense_rank() OVER (PARTITION BY dept_id ORDER BY emp_salary DESC)	count() OVER (PARTITION BY dept_id)
7	martin	60000	3	1	2
6	david	50000	3	2	2
3	doe	75000	1	1	3
1	john	50000	1	2	3
2	wayne	50000	1	2	3
5	leo	80000	2	1	2
4	chris	50000	2	2	2
```

from here we can use a simple filter to get only the rows with >= 3 employees and a row with rank of 2 
```
WITH ranked_employees AS (
  SELECT *, 
    DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY emp_salary DESC) AS emp_rank, 
    COUNT() OVER(PARTITION BY dept_id) AS dept_cnt
  FROM temp
)

SELECT *
FROM ranked_employees
WHERE emp_rank = 2 AND dept_cnt >= 3
```

or by using subquery (because window functions ussed with where cannot be used as it will raise an error)

```
SELECT * 
FROM (
    SELECT *, 
        DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY emp_salary DESC) AS emp_rank, 
        COUNT() OVER(PARTITION BY dept_id) AS dept_cnt
    FROM temp
) WHERE emp_rank = 2 AND dept_cnt >= 3
```

5. For each user, calculate the 7-day moving average of transactions, considering transaction dates with gaps.
```
-- Create the transactions table
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);

-- Insert sample data
INSERT INTO transactions (transaction_id, user_id, transaction_date, amount) VALUES
(1, 101, '2024-01-01', 10.50),
(2, 101, '2024-01-02', 15.00),
(3, 101, '2024-01-03', 20.00),
(4, 101, '2024-01-05', 12.75), -- Gap on Jan 4
(5, 101, '2024-01-06', 18.20),
(6, 101, '2024-01-07', 25.00),
(7, 101, '2024-01-08', 30.00),
(8, 101, '2024-01-09', 11.00),
(9, 101, '2024-01-12', 14.50), -- Another gap of 2 days since 2024-01-10 and 2024-01-11 have no transactions
(10, 101, '2024-01-13', 22.00),
(11, 101, '2024-01-14', 16.80),
(1, 102, '2024-01-01', 5.00),
(2, 102, '2024-01-03', 7.50),
(3, 102, '2024-01-04', 12.00),
(4, 102, '2024-01-08', 9.00),
(5, 102, '2024-01-09', 11.20),
(6, 102, '2024-01-10', 8.00);
```

because we have different users like 101 and 102, we will have to partition the table such that we calculate the 7-day moving average of a group of transactions of a specific user. Since the user will probably have days where they will not have transactions leaving dates where there are no transactions, this is of no obstacle to calculating the 7 day moving average. This would be a different matter however if we strictly needed to get the moving average of not only a users transactions but also their non transactions, if this was the case we would have to somehow impute the days without transactins or gap days with a value of 0 so that the avg() window function can pool instead the days with non transaction or values with 0 as opposed to pooling 7 days with purely only transactions. More on imputation on gap dates: 
- https://stackoverflow.com/questions/76203662/best-way-to-fill-in-gaps-between-dates-in-sql-table
- https://www.geeksforgeeks.org/mysql-lead-and-lag-function/

```
SELECT 
  *,
  AVG(amount) OVER(
    PARTITION BY user_id 
    ORDER BY transaction_date ASC 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS ma_7
FROM transactions
```
Here we partitioned by each user. We also need to make sure the transaction date is ordered in ascending order to that our moving average is calculated according to this manner.

if we were however going to impute we would need to get the date difference in each subsequent transactin and count how many gap days there are inbetween each transaction.
```
WITH new_transactions AS (
  SELECT
    transaction_id,
    user_id,
    transaction_date AS curr_txn_date,
    LEAD(transaction_date) OVER(
      PARTITION BY user_id 
      ORDER BY transaction_date
    ) AS next_txn_date,
    amount
  FROM transactions
),

transactions_b AS (
  SELECT 
    *,
    -- we add a one because if a difference between a date is only
    -- 1 day then resulting value will be -1, we turn this to 0 by
    -- adding 1 to represent that there are no gaps in between the
    -- dates
    DATEDIFF('day', curr_txn_date, next_txn_date) - 1 AS date_diff
  FROM new_transactions
)

SELECT *
FROM transactions_b
```

resulting in table

```
transaction_id	user_id	curr_txn_date	next_txn_date	amount	date_diff
12	102	2024-01-01	2024-01-03	5.00	1
13	102	2024-01-03	2024-01-04	7.50	0
14	102	2024-01-04	2024-01-08	12.00	3
15	102	2024-01-08	2024-01-09	9.00	0
16	102	2024-01-09	2024-01-10	11.20	0
17	102	2024-01-10		8.00	
1	101	2024-01-01	2024-01-02	10.50	0
2	101	2024-01-02	2024-01-03	15.00	0
3	101	2024-01-03	2024-01-05	20.00	1
4	101	2024-01-05	2024-01-06	12.75	0
5	101	2024-01-06	2024-01-07	18.20	0
6	101	2024-01-07	2024-01-08	25.00	0
7	101	2024-01-08	2024-01-09	30.00	0
8	101	2024-01-09	2024-01-12	11.00	2
9	101	2024-01-12	2024-01-13	14.50	0
10	101	2024-01-13	2024-01-14	22.00	0
11	101	2024-01-14		16.80	
```


```
-- we generate a series starting from minimum date to
-- the maximum date as we will be using this temp generated
-- table to cross join on our transactions table
WITH date_lookup AS (
  SELECT * AS dt FROM GENERATE_SERIES( 
    (SELECT MIN(transaction_date)
    FROM transactions),
    (SELECT MAX(transaction_date)
    FROM transactions),
    INTERVAL 1 DAY
  )
),

user_max_min_txn_dates AS (
  SELECT 
    user_id, 
    MIN(transaction_date) AS min_txn_date, 
    MAX(transaction_date) AS max_txn_date
  FROM transactions
  GROUP BY user_id
),

imputed_dates AS (
  SELECT
    b.user_id,
    a.dt
  FROM date_lookup a
  LEFT JOIN user_max_min_txn_dates b
  ON a.dt BETWEEN b.min_txn_date AND b.max_txn_date
),

fixed_transactions AS (
  SELECT 
    b.transaction_id AS txn_id, 
    a.user_id, 
    a.dt AS txn_date, 
    COALESCE(b.amount, 0) AS amount,
  FROM imputed_dates a 
  LEFT JOIN transactions b
  ON a.user_id = b.user_id
  AND a.dt = b.transaction_date
  ORDER BY a.user_id, a.dt
)

SELECT 
  *, 
  AVG(amount) OVER(
    PARTITION BY user_id 
    ORDER BY txn_date ASC
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS amount_7ma
FROM fixed_transactions
```

6. Given two tables: projects(project_id, budget), employees(employee_id, project_id), find the project with the highest “budget per unique role.” Assume an employee_roles table exists.

7. Identify users who had a transaction amount 2x higher than their average transaction amount in the past 30 days.



### PowerBI Related
1. What is the difference between a visual-level filter, page-level filter, and a report-level filter? Provide an example where improper use leads to misleading analytics.

2. Design a Power BI dashboard with Row-Level Security (RLS) where a user might belong to multiple departments. How would you implement dynamic RLS using DAX? 

### Python Related
1. Using pandas, merge three datasets (sales, promotions, inventory). Return top 5 products with the highest uplift in sales during a valid promotion window.

2. Implement a custom function in pandas that bins continuous numerical data into deciles and labels outliers based on the IQR method. Return a summary table.

3. Compare and contrast defaultdict, Counter, and regular dictionaries in Python. When would you use each for analyzing customer purchase patterns?

### Data Analytics/Engineering related
* is it a fair assertion to say that the median should be used in imputation of missing values in a column if the histogram or the distribution of data in the column when plotted is skewed and not normal since this better represents a measure of central tendency and that we would use average if the distribution of the data is normal?

* when would you use median vs mean in analyzing data? If the histogram or the distribution of data when plotted is skewed and nto normal then it may be helpful to use the middle value for imputation as this better represents a measure of central tendency. We would use average if the distribution of the data is normal.

Mean is the best choice when data is symmetric and free from extreme outliers, as it leverages all data points.
Median is preferred when data is skewed or contains outliers, as it provides a robust measure of central tendency that isn't unduly affected by extreme values.
```
CREATE OR REPLACE TEMPORARY SEQUENCE id_sequence START 1;
  
-- Create the transactions table
CREATE OR REPLACE TEMPORARY TABLE transactions (
    transaction_id INT DEFAULT nextval('id_sequence') PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);

-- Insert sample data
INSERT INTO transactions (user_id, transaction_date, amount) VALUES
(101, '2024-01-01', 10.50),
(101, '2024-01-02', 15.00),
(101, '2024-01-03', 20.00),
(101, '2024-01-05', 12.75), -- Gap on Jan 4
(101, '2024-01-06', 18.20),
(101, '2024-01-07', 25.00),
(101, '2024-01-08', 30.00),
(101, '2024-01-09', 11.00),
(101, '2024-01-12', 14.50), -- Another gap
(101, '2024-01-13', 22.00),
(101, '2024-01-14', 16.80),
(102, '2024-01-01', 5.00),
(102, '2024-01-03', 7.50),
(102, '2024-01-04', 12.00),
(102, '2024-01-08', 9.00),
(102, '2024-01-09', 11.20),
(102, '2024-01-10', 8.00);

-- we generate a series starting from minimum date to
-- the maximum date as we will be using this temp generated
-- table to cross join on our transactions table
CREATE OR REPLACE TEMPORARY TABLE date_lookup AS (
  SELECT * AS dt FROM GENERATE_SERIES( 
    (SELECT MIN(transaction_date)
    FROM transactions),
    (SELECT MAX(transaction_date)
    FROM transactions),
    INTERVAL 1 DAY
  )
)

CREATE OR REPLACE TEMPORARY TABLE user_max_min_txn_dates AS (
  SELECT 
    user_id, 
    MIN(transaction_date) AS min_txn_date, 
    MAX(transaction_date) AS max_txn_date
  FROM transactions
  GROUP BY user_id
)

CREATE OR REPLACE TABLE imputed_dates AS (
  SELECT
    b.user_id,
    a.dt
  FROM date_lookup a
  LEFT JOIN user_max_min_txn_dates b
  ON a.dt BETWEEN b.min_txn_date AND b.max_txn_date
)

WITH fixed_transactions AS (
  SELECT 
    b.transaction_id AS txn_id, 
    a.user_id, 
    a.dt AS txn_date,
    b.amount AS amount
  FROM imputed_dates a 
  LEFT JOIN transactions b
  ON a.user_id = b.user_id
  AND a.dt = b.transaction_date
  ORDER BY a.user_id, a.dt
),


final AS (
  SELECT 
    *, 
    COALESCE(
      amount, 
      (SELECT MEDIAN(amount) FROM fixed_transactions)
    ) AS amount
  FROM fixed_transactions
)

SELECT 
  *, 
  AVG(amount) OVER(
    PARTITION BY user_id 
    ORDER BY txn_date ASC
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS amount_7ma
FROM final
```

```
txn_id	user_id	txn_date	amount	amount_1	amount_7ma
1	101	2024-01-01 00:00:00	10.50	10.50	10.5
2	101	2024-01-02 00:00:00	15.00	15.00	12.75
3	101	2024-01-03 00:00:00	20.00	20.00	15.166666666666666
	101	2024-01-04 00:00:00	NULL 12.75	15.166666666666666
4	101	2024-01-05 00:00:00	12.75	12.75	14.5625
5	101	2024-01-06 00:00:00	18.20	18.20	15.29
6	101	2024-01-07 00:00:00	25.00	25.00	16.908333333333335
7	101	2024-01-08 00:00:00	30.00	30.00	20.158333333333335
8	101	2024-01-09 00:00:00	11.00	11.00	19.491666666666667
	101	2024-01-10 00:00:00	NULL 12.75	19.39
	101	2024-01-11 00:00:00	NULL 12.75	19.39
9	101	2024-01-12 00:00:00	14.50	14.50	19.74
10	101	2024-01-13 00:00:00	22.00	22.00	20.5
11	101	2024-01-14 00:00:00	16.80	16.80	18.86
12	102	2024-01-01 00:00:00	5.00	5.00	5.0
	102	2024-01-02 00:00:00	NULL 12.75	5.0
13	102	2024-01-03 00:00:00	7.50	7.50	6.25
14	102	2024-01-04 00:00:00	12.00	12.00	8.166666666666666
	102	2024-01-05 00:00:00	NULL 12.75	8.166666666666666
	102	2024-01-06 00:00:00	NULL 12.75	8.166666666666666
	102	2024-01-07 00:00:00	NULL 12.75	8.166666666666666
15	102	2024-01-08 00:00:00	9.00	9.00	9.5
16	102	2024-01-09 00:00:00	11.20	11.20	9.925
17	102	2024-01-10 00:00:00	8.00	8.00	10.05
```




* What is data analytics? Data analytics is the process of examining, cleaning, transforming, and modeling data to extract useful information, draw conclusions, and support decision-making.

* What are the types of data analytics? Descriptive, diagnostic, predictive, and prescriptive analysis.

* Explain the difference between qualitative and quantitative data? Qualitative data is non numerical, such as text or images, while quantitative data is numerical, such as measurements or counts.

* What is data cleansing? Data cleansing is the process of identifying and correcting errors, inconsistencies, and inaccuracies in datasets.

* What is data outlier? An outlier is a data point that significantly differs from the rest of the data points in a dataset.

* Explain the difference between SQL and NOSQL databases? SQL databases are relational, use structured query language, and have a predefined schema, while NoSQL databases are non-relational, use various query languages, and have a dynamic schema.

* What is a histogram? A histogram is a graphical representation of the distribution of a dataset, showing the frequency of data points in specified intervals.

* What is a box plot? A box plot is a graphical representation of the distribution of a dataset, showing the median, quartiles, and possible outliers.

* How do you design/data model a data warehouse schema?
|- understanding business needs
    |- what questions they need answers to (e.g. what are the best selling products by region, average sales last year)
    |- what metrics they care about? (quantifiable numbers e.g. transactions in an institution)

|- identifying fundamental activities and entities
|- business/platform/app?
    |- clicking on products
    |- placing an order
    |- adding to cart
    |- payment
    |- product shipping
    |- product returns
    |- customer signups/registrations

|- each process
|- has transactions
|- make fact table in DWH
|- depending on size of data
|- identify quantifiable data
|- numerical data change each row
|- for analyses
|- sales
|- prie
|- units/quantity sold
|- discount value

|- depending on what is the business situation (e.g. size of data they have)
|- and what they are optimizing for e.g. optimize for storage efficiency, 
computational efficiency, or both  
|- 

|- think of the transactions one big table
|- which attributes are redundant
|- which attibutes are numeric
|- which attributes numeric or non numeric can be grouped into their own table
|- split identified attributes into their own table
|- customer_id, customer_name, email, address, city, state, region, total_txn, txn_date, order_id, prod_id, prod_name, category, brand, stock keeping units
|- group 1 attributes: customer_id, customer_name, email, customer_id, city, state, region
|- group 2 attributes: prod_id, prod_name, category, brand, stock keeping units, 
|- 

|- all this to improve cost efficiency and query performance in analytical tasks

Designing a data warehouse schema for an e-commerce website is a common task for data professionals. Interviewees typically approach this by outlining a structured, logical process.

- Understand Business Requirements & Key Metrics.
- Identify Core E-commerce Business Processes.
- Choose a Dimensional Modeling Methodology.
- Define Fact Tables (Measures & Granularity).
- Identify Dimension Tables.
- Determine Attributes for Each Dimension.
- Establish Relationships (Fact-Dimension Joins).
- Plan for Slowly Changing Dimensions (SCDs).
- Consider Aggregation Strategies.
- Review, Validate, and Iterate.

Data Warehouse Schema Design Steps (Simple & Concise)
Understand Business Requirements & Key Metrics:

Establish Relationships (Fact-Dimension Joins):

What: Connect your fact tables to your dimension tables using foreign keys. The fact table will contain numeric IDs that link to the primary keys of the dimension tables.

* What are slowly changing dimensions (SCD), and how do you handle them?
|- refer
|- dim tables
|- evolve
|- overwrite
|- inserting
|- adding col/attribute/fields
|- based
|- fact table
|- fact table orders
|- added new customer
|- added new product
|- changed customer name, phone, email, address
|- changed product label
|-  
Slowly changing dimensions (SCD) refer to data in dimension tables that evolve gradually over time. For example, a customer's address may change, but the historical data needs to be preserved for accurate reporting.

There are three main types of SCD:

- Type 1: Overwrite the old data with new data (e.g., update the address directly)
there are different columns

a natural key is a column
comes from and created by OLTP systems
user1
user2
...
user3
used to track a specific entity
distinguishes it from all other rows
oh so a natural key is like 
1, 2, 3 - surrogate key
0001, 0002, 0003 - natural key with semantic meaning
ZCZ371, NIJ120, OHP234 - natural key with semantic meaning
basically natural keys are like primary keys but have
semantic meanings for business contexts especially
kaya lang if you try to optimize for readability
then use natural key if for optimizing storage

target table - 

source (staging) table - 

- Type 2: Maintain historical data by adding a new record with a start and end date.
- Type 3: Keep limited historical data by adding new fields/attributes for the old and current values.

* what is ACID compliant transactions?
|- acronym
|- atomicity
    |- treated as 
    |- single
    |- unit
    |- if transaction fails
    |- rolled back
    |- original state
|- consistency
    |- transaction
    |- bring DB 
    |- from 
    |- valid state 
    |- to another
    |- ensures
    |- data
    |- 
|- isolation
    |- transactions/queries
    |- no interference
    |- each other
    |- prevent
    |- corruption
|- durability 
    |- a transaction
    |- after success
    |- remain
    |- permanent
|- systems
|- use
|- as standard
|- ensure
|- data integrity

* Can you explain the differences between OLAP and OLTP?
|- OLTP
|- real time
|- fast transaction
|- insertion
|- deletion
|- update
|- OLAP
|- consolidated 
|- long time
|- complex
|- aggregations
|- joins
|- fast querying
|- for analytics

* how do you handle large volume of data efficiently?
|- multiple ways
|- parquet file format
|- normalizing
|- structured data
|- little (dimension) tables
|- using distributed compute
|- concurrent
|- processing
|- across 
|- multiple
|- nodes 
|- cores

* Explain the difference between inner join and outer join in SQL. 
|- Inner join returns records 
|- with matching values in both tables
|- while outer join returns records 
|- from one table and the matching 
|- records from the other table, filing
|- in NULL values for non-matching records.

* What is primary key in a database? 
|- A primary key is a unique 
|- identifier for each record in table.

* What is foreign key in a database? 
|- A foreign key is a field in a table
|- that refers to the primary key of 
|- another table, establishing a relationship
|- between the two tables.

* difference betweeen DELETE and TRUNCATE

* how do you define the role of a data engineer?
|- perform
|- data transformatio
|- presenting
|- stakeholder

* what is a data engineer?
|- backbone
|- data driven org
|- collecting/storing
|- usble
|- data scientist/analyst/business

* what is ETL?
|- extract
|- collect
|- various
|- sources
|- cleaning
|- organzing
|- ussable
|- loading
|- destination
|- OLAP
|- for
|- analytical
|- vector
|- for 
|- AI/ML

* how do you handle 

* Compare Import vs Direct Query modes in the context of handling real-time data from a distributed warehouse system with high latency.

* what is data transformation
|- changing
|- raw

* how do you stay updated in tech in data engineering?

* have you worked with real time data streaming tech?

* what is data ingestion?

* how do you handle data security and privacy concerns?

* Difference between SQL and MySQL?

* what are CRUD operations?

* how to display unique rows?

* is there any way to retrieve a deleted database?

* https://www.datacamp.com/blog/data-warehouse-interview-questions

* what are some data quality checks you can do for your final data in an ETL pipeline?
|- Null or missing values check
|- Primary key uniqueness check
|- Duplicate record detection
|- Referential integrity validation
|- Data type validation against schema
|- Numeric range checks (e.g., 0–100%)
|- String length validation
|- Regex pattern validation (email, phone, IDs)
|- Allowed values/domain validation
|- Business rule consistency (aggregates, totals)
|- Cross-column consistency checks
|- Timeliness/freshness check against SLA
|- Completeness check (all expected partitions/files)
|- Volume checks against historical thresholds
|- Distribution checks (mean, median, std deviation)
|- Outlier detection for abnormal values
|- Schema drift detection (new/removed columns)
|- End-to-end reconciliation across systems
|- Duplicate file ingestion prevention
|- Negative value checks were not allowed
|- Percentage/total consistency checks
|- Hierarchy validation (region → country → state)
|- Multi-source consistency checks
|- Audit column validation (created_at, updated_at)
|- Change data capture consistency

### Data Science/ML related
* What is linear regression? Linear regression is a statistical method used to modethe relationship between a dependent variable and one or more independent variables.

* What is overfitting? Overfitting occurs when a model is too complex and performs well.

* Explain the difference between Rsquared and adjusted R-squared? R-squared measures the proportion of variation the dependent variable explained by the independent variables, while adjusted R-squared adjusts for the number of independent variables in the model.

* What is a confusion matrix? In a confusion matrix is a table used to evaluate the performance of a classification model, showing the true positives, true negatives, false positives, and false negatives.

* What is K-means clustering? K-means clustering is an unsupervised machine learning algorithm used to partition data into k clusters based on their similarity.

* What is cross-validation? Cross-validation is a technique used to evaluate the performance of a model by splitting the dataset into training and testing sets multiple times and calculating the average performance.

* What is a decision tree? A decision tree is a flowchart-like structure used indecision making and machine learning, where each internalnode represents a feature, each branch represents adecision rule, and each leaf node represents an outcome.

* What is the difference between supervised and unsupervised learning? Supervised learning uses labeled data and a known output, while unsupervised learning uses unlabeled data and discovers patterns or structures in the data.

* Explain principal component analysis (PCA)? PCA is a dimensionality reduction technique that transforms data into a new coordinate system, reducing the number of dimensions while retaining as much information as possible.

* What is time series analysis? Time series analysis is a statistical technique for analyzing and forecasting data points collected over time, such as stock prices or weather data.

* What is difference between a bar chart and a pie chart? A bar chart represents data using rectangular bars, showing the relationship between categories and values, while a pie chart represents data as slices of a circle, showing the relative proportion of each category.

* What is a pivot table? A pivot table is a data summarization tool that allows users to reorganize, filter, and aggregate data in a spreadsheet or database. 

* What is data normalization? Data normalization is the process of scaling and transforming data to eliminate redundancy and improve consistency, making it easier to compare and analyze.

* Explain the concept of data warehousing? A data warehouse is a large, centralized repository of data used for reporting and analysis, combining data from different sources and organizing it for efficient querying and reporting.

* What is the role of a data analyst in a company? A data analyst collects, processes, and analyzes data to help organizations make informed decisions, identify trends, and improve efficiency.

* How do you handle missing data in a
dataset? Missing data can be handled by imputing values
(mean, median, mode), deleting rows with missing data, or
using models that can handle missing data.
* How do you deal with outliers in a dataset? Outliers can be dealt with by deleting,
transforming, or replacing them, or by using models that
are less sensitive to outliers.
* Describe a situation where you used data
analysis to solve a problem? Answer this based on your personal experience,
detailing the problem, your approach, and the outcome.
* How do you ensure data quality and
accuracy in your analysis? Ensuring data quality and accuracy involves data
cleansing, validation, normalization, and cross-referencing
with other sources, as we I as using appropriate analytical
methods and tools. 
* Describe your experience with
programming languages, such as R or Python,
used in data analysis? Answer this based on your personal experience,
highlighting your proficiency
* How do you handle large datasets? Handling large datasets involves using efficient
data storage and processing techniques, such as SQL
databases, para lel computing, or cloud-based solutions,
and optimizing code and algorithms for performance.
* What is your experience with data
visualization tools, such as Tableau, Power Bl, or
Excel? Answer this based on your personal experience and
familiarity with the mentioned tools, providing examples of
projects or tasks you have completed using them
* How do you stay. upadated on the latest
trends and developments in data analysis? Mention resources such as blogs, podcasts, online
courses, conferences, and industry publications that you use
to stay informed and up-to-date.
* How do you handle data privacy and
security concerns in your analysis ?
* How do you ensure your data analysis is
unbiased? By being aware of potential biases, using diverse
data sources, applying objective analytical methods, and
cross-validating results with other sources or techniques.
* What metrics do you use to evaluate the
sucess of a data analysis project? Metrics may include accuracy, precision, reca I, F1
score, R-squared, or other relevant performance measures,
depending on the project's goals and objectives
* How do you determine the most appropriate data analysis technique for a given problem? By understanding the problem's context, the nature of the data, the desired outcome, and the assumptions and limitations of various techniques, selecting the most suitable method through experimentation and validation.
* How do you validate the results of your data analysis? By using cross-validation, holdout samples, comparing results with known benchmarks, and checking for consistency and reasonableness in the findings.
* What are AI agents and RAG AI agents?

AI agents takes in information from its environment (like reading Twitter posts, stock data, or even a user's question).

Reason/Decide: It processes that information and decides what action to take or what output to generate based on its goals and programming. This often involves using a Large Language Model (LLM) as its "brain."

Act: It performs an action or generates a response (like drafting a summary, answering a question, or giving feedback).

The key idea is that an AI agent has some level of autonomy and can perform tasks to achieve a goal, often by interacting with external tools or information sources.

RAG AI agents specific AI agents which receives a Query/Request: A user asks the RAG agent a question or gives it a task (e.g., "What's the sentiment on Apple stock among users?", or "Summarize recent user feedback on market trends").

Retrieval (Your Data Comes In Here!): Instead of just relying on its internal, pre-trained knowledge (which might be outdated or not specific enough), the RAG agent first performs a retrieval step.

It looks up relevant information from an external, curated knowledge base. This is the vector database or search index that contains the data you transformed.

Your Data Engineering Role: You transformed raw, tabular stock data (and other types) into a text format (e.g., descriptions, news articles, reports) suitable for this knowledge base. You then fed it into the "ingestion layer," which likely involved preparing it for vectorization (converting text into numerical representations that capture meaning) and indexing in a search-optimized database. This ensures the RAG agent has access to specific, up-to-date, and relevant context.

Augmentation: The relevant pieces of information retrieved from your knowledge base are then "augmented" or added to the user's original query. This provides the LLM with context.

Generation: The augmented query (original query + retrieved context) is then fed into the core LLM. The LLM uses this specific context to generate a much more informed, accurate, and relevant response.

Analogy: Imagine asking a very smart person a question.

Without RAG: They just answer based on what they already know.

With RAG: They first quickly look up relevant facts in a well-organized library (your transformed data!), then use those facts to formulate a precise answer.

How Your RAG AI Agents Operated (on Twitter data):
Based on your description, the flow for an agent focused on "giving feedback on the stock market" might have looked like this:

User Creates Agent: A user configures an AI agent to monitor Twitter for stock market discussions.

Twitter Data Ingestion: The company's system continuously collects tweets from users related to specific stocks or market trends.

Your Data Transformation & Ingestion:

You receive raw stock data (prices, company news, financial reports – likely tabular).

You transform this tabular data into meaningful textual formats (e.g., converting price movements into descriptive sentences, summarizing key financial metrics, turning news articles into searchable chunks).

This transformed text is then fed into an "ingestion layer" which processes it (e.g., chunks it, vectorizes it) and adds it to the knowledge base/vector database that the RAG agents query.

Agent Activation/Querying: When a user asks the stock market feedback agent a question (or the agent needs to generate a summary/feedback):

It queries the knowledge base (which contains your transformed stock data and potentially other relevant information).

It retrieves the most relevant textual pieces of stock market context.

Feedback Generation: The agent (using its LLM) then uses this retrieved context, combined with the real-time Twitter data it's monitoring, to generate informed feedback or analysis on the stock market.

Describing Your Work in Interviews:
When describing your work, emphasize these points:

"As a Data Engineer Intern, I specialized in building data pipelines to support Retrieval Augmented Generation (RAG) AI agents."

"My core responsibility involved transforming diverse data sources, particularly tabular financial/stock market data, into a structured textual format. This preparation was crucial for optimizing its use by Large Language Models (LLMs)."

"I ensured this prepared data was accurately fed into an ingestion layer, which facilitated its vectorization and indexing in a knowledge base (or vector database). This knowledge base served as the external memory for RAG agents."

"This enabled the AI agents, which primarily analyzed real-time user-generated content from platforms like Twitter, to provide highly accurate, contextually relevant, and up-to-date insights – for example, generating detailed feedback on stock market trends, augmented by the specific financial data I prepared."

"Essentially, I was the bridge ensuring the AI agents had access to precise, external, and up-to-the-minute information, allowing them to go beyond their pre-trained knowledge and provide more factual and valuable responses to users."

This highlights your understanding of AI, your specific technical contributions, and the direct business impact of your data engineering work. You weren't just moving data; you were making AI smarter and more reliable.

## Behavioral Interview Questions (21):

### Background (1):
* tell me about yourself:
|- data engineer intern
|- cleaned transformed
|- incoming data
|- text
|- ingested
|- ETL 
|- developed
|- data engineers
|- transformed
|- vector
|- augment
|- rag ai
|- knowledge
|- existing
|- predict
|- up-to-date
|- domain 
|- specialize 

|- additionally
|- recent grad
|- picked up
|- data science
|- during
|- personal projects
|- AI/ML
|- now
|- geared
|- more recent
|- shifted
|- data engineering
|- analytics
|- more fun personally
|- where
|- 2 recent
|- I'm most
|- Proud of
|- Healthcare
|- Data
|- Analytics
|- End2end
|- DE pipeline
|- Gender based
|- ML
|- model
|- API

|- eager
|- opportunity
|- skills
|- use
|- grow

* Do you have experience in data analysis/engineering, ETL/ELT, data warehousing, etc.?

|- I appreciate 
|- question 
|- maam
|- I'd like
|- clarify
|- could the
|- personal projects
|- have done
|- that allowed
|- onself
|- gain 
|- extensive exp
|- serve
|- equivalent 
|- years of exp
|- done/applied in
|- a formal work setting

|- if that's the case
|- yes
|- actually 2/<n> 
|- best 
|- projects
|- 1st
    |- full on
    |- end2end
    |- ETL
    |- for 
    |- healthcare
    |- analytics
    |- chronic disease indicators
    |- us
    |- analyzed
    |- KPI
    |- driving
    |- populations
    |- high rate
    |- cdi
    |-
    |- business use case
    |- potentially 
    |- solve
    |- lack
    |- insights
    |- which
    |- demographic
    |- target
    |-
    |- by
    |- identifying
    |- KPI
    |- (see above)
    |-
    |- allocate 
    |- healthcare
    |- efficiently
|- 2nd
    |- full on
    |- end2end
    |- MLOps
    |- pipeline
    |- for 
    |- voice 
    |- based
    |- AI/ML app
    |- capable
    |- predicting
    |- gender
    |- audio recording
    |- individuals
    |-
    |- business use case
    |- two fold
    |-
    |- potentially
    |- automate market analyses/research
    |- largely manual 
    |- such as knowing what products individuals of specfic demographics gravitate to
    |-
    |- by utilizing audio devices coupled
    |- this developed predictive power model
    |- product/market insights may be achieved
    |-  obtained faster
    |- therefore driving market growth
    |-
    |- audio data
    |- difficult to 
    |- efficiently & affordably convert from
    |- unstructured format to actionable intelligence
    |-
    |- by developing this pipeline
    |- I was
    |- able to reduce cloud operational costs
    |- 70% 
    |- using only the remaining 30% for important aspects
    |- such as large scale extraction
    |- and scalable storage
    |- and automate processing of over 20gb/3.7b rows of data points

* Tell me about your experience with modern DE tools like dbt and Snowflake?
|- That's a fair point
|- While I may not have years of 
|- employment experience with dbt and Snowflake
|- my experience is measured by proactive mastery 
|- and execution—which I believe is more relevant.
|- 
|- After completing 2 of my recent end to end ETL projects   
|- I became obsessively goal-oriented
|- dedicating the last six months to building my technical foundation to match industry demand.
|- and it just so happened that the job description itself required dbt and snowflake as I was developing another recent project which I am documenting myself in LinkedIn about it 

The Proof of Mettle: I designed and implemented a full-scale ELT Data Lakehouse pipeline using Snowflake, dbt, and Apache Airflow to ingest and model unstructured forum data for emerging market trend analysis.

The Analytical Mind: My unique inclination is to be a cost optimization maniac. I intentionally architected the solution to be cost-efficient and scalable, leveraging S3/Delta Lake for storage and using Snowflake only for compute-intensive transformations.

The Coachability Factor: This entire project was built using industry best practices, largely due to direct mentorship from senior Data Engineers who guided my use of dbt's staging methodologies, proving my ability to rapidly adopt and implement complex professional feedback.

### Company Related (6):
* what's your salary expectation
|- seen
|- typical
|- range
|- application
|- comfortable
|- based
|- ask
|- know more
|- align
|- technology
|- determine
|- expectations

`I've researched and seen the typical salary range of mid level software developers and engineers in this company amid my application and the range is between the lower range of 250k/year to 500k/year or 20800/month to 41700/month, so the number I'm comfortable with would be 30000/month based on my current knowledge and expertise does that fit into the company budget? But I'd like to learn more about the specific technologies tailored for this position as that will determine further my expectations for my salary.`

* why should we hire you (more selfish reasons)? 
|- hoping
|- ask
|- I understand
|- looking
|- skilled in <insert job qualifications e.g. Data Pipelines, MLOps, Python, SQL, powerbi, data analysis, informatica>
|- used
|- python 
|- all years 
|- college
|- all personal projects
|- thesis

|- recently
|- developed
|- DE/DA project
|- refer above to (chronic-disease-analyses) project
|- used
|- orchestration framework
|- airflow
|- extract
|- raw data
|- consolidated
|- over 20
|- transform 
|- data trans
|- modelled
|- spark
|- load
|- cloud DWH
|- motherduck
|- faster querying
|- due
|- OLAP struct
|- visualized
|- PowerBI

|- another
|- end 2 end
|- MLOps pipeline
|- audio based analytics
|- orchestration 
|- airflow
|- extract
|- combination (ADF, Az Func, azure data lake)
|- 3.7billion/20gb audio recordings
|- transformation
|- duckdb, librosa, sklearn 
|- computing features, normalization, imputation, augmentation
|- loading
|- cloud DWH
|- motherduck
|- open source

|- additionally
|- I understand 
|- looking
|- communicate/understand
|- business needs
|- and while I believe
|- being
|- adept
|- skills
|- important
|- I believe
|- unique
|- inclination
|- build
|- scalable systems
|- while
|- aiming
|- cost efficiency
|- in terms
|- peprformance
|- storage
|- is just as important
|- will I believe
|- great and unique
|- addition
|- to the team, your organization

|- while I (insert lack of skill in what their lookign for e.g. exp in credit risk, fintech as a whole, domain knowledge in business)
|- I believe
|- can
|- adept
|- skills,
|- to learn
|- not so much
|- whole
|- domain
|- just
|- enough
|- do the job

* why do you want to work here (more selfless reasons)?
|- I understand 
|- <company name>
|- prides itself
|- <insert work env e.g. 
    gcash: growth, recognition and social impact
    z-lift: empowerment, consultancy, 
  >
|- real
|- skills
|- alone
|- important
|- matters
|- moreso
|- ones
|- drive/fire
|- learn
|- grow
|- which
|- I believe
|- <insert company name>
|- holds
|- on
|- to

|- I honestly
|- want
|- impact
|- give value
|- contribute
|- organization
|- cause
|- matters

|- sincerely
|- for lack
|- better 
|- all I
|- need
|- shot
`Having first learned about your company 2 years ago what I really value is that your compnay strives for the virtues of responsibility, teamwork, and honesty, which resonate with me because I believe I can be responsible enough to own my shortcomings, support my teammates by listening to their concerns and questions, and be completely honest about certain predicaments I may be in, or concerns I have without fear of ridicule or shame. I think these are essential in the workplace which funnily enough can be translated into human to human relationships themselves be it platonic or romantic.`

`I think the company fosters growth in technologies which I'm greatly enthusiastic about, because while monetary value is important we cannot deny this, learning new things is just as equally important and I think learning new things like technologies can greatly contribute to developing quality products. On a more simple note learning new things is fun for me personally and learning new things through hands on building is what I'm fond of doing the most`

* what do you know about this organization (gcash for example)?
|- I understand
|- <company name>
|- dedicated
|- business
|- of

|- digital financial services, finance technology, 
    |- leading mobile wallet & finance super-app
    |- in the Philippines. 
    |- its core purpose:
    |- accelerate financial inclusion by making digital financial services accessible to the country's large unbanked population.
    |-
    |- Core Business Functions
    |- 1. e-wallet for instant, secure transactions. 
    |- to deposit and withdraw in/out
    |- pay bills to over 400+ billers, 
    |- and make purchases via QR code (Scan-to-Pay) at millions of partner merchants and social sellers.
    |- seamless, real-time money transfers between GCash users (GCash-to-GCash) 
    |- and to and from traditional banks (via InstaPay), 
    |- eliminating the need for physical bank visits.
    |- 
    |- 2. provider for revolving credit lines (GCredit)
    |- personal loans (GLoan and GGives - buy now, pay later) to users based on
    |- their GScore (creditworthiness).
    |-
    |- 3. other financial services such as
    |- (GSave) for digital savings
    |- (GFunds and GStocks) for accessible investment 
    |- products with low barriers to entry (e.g., no minimum deposit).
    |- 
    |- honestly has interested me to know
    |- that potentially working here
    |- may entail getting to work with to an
    |- extent the sheer massive scale of data 
    |- coming from
    |- the millions
    |- active users
    |- billions of transactions everyday
    |- generating data at high volumes and velocity: Handling millions of real-time financial transactions daily.
    |- and its reliance on novel technologies 
    |- for advanced analytics by means of AI/ML 
    |- (like the GScore AI) for credit scoring, personalized ads, and fraud detection.

|- search & referral
    |- company
    |- aim
    |- to put
    |- best
    |- most qualified
    |- candidates
    |- assisting
    |- client company
    |- in filling
    |- various
    |- positions
    |- in their organization
    (|- and as I understood
    |- positions
    |- suited more for tech/IT)
    |-
    |- providing information-based analytics & decision tools
    |- help researchers 
    |- advance 
    |- scientific knowledge
    |- help businesses, governments 
    |- prevent fraud
    |- help law makers achieve 
    |- justice
    |- fair results for their clients
    |- help consumers 
    |- access financial services 
    |- get fair prices on insurance
    |- help customers 
    |- learn about markets
    |- complete transactions
    |-
    |- for professional and business clients
    |- driving them
    |- in better decision making processes
    |- to get better results
    |- to be more productive.

|- developing pharmaceuticals
    |- being the one
    |- leading the charge
    |- I would say in this 
    |- domain
    |- healthcare realted products
    |- 
    |- additionally 
    |- lead manufacturer
    |- well known otcs, health supplements
    |- Neozep, Biogesic, Solmux, Ceelin, ImmunPro, Enervon
    |- 
    |- committed to world-class
    |- quality manufacturing of
    |- these products 
    |- 
    |- upholds standardds
    |- of 'malasakit' 
    |- above and beyond to serve health needs of Filipinos
    |- through numerous advocacies 
    |- like Alagang Unilab
    |- focuseing on making primary 
    |- healthcare accessible to communities
    |- bayanihan
    |- emphasizing teamwork for the welfare of the Filipino



|- other than
|- that
|- heard 
|- positive 
|- work environment

|- people

|- came across
|- I actually interviewed
|- learned
|- interesting
|- tech stack




* what qualities are you trying to find in a company? `open honest communication, mutual support, responsibility and integrity `



### Personality (6):
* what are your 3 biggest strengths and explain each one?
|- meticulousness
|- creativity
|- collaboration
    |- sharing
    |- ideas
    |- improvement
    |- consensus
- `meticulousness: as I always make sure to analyze the quality of the code I write and make sure most if not every case is taken into consideration`
- `creativity: I really like to implement designs in code that elicit beauty and inspiration`
- `collaboration: I like to share my thoughts of approaching a problem with my teammates and asking in turn their opinion on how they would solve it, and sharing our solutions right after and come to a reasonable way how to integrate it`

* What were the results of your 3 strengths in thesis? 
- `meticulousness: I made sure the signal features we had were properly extracted and through the functions we wrote, we made sure to understand the dataset fully in order to implement the features needed for our system to train on`
- `creativity: the user interface is something I'm most proud of because of its ability to be simple but also functional and informative, the design is also something I'm most proud of as it elicits the paradigm of minimalism in something as complex a system as ours`
- `collaboration: me and my group mates had our strengths in doing other aspects of our thesis, but one aspect was really challenging in that we had no adequate resources to train our system using our large dataset. I offered solutions to avail computing resources from providers like google to my groupmates but with mutual effort in researching other means my other groupmate offered to instead avail computing resources from DOST which was luckily completely free of charge, and luckily could be used using a Linux OS which I was already familiar with, allowing us to train our system without much hassle from cost and most especially not having a large learning curve to use the resource`

* what are your weakness as a person and as a worker/student and how did you confront them? 
- `sometimes *I tend to keep problems (both technical and non-technical) to myself*, and while independence has its merits it means that I lead myself at times to unnecessary amounts stress, so I always make sure to understand the problem clearly by asking my colleagues and then ask without shame help if needed`
- `due to me being *overly independent sometimes* I fail to have my team check on what I've done and whether it measures up to their approval, so what I do to confront this is to make sure that in times where I catch myself working on something and having thoughts of perhaps submitting it before approval of others, I have my team members assess the thing I've worked on and come to a reasonable agreement on what else could be improved before submitting it as a final product`

* describe a time where you failed at work or in a project.
- `I think it was the time when I was making my personal projects because when I was running into error after error I sometimes like any other human felt the frustration of being unable to sovle it however I noticed that whenever I gave myself some time or perhaps a break that the will so to speak or the idea of potentially solving the problem at hand would come to me, and I'd use it to solve the problem at hand. I did have times where I really could not sovle the problem I was facing case on point the 1st attempt of my undergrad thesis because we did not seemingly come to identify what part our algorithm was going wrong, we could not figure out why our results were the way they were, even when we tried every other means of solving it or trying to make it better. In the end however we learned a ton from it and made us more resilient in tackling errors in the future which would come to also manifest in our 2nd attempt at our thesis`

* what are you trying to avoid when working (they give work life balance kaya answer you don't want to burn out well not explicitly but as much as possible you try to avoid enough work and then balance with it other endeavors)? `I know I'm a young developer I have much to learn and naturally that may come out in trying to take on as much responsibility as physically possible as a way to learn and prove myself, so I avoid biting off more than I can chew because I've learned that everything can just be taken one step at a time as opposed to all at once at the cost of being burnt out in long run`

* how do you manage your time and schedule? `I find that in the context of work I write down the task what this task requires what other requirements those requirements require, and see the simplest task/requirement I can accomplish this way I manage my time by not procrastinating through being overwhelmed at the task given. I make sure to also do my routine like eating, sleeping, taking little breaks here and there in an orderly manner so as to keep my schedule and time on track.`

### Team Playing Related (8):
* what would you do if your teammate does not agree with how you wrote your code?
|- uncover reason
|- theres
|- always
|- justification
|- why
|- they
|- wrote
|- you 
|- wrote
|- way
|- example
|- optimized
|- readability
|- I optimized
|- time efficiency and cost
|- decide
|- net benefit
|- company
|- readable yes 
|- not scalable
|- unreadable yes
|- virtually
|- cost efficient
|- scalable 

```
SELECT emp_name, emp_id, dept_id
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id
WHERE department.dept_id = 1
```

may very well be readable but sometimes the code below is much more performant and efficient

```
SELECT emp_name, emp_id, dept_id
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id
AND department.dept_id = 1

```
- `this is much performatn than the latter because rather than joining all potential rows of the tables that have the same department id and then filtering them right after, we immediately filter the rows that have a certain department id while also joining these rows to the other tables corresponding rows with the same department id, making it scalable and efficient`

* what do you do when having conflicting ideas with other members? 
|- sometimes
|- both
|- quality
|- output/code
|- obviously
|- one
|- need
|- feel
|- contributing
|- assess
|- each 
|- strength
|- incorporate both
|- come
|- reasonable
|- middle

```
similar to the previous answer of having certain justifications for the code I write I would do the ff:
1. know the idea I have in mind and want implemented 
2. know the idea my team member personally wants to implement
3. assess the strengths and weaknesses of each idea
4. it is at times unavoidable that he/she will have the better solution and so sometimes you have to put your ego aside but sometimes I reasonable integration of both ideas strengths can be in fact better as it not only maybe a better solution but both parties can be mutually satisified. (You can both have your cake and eat it too so to speak)
```

* what kind of personality you like to work with? `A kind that fosters a collaborative, supportive, and teamwork oriented environment, one that works with fellow team member through the problem when needed while allowing the growth of his fellow team members, and one that is capable of providing the team with an encouraging voice towards success which may mean finishing even the smallest of tasks for the day`

* what are the types of people you don't want to work with? `I honestly think that I can get along with anyone so long as there is mutual respect, but one thing I cannot tolerate in a person is dishonesty by taking credit for other peoples work that is the only exception i would say to the person I would not want to work with`

* How do you make sure that you deploy quality code in production? `One dont work in silence, communicate if may mali sa data niyo to data engineers. And two have someone quality assure your code`

Key Focus: Prevention, thorough testing, collaboration, and robust processes.

Suggested Answer:

"Ensuring quality code in production is a multi-faceted process that involves a combination of preventative measures, rigorous testing, and strong team collaboration. My approach would cover these areas:

Robust Local Development & Version Control:

Modular and Testable Code: **Write code in a modular fashion, making individual components easily testable**.

Local Unit and Integration Tests: **Develop comprehensive unit tests for individual functions and integration tests to ensure different components work together as expected**.

Git and Feature Branches: **All code is developed on feature branches** and managed with Git for version control.

Code Review and Collaboration:

Pull Requests (PRs): Changes are submitted via PRs, requiring **at least one peer reviewer (or more for critical changes)**.

Thorough Code Review: Reviewers **check for logic correctness, adherence to coding standards, potential edge cases, performance implications, and security vulnerabilities**. This is also where discussions about data handling and assumptions take place.

Documentation: **Ensure code is well-commented and documented**

Automated Testing and Continuous Integration (CI):

CI Pipeline Integration: Integrate automated tests (unit, integration, data quality tests) into a CI pipeline (e.g., GitHub Actions, GitLab CI, Azure DevOps Pipelines).

Automated Data Quality Tests: Crucially, implement tests (e.g., using dbt test or Great Expectations) that validate assumptions about the data itself – checking for uniqueness, non-null values, expected ranges, and schema conformity before data transformations are applied or moved to production.

Static Code Analysis/Linting: Use tools to automatically check for code style, potential bugs, and best practices.

Automated Build & Package: Ensure the code can be built and packaged correctly without manual intervention.

Staging/Pre-Production Environments:

Environment Parity: Deploy changes to a staging environment that closely mirrors production (data volume, configuration, infrastructure).

End-to-End Testing: Run end-to-end tests in staging to validate the entire pipeline flow, from data ingestion to final consumption (e.g., dashboard updates, downstream system feeds).

Performance and Scalability Testing: Assess how the code performs under realistic loads.

Clear Deployment Strategy:

Controlled Deployments: Use automated deployment tools (part of CI/CD) to ensure consistent and repeatable deployments.

Rollback Plan: Always have a clear and tested rollback strategy in case issues arise post-deployment.

* What would you do if you deploy bad code in prod? `My first answer was to pull the code from production again, push it to a development branch and have someone quality test it before pushing to production`

Key Focus: Immediate mitigation, communication, root cause analysis, and prevention of recurrence.

Suggested Answer:

"If I were to deploy bad code to production, my immediate actions would prioritize mitigating impact, communicating effectively, and then systematically resolving the issue to prevent recurrence.

Immediate Impact Mitigation (Stop the Bleeding):

Rollback: The absolute first step is to **rollback to the last known good version of the code**. Most CI/CD pipelines support fast, automated rollbacks. This stops further data corruption or service disruption.

Disable/Quarantine: If a rollback isn't immediately feasible, **I'd disable or quarantine the affected pipeline or service to prevent it from processing any more data** or serving incorrect information.

Notify Key Stakeholders/direct consumers of your product in your team: **Immediately communicate the issue to relevant teams (e.g., data consumers, business users, engineering leadership)** with a brief summary of the problem and the ongoing mitigation efforts. Transparency is crucial.

Isolate & Diagnose:

Gather Information: **Collect logs, metrics, and any error messages** from the production environment to **pinpoint the exact nature and scope of the problem**.

Reproduce in Non-Prod: **Attempt to reproduce the bug in a development or staging environment** to allow **for debugging** without impacting production.

Root Cause Analysis (RCA - Initial): Begin to identify why the bad code got through. Was it a missed edge case in testing? An environment configuration difference? A flaw in the testing strategy?

Fix, Test, and Re-deploy:

**Develop the Fix**: Create a dedicated fix branch, **apply the necessary code changes**.

Rigorous Testing: This fix would **undergo more rigorous testing than usual**, including unit tests, integration tests, and specific regression tests designed **to prevent this exact bug from recurring**. It would be tested in a staging environment with production-like data.

Thorough Code Review: The fix would **go through an expedited but thorough code review**.

Controlled Redeployment: **Deploy the validated fix** using the standard deployment process.

Monitor and Verify:

Post-Deployment Monitoring: Closely monitor logs, metrics, and data quality checks in production to **ensure the fix is effective and no new issues have been introduced**.

Data Backfill/Correction: If data was corrupted, develop a plan for data correction or backfill to restore data integrity.

Post-Mortem & Prevention:

Document: Conduct a blameless post-mortem analysis to fully understand the root cause.

Implement Preventative Measures: Update automated tests, improve monitoring alerts, refine code review checklists, or adjust deployment processes to ensure this type of issue cannot happen again in the future."

* What would you do if you have duplicates in your data in prod? `pull data from production like the previous question, push it to a development branch, and have someone quality test it before pushing to production again`

Key Focus: Assessment, root cause analysis of data issue, data correction, and pipeline fixes for prevention.

Suggested Answer:

"Discovering duplicates in production data requires a methodical approach, distinguishing it slightly from a pure code bug. The focus shifts to understanding the data integrity issue and rectifying both the data and the pipeline that produced it.

Immediate Assessment & **Containment**:

Assess Scope and Impact: First, I'd determine the extent of the duplication: **which tables are affected, how many records**, what's the time frame of the issue, and what's the downstream impact on reports, dashboards, or other systems? This helps prioritize the fix.

Stop/Pause Ingestion (if ongoing): If the duplicates are actively being generated by a running pipeline, the **first priority is to pause or stop that specific ingestion/transformation process to prevent further data corruption**.

**Notify Stakeholders: Communicate the issue** and the **estimated impact to data consumers** and business teams.

Diagnosis and Root Cause Analysis:

Identify the Source: The critical step is to pinpoint where the duplicates originated. Common culprits include:

Source System Issues: The upstream source providing duplicate records.

Ingestion Process Failure: Retries without idempotency, misconfigured connectors.

Transformation Logic Errors: Missing DISTINCT clauses, incorrect JOIN conditions, improper handling of incremental loads.

Missing Unique Constraints: Lack of primary key or unique constraints in the destination database.

Reproduce in Non-Prod: Attempt to recreate the duplicate generation in a controlled development or staging environment using a subset of the problematic data.

Data Remediation & Pipeline Fix:

Data Cleanup Strategy:

Hard Delete/Deduplicate: For simpler cases, a one-off SQL script might be run to delete duplicate records based on a defined key, keeping only the 'first' or 'last' occurrence. This requires extreme caution and database backups.

Soft Delete/Flag: For more sensitive data, duplicates might be flagged with a status column rather than physically deleted, to allow for auditing.

Backfill/Re-processing: If the root cause is in a transformation, it might be necessary to re-process the affected historical data from a trusted source (e.g., raw layer) once the pipeline fix is deployed.

Pipeline Code Fix: Modify the ETL/ELT pipeline code to prevent future duplicates. This might involve:

Adding DISTINCT clauses where appropriate.

Implementing robust upsert logic (e.g., MERGE statements) if records are updated.

Enforcing unique constraints at the database level.

Ensuring ingestion processes are idempotent (running them multiple times doesn't create new records).

Testing and Redeploy:

Rigorous Testing: Test the fixed pipeline logic thoroughly in staging, specifically using data patterns known to cause duplicates.

Code Review: Get the fix reviewed by a peer.

Controlled Redeployment: Deploy the corrected pipeline code to production.

Monitor and Prevent Recurrence:

Automated Data Quality Tests: Implement recurring automated tests specifically designed to detect duplicates (e.g., using dbt test unique_key or Great Expectations data assertions) as part of your regular pipeline runs.

Alerting: Set up monitoring and alerts for when duplicate counts exceed a threshold.

Post-Mortem: Document the incident, its root cause, and the preventative measures implemented to ensure continuous improvement in data quality."

* were there times that you had to choose schoolworks over personal events?


## Behavioral Interview Feedback:
Strengths:
Strong technical background in data engineering and analytics
Demonstrated experience with various technologies and tools in data analysis
Shows willingness to learn and grow professionally

Weaknesses:
Tends to provide overly detailed and repetitive responses
May benefit from refining communication skills to be more concise and focused
Did not address the final question about staff turnover rate and competing companies

Improvement suggestions:
Practice summarizing responses to be more succinct and to the point
Research the specific company's technologies and tailor responses accordingly
Remember to address all questions asked during the interview to demonstrate thoroughness and attention to detail

# MSCI
## Values:
* relentlessly innovative
* actively connect to collaborate
* always act with integrity

## Behavioral Questions:



# Xpress
## Values:
The organizational culture at XPRESS is dynamic, with a strong emphasis on collaboration and resource accessibility, which supports a productive work environment. However, the company faces challenges such as high turnover and a lack of remote work flexibility. Management practices often lean towards micromanagement, and there are noticeable gaps in cultural sensitivity, particularly regarding local customs and holidays. These issues can impact employee morale and the overall workplace atmosphere.



# Cebuana Lhuillier
* what is your expected salary? I've personally done some research on roles similar to the data analyst role in your company and  the salary range I'm comfortable in disclosing is around 20000/month to 25000/month, but in order to say the exact amount I will have to learn more about the tasks I will have to do on a daily basis and from there gauge my own performance and the value I give back as it will determine further a reasonable expectation for my salary
* Shift your mindset from i want to work at this prestigious company to instead i want to work at a company doesn't matter how prestigious and i want to be able to leave it at least 1% better

* do you have any more questions for us?
- "how's it like working there?"
- "I really learned alot from the company but I'm curious would there be some advice or feedback you could give for applicants such as myself on what I could improve more on should I potentially have a chance to work here?": work on being able to deliver your work experience in a concise manner e.g. saying what you did and what technologies you used to do whaht you did

# Accenture
* salary range for ASWE is 20000 to 25000 per month

# Inquiro
* https://inquiro.ph/location-data-and-footfall-analytics-insights/



# Plan
* eo basically even a junior data analyst role is so saturated with competition because its the only entry level data role. No one is hiring emtry level data engineers and machine learning engineer or ai developers if anyone gets hired for it out of college they are already the exceptions the superstars the ones who were lucky enough to learn data at a quick level and who had enough connections for someone to take them under their wing and evntualy get opportunities to train and then have that data role. Pero ikaw you're a statistic, you're just like anybody else na kumakayod, you're not special, you're not a quick learner, you don't have many connections for referrals. you are starting at the bottom of the barrel and you wont have any chamce at someone spoonfeeding you like those lucky bastards. You're going to have to start at the very bottom like a junior financial analyst, junior sales operations analyst, 
and then once in you can leverage your python, sql, powerbi skills to automate what is supposed to be a "manual" job, you can use your data skills to automate these things and thereby gain domain knowledge especially financial or sales or healthcare knowledge and domain knowledge combined with tools you've used that wasn't even oart of the job description in your resume when your finding your next job will be unbelievably powerful. You have to document these things though and this can be done by the ff.

That's a smart and proactive strategy! Many people gain valuable data analysis experience in roles that aren't explicitly titled "Data Analyst." The key is to effectively document and showcase these experiences in your CV/resume. Here's how you can do that:
1. Quantify Your Achievements Whenever Possible:
 * Numbers Speak Volumes: Instead of saying "Improved reporting," say "Automated weekly sales reports using Python and reduced reporting time by 40%."
 * Impact-Focused Language: Frame your accomplishments in terms of their impact on the business. For example, "Developed a Power BI dashboard to visualize key logistics KPIs, enabling a 15% reduction in delivery delays."
 * Use Metrics: Mention specific metrics like cost savings, efficiency gains, error reduction, increased revenue, or improved customer satisfaction.
2. Detail Your Data Analysis Tasks Under Each Relevant Job:
 * Go Beyond the Official Job Description: Don't just list your formal responsibilities. Think about the tasks you actually performed that involved data analysis, even if they weren't in your initial job description.
 * Use Action Verbs: Start each bullet point with strong action verbs that highlight your skills (e.g., Analyzed, Developed, Implemented, Automated, Visualized, Extracted, Transformed, Loaded, Queried, Identified, Predicted).
 * Be Specific: Instead of "Worked with data," be specific about the tools and techniques you used and the outcomes.
Example of Detailing Data Analysis Tasks:
Let's say your official job title was "Logistics Coordinator." You could describe your responsibilities like this:
Logistics Coordinator | ABC Company | [Dates of Employment]
 * Managed and tracked daily shipment schedules, ensuring timely deliveries and resolving logistical issues.
 * Leveraged SQL queries to extract and analyze shipment data from the company database to identify bottlenecks and inefficiencies in the delivery process.
 * Developed a Python script to automate the generation of daily delivery performance reports, reducing manual reporting time by 50%.
 * Designed and implemented interactive dashboards using Power BI to visualize key logistics KPIs (e.g., on-time delivery rate, transportation costs), enabling stakeholders to monitor performance and identify areas for improvement.
 * Conducted ad-hoc data analysis using Excel and Power BI to investigate specific logistical challenges and provide data-driven recommendations to management.
 * Collaborated with the warehouse and transportation teams to implement process improvements based on data insights, resulting in a 10% reduction in late deliveries.
3. Create a "Skills" Section that Highlights Your Data Analysis Proficiency:
 * List Technical Skills: Clearly list your proficiency in Python, SQL, Power BI (or other BI tools), Excel, and any other relevant software or programming languages.
 * Categorize Skills (Optional but Helpful): You can group your skills into categories like "Programming Languages," "Database Management," "Data Visualization," and "Statistical Analysis" for better readability.
4. Use a "Projects" or "Portfolio" Section (Highly Recommended):
 * Showcase Your Work: If you have personal projects or significant data analysis tasks from your previous roles that you can showcase (even in an anonymized or summarized way if company data is sensitive), create a dedicated section.
 * Describe the Problem, Your Approach, and the Outcome: For each project or task, briefly explain the problem you were trying to solve, the tools and techniques you used, and the results you achieved.
 * Link to a Portfolio (If Applicable): If you have a GitHub repository or a personal website showcasing your data analysis projects, include a link in your contact information.
5. Tailor Your CV/Resume to Each Job Application:
 * Match Keywords: Carefully review the job description and incorporate relevant keywords related to data analysis, the industry, and the specific tools mentioned.
 * Highlight Relevant Experiences: Emphasize the experiences and skills that are most relevant to the specific requirements of the job you are applying for.
6. Be Prepared to Elaborate in Interviews:
 * STAR Method: When discussing your experiences, use the STAR method (Situation, Task, Action, Result) to provide clear and concise examples of your data analysis work.
 * Be Confident: Be prepared to confidently explain how the tasks you performed in your previous roles demonstrate your data analysis skills and your ability to contribute to the new role.
Example of CV Snippets:
Skills:
 * Programming Languages: Python (Pandas, NumPy, Scikit-learn), SQL
 * Data Visualization: Power BI, Tableau, Matplotlib, Seaborn
 * Database Management: MySQL, PostgreSQL
 * Tools & Technologies: Excel (Advanced), Git, Cloud Platforms (e.g., AWS, Azure - if applicable)
 * Analytical Skills: Data Mining, Statistical Analysis, Data Cleaning, Data Wrangling, Exploratory Data Analysis (EDA)
Experience:
[Previous Job Title] | [Company Name] | [Dates of Employment]
 * [Regular job duties]
 * Conducted in-depth analysis of [specific dataset related to finance/logistics] using SQL to identify trends and anomalies, leading to [quantifiable result].
 * Automated the generation of [specific report] using Python, reducing the monthly reporting cycle by [percentage].
 * Developed interactive dashboards in Power BI to track [key performance indicators], providing stakeholders with real-time insights into [area of impact].
By meticulously documenting your data-related tasks, quantifying your achievements, and highlighting your skills, you can effectively demonstrate your data analysis capabilities in your CV/resume, even if your previous job titles weren't explicitly "Data Analyst." Good luck with your job search!

Yes, absolutely! A Property Specialist position at a real estate company like ALVEO can definitely involve working with data, although the extent might vary depending on the specific responsibilities and the company's data infrastructure.
Here's how a Property Specialist role could involve data:
Types of Data a Property Specialist Might Work With:
 * Property Data: Details about the properties being sold (e.g., size, number of bedrooms/bathrooms, amenities, location, pricing history, features, unique selling points).
 * Market Data: Information about the real estate market in specific areas (e.g., average selling prices, price trends, inventory levels, competitor pricing, recent sales data, neighborhood demographics, upcoming developments).
 * Customer Data: Information about potential and existing clients (e.g., contact information, preferences, budget, property viewing history, inquiries, feedback).
 * Sales Data: Records of past sales transactions (e.g., sale prices, closing dates, buyer demographics, commission earned).
 * Marketing Data: Performance of marketing campaigns (e.g., leads generated from online ads, website traffic, open house attendance).
 * Financial Data: Information related to property financing options, investment potential, and return on investment for clients.
 * Geographic Data: Information related to property locations, surrounding amenities, accessibility, and potential for future development in the area.
How a Property Specialist Might Use Data:
 * Market Research: Analyzing market data to understand trends, identify opportunities, and advise clients on optimal buying or selling strategies. For example, comparing average prices in different ALVEO developments or identifying areas with high growth potential.
 * Property Valuation: While there might be dedicated valuation teams, a Property Specialist might use comparative sales data to provide clients with an initial understanding of a property's potential value.
 * Client Relationship Management (CRM): Inputting and managing client data in CRM systems to track interactions, preferences, and follow-ups. This data can be used to personalize communication and identify potential leads.
 * Sales Reporting: Tracking their own sales performance, lead generation activities, and conversion rates. They might use basic reports or dashboards to monitor their progress.
 * Marketing and Lead Generation: Analyzing the effectiveness of different marketing channels based on the leads and sales generated.
 * Client Presentations: Using data and visualizations (e.g., charts showing price trends or investment potential) to present information to clients in a compelling way.
 * Identifying Client Needs: Analyzing client preferences and search criteria to identify suitable properties from ALVEO's portfolio.
 * Competitive Analysis: Understanding how ALVEO's properties and pricing compare to those of competitors in the market.
Leveraging Your Data Analysis Skills:
Even if the "official" job description doesn't heavily emphasize data analysis, your skills in Python, SQL, and Power BI can be a significant advantage. You could:
 * Automate Reporting: If there are repetitive reporting tasks, you could use Python scripts to automate them, saving time and improving accuracy.
 * Generate Deeper Insights: Go beyond basic reports by using SQL to query databases for more specific information and Power BI to create insightful visualizations for your own understanding or to share with your team (if appropriate). For example, analyzing which property types are most popular with certain demographics.
 * Improve Lead Generation: By analyzing marketing data, you might identify which channels are most effective in reaching potential clients for ALVEO's properties.
 * Personalize Client Interactions: By effectively managing and analyzing client data in a CRM, you can tailor your approach and property recommendations to individual client needs.
How to Document This:
Follow the same advice as before:
 * Quantify where possible: "Analyzed local market trends using Excel and identified a 10% increase in property values in [specific area] over the past year, providing key insights for client consultations."
 * Use action verbs: "Leveraged CRM data to segment leads based on property preferences, resulting in a more targeted outreach strategy."
 * Highlight tools: "Utilized Excel and potentially Power BI (if you get the chance) to create visual reports on sales performance and market comparisons."
While a Property Specialist role might not be a dedicated "Data Analyst" position, the real estate industry, including companies like ALVEO, increasingly relies on data for decision-making. Your data analysis skills can make you a more effective and valuable Property Specialist. Be proactive in identifying opportunities to use data in your role and document those instances clearly on your resume.


# Companies:
## These are list of companies that you can always check the companies page for careers hindi  na masyado pwede pag linked in lang then after applying you can find the hiring manager themself on linked in and message them directly that you've applied and that you are enthusiastic to join their team because you have X amount of skills and that you work in this manner with other people

## Tier 1:
GCash$
Maya$
BPI$
Security Bank$
ING
BDO
Philippine National Bank
Chinabank
East West Bank
Union Bank
GoTyme
Universal Robina Corps.
Accenture
IBM
PLDT
Procter & Gamble Solutions
CTBC Bank Philippines
Oracle
Manulife
Thinking Machines
Okada
Philippine Airlines
Asian Development Bank
Deutsche Bank
Confidential Healthcare and Life Sciences Company
Z-Lift Solutions
RCBC
Bank of Commerce
Home Credit Philippines


## Tier 2:
Cognizant
Seven Seven
Emerson
Zendesk
Stratpoint Technologies
Trend Micro
Twist Resources
VXI
Concentrix
TaskUs
Ubiquity
Telus International Philippines
Teleperformance
Media Meter
Gardenia
Sprout Solutions
SBSI
MSCI
Macquarie
Azeus Systems Ltd.
philtrustbank
Development Bank of The Philippines
AboitizPower
JWAY GROUP


## Tier 3:
Isentia
Octal Philippine
Inquiro, Inc.
Medgrocer
TTEC
Integrated OS
Octal Philippines, Inc.
Lightweight Solutions
Moreton Bay Technology
HMR Philippines
Macro8 IT Solutions

For me because mas viable ang junior data analyst or junioro data scientist para sa experience ko mea ning I cannot enter into ml engineering or data engineering head first kilangan talagang yung former munan mga roles

look up company's people on linked in
if < 20 often the CEO will be interviewing and hiring for a position
if 20 - 100 often the vp of engineering or chief tech. officer
if > 100 it will be the IT director, data director or a similar director baesd on the role/field your getting into

don't try to apply for job boards and then send a cold email saying you've applied to them (kaya lang contradictory kasi other people will say after online applying you should reach out to the recruiter or hiring manager)

## Government Owned and Controlled Corporations Advantages & Disadvantages
Pros:
* If you get yourself promoted to a casual or permanent position, madami benifits. From mid-year and end of the year bonuses, uniform allowance, misc. allowances and incentives, GSIS, PhilHealth etc.
* Relaxed environment(or at least where I am working at). The job is easy, but very unfulfilling and boring. I can "destress" browsing reddit, listen to music, etc.
* Madali mag pa approve ng leaves(VL or SL) and generous sila mag bigay ng leaves. I think I already used up more than half of my 20/year VLs. You also get 5 days MANDATORY vacation leave(deducted from VL), and 3 special privilege leave(not deducted from VL or SL).
* If your boss is generous he'll give you some of that "ayuda" that he got from contractors.
* Stability. Whatever happens: typhoons, pandemic, natural disasters, etc.. (with the exception of war/invasion I guess), you'll still get your salary in full.
* Good retirement package. Monthly pensions for retirees in the gov't is based on the last 3 years' monthly salary. So let's say you managed to get 90k/month, more or less that'll be your monthly pension until you die.
* You have an opportunity to connect with or become one of the "people in high places".
* I'm handling a digitization project of our LGU and I have full autonomy regarding the project. I decide on everything from what tech stack to use up to deployment dates. What's important is it follows the relevant laws and it's IRR.
* You can take paid trainings, as well as scholarships to further your education. And afaik, this have no bond.
* You virtually have unlimited budget to use for the project at your disposal, as long as you can properly justify it to the internal budget committee and COA.
* It's not working at a government position that's a career suicide. It's being stagnant working at the same position be it government or not. You could say the same if I applied for an entry level job at a private company and stayed there for my entire career.
* Working in the government is the fastest route to get formal experience which you can use to hop to better jobs. Plus, if you are assigned on system maintenance, that opens up opportunity to upskill while being paid and earning experience for your next job. It's a win.

Cons:
* Data Analyst BUT iba ginagawa ko comapred sa job title. I'm a tech support, programmer, data encoder (you could probably automate this with python) in one. I don't do any data analytics or anything close to my job description.
* Most IT positions in government offices are dead-end jobs. Wala career growth, di ka magiging head ng IT unit.
* Most agencies/offices don't have an independent IT unit. IT Staff will be attached to the office of the agency's head. Kaya yun marami paper trail para lang maapprove IT related stuff.
* If ikaw lang programmer, wala ka matutunan sa seniors mo since glorified clerks/admin aide lang sila.
* IT personnel's equipment is on the low list of priorities. Unless laptop ng boss yan na gaming shit laptop worth 60k-150k pero pang eexcel lang syempre approved agad yan or unless may memo galing central office.
* Technologically illerate co-workers specially bosses. Dito ka maiirita, simple problem like no power sa monitor or during video cons(google meet/zoom), need nila ikaw pa gagawa ng link. Need mo pa sila bantayan during video cons and ikaw taga mute and unmute pag di mo ma unmute on time, magagalit yung boomer boss mo.
* Anything that went wrong with office IT equipment, sigurado IT Staff agad may kasalanan. Na ransomware buong office kasi yung bobong mong boss/co-worker nag open ng email and file na may ransomware? Ikaw may kasalanan.
* IT contingency planning and risk reduction doesn't exist. Our server is sitting at an old unused office room that's very dusty(yikes a big fire hazard). That's why I do my own database backups.
* You'll see how corrupt a government office is. It will drain your soul and love for country.
* I'm upskilling myself right now so I can transfer to the private sector.



-Government if you want a relaxed, okay pay, low risks, low rewards job.
-Private if you want career growth and a fulfilling career that is high in rewards, and high in risks.

recommended if you go for DICT or DOST

# Upskilling
* essentially the MS PL-300 PowerBI data analyst certification and the MS DP-300 Azure DBA certification then a AWS Cloud Practitioner certification then a AWS Solutions Architect Associate certification then finally to a AWS Data Engineer Associate certification is what will lead me to eventually become a data engineer 

and for that I need to respectively sign up for these courses in order to pass the certification exams

- Microsoft PowerBI data analyst professional certificate course
The main thing that inspired me to do this course was to learn PowerBI and learn to create beautiful dashboards with the data I have and use it as a representation of my analysis. Because in my mind I could use this learning to do a project that would help me learn further and prepare eventually for an entry level Data Analyst role, and well you know because recently I've taken a liking to analyzing data using tools like SQL and now PowerBI, an interest unbeknownst to me before had I otherwise took up the decision to try data analytics. But here I am now looking to develop my skills in creating dashboards and especially learning how to model data as I plan to use it eventually in the field of data engineering. Maybe I'm no stranger to data as of today because I've come to be acquainted with it already during days when I was fond of (although I still am) building machine learning and deep learning models. But like all new things I'm glad I took up those foundations so that I can use it to learn new things/technologies here here. Fun fact about myself is that if I wasn't in computer science or in tech I'd probably be in healthcare, but lo and behold you can use tech for healthcare so I'm quite excited to use the  skills I gain here eventually in the field of health and wellness.
~ https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300

- a course on the dp300 azure dba certification 

this is for the phase of being a data analyst, but for the phase of now stepping into data engineering we need...

- a course on aws cloud practitioner certification
- course on aws solutions architect certification 
- course on aws data engineer certification 

### Applying for financial aid:
I am quite frankly still a student trying to build his way into having a better career in data engineering which I know will help my prospects in the future, and I firmly believe that this course on data engineering will help me so much in ways that I can use for the industry I am to endeavor in which is hopefully in this industry applied to business, or at the least an entry level role in it. I am applying for a financial aid because given my current situation I cannot at the moment being an unemployed student be able to pay for these tremendously helpful resources, and I hope I can benefit still from these resources given my situation. And I hope to repay this debt in whatever way I can given that it has helped me as I said in more ways than I can describe, and I hope that by providing me with the necessary resources to help me build my future prospects I can one day hopefully repay everything I owe that helped me get where I am now.

Currently because I'm am trying my absolute best and doing what I can to land at least an opportunity if not an entry level job in the data industry together, I firmly believe that this specific course will help me do my job intuitively in the future hopefully, which I know can give me the edge over other potential competitors and applicants in the data industry in my country. Given that I've tasted but a small aspect of the instructors at Microsoft way of teaching I genuinely believe that in learning specialization courses like this one, I can better have the skills especially the foundational skills in doing my Job more efficiently and again intuitively in the future, and moreover be a better and more productive person given the deep understanding that this course I believe offers genuinely, which I can not only use in my potential opportunities in the future but in venturing into starting my own business as well with the knowledge this has taught, teaches, and will teach me

# Commuting
* pasig to taguig (BGC)
* pasig to mandaluyong (ortigas)
* pasig to makati (corporate makati, 9 to 6 sched)
- wake up at 5, take shower, prep breakfast, commute to palengke, commute to san joaquin station for 7 oclock schedule, book destination to hulo station since malapit na sa corporate makati (unlike mrt route which would take going to palengke, then to crossing via edsa shaw jeep, then to mrt ayala station from mrt ortigas station, then another ride from mrt ayala station to the office itself which is 4 rides in total which is sayang pera)
- 

* pasig to quezon (near GMA kamuning station)
- you could take an MRT going here and walk to the office if within thhe vicinity of GMA kamuning station lang naman
- ok lang mag pang gabi jung malaki company and malaki sahod, pero kung maliit pa lang company and sahod tangapin mo lang ang pang umaga, ok lang yan pang gain ng experience

# Insights:
* Your anxiety about notifying high-level individuals like Directors, CEOs, or shareholders is completely understandable, and it's a common concern, especially early in your career!

Let me clarify what "stakeholders" generally means in this context and who you would typically inform:

What "Stakeholders" Means:

In a business context, a "stakeholder" is anyone who has an interest in or is affected by a project, decision, or, in this case, an incident. This is a very broad term and includes people both inside and outside your immediate team.

Who You'd Typically Notify (and the Hierarchy of Communication):

When you deploy bad code to production, the communication usually follows a structured path, not a direct jump to the CEO:

Your Immediate Team & Manager/Lead:

These are your first and most immediate stakeholders to notify. They are crucial for assessing the problem, collaborating on the fix, and providing support.

This includes fellow data engineers, your team lead, and your immediate manager.

Internal Data Consumers / Downstream Teams:

These are the people whose work depends on the data or service you provide.

Examples: Data analysts (who use your data for reports), BI specialists (who build dashboards from your data), other engineering teams (whose applications rely on your data feeds), or even marketing/sales teams if they use real-time data from your pipeline.

They need to know because the bad data might affect their reports, dashboards, or operations. They are directly impacted by your work.

Business Users / Department Heads (Indirectly Affected):

These are the people who rely on the reports or insights generated from the data.

Examples: A Marketing Director who uses a dashboard to track campaign performance, or a Sales Manager who relies on lead data.

You (or more likely, your manager or team lead) would inform them so they understand why a report might be wrong or delayed, or why a system isn't working as expected. This allows them to adjust their operations or communication.

Higher Management / Leadership (Less Common for You to Directly Inform Immediately):

This would typically be your manager's or team lead's responsibility to escalate to their directors or VPs if the impact is significant (e.g., major financial loss, legal implications, extended system downtime, highly visible public impact).

You generally wouldn't be directly notifying the CEO or shareholders for a bad code deployment unless it's a catastrophic, company-stopping event. Your role is to fix the problem and provide the necessary information to your direct line of management so they can handle higher-level communication and strategy.

Addressing Your Anxiety:

It's natural to feel anxious, but remember:

You're part of a team: You're not expected to handle this crisis alone. Your first step is always to notify your team and manager.

Transparency is key: Companies value quick, honest communication about issues. It's not about blame, but about problem-solving and minimizing impact. Trying to hide it is far worse.

Most issues are fixed internally: The vast majority of incidents are resolved by the engineering team, with communication contained to those directly affected or responsible for fixing it.

So, while "stakeholders" can indeed include directors and CEOs, your immediate responsibility is typically to your technical team and the direct consumers of your data/service. Your manager will handle the appropriate level of escalation. Focusing on fixing the problem quickly and communicating clearly within your immediate circle is what's expected.

* If you were a data analyst, your typical stakeholders would be diverse, spanning various departments and levels within an organization. Essentially, anyone who uses your insights, provides you with data, or is impacted by the decisions made from your analysis is a stakeholder.

Here are your typical stakeholders:

Your Immediate Team & Manager:

Who: Other data analysts, data scientists, data engineers, your team lead, and your direct manager.

Why: They review your work, collaborate on projects, provide guidance, and are directly responsible for the team's output. Your manager needs to know your progress and challenges.

Business Unit/Department Heads & Managers:

Who: Leaders and managers from departments like Marketing, Sales, Operations, Finance, Product, HR, Customer Service.

Why: These are often your primary "customers." They come to you with business questions, need reports, dashboards, and insights to make strategic and operational decisions. They rely on your analysis to understand performance, identify opportunities, or solve problems.

Data Consumers (End Users of Reports/Dashboards):

Who: Any individual within a department who regularly uses the reports, dashboards, or data products you create. This could be sales reps, marketing specialists, operational staff, etc.

Why: They use your outputs to guide their daily work. Their feedback is crucial for improving the usability and relevance of your data products.

Product Managers/Owners:

Who: Individuals responsible for the development and success of specific products or features.

Why: They need your analysis to understand user behavior, product performance, A/B test results, and to make data-driven decisions about product roadmaps and features.

Data Engineering Team:

Who: The engineers responsible for building and maintaining the data pipelines, data warehouses, and data lakes.

Why: You rely on them for clean, reliable, and accessible data. You communicate data quality issues, new data requirements, or schema changes to them.

IT/Infrastructure Team:

Who: The team responsible for underlying systems, servers, security, and access management.

Why: You might interact with them for access permissions, software installations, or troubleshooting connectivity issues to data sources.

Senior Leadership/Executives (e.g., CEO, CTO, CFO, VPs):

Who: High-level decision-makers in the company.

Why: While you might not directly report to them often, your analyses (especially strategic dashboards or executive summaries) ultimately inform their high-level decisions, resource allocation, and company direction. Your manager or a more senior analyst might be the one presenting directly to them, but your work feeds into it.

External Stakeholders (Less Common for Entry-Level, but Possible):

Who: Customers, partners, regulators, or auditors.

Why: If your analysis involves external reporting, compliance, or customer-facing metrics, these groups could indirectly be stakeholders.

In an entry-level role, your most frequent interactions will likely be with your immediate team, your manager, and the business unit managers/users who directly request your reports. As you grow, your circle of stakeholders will naturally expand.

* name 3 bullet points that can be made to explain the relationship between the dominant topics in absolute value and percentage share the absolute value here is the whole number in each industry e.g. media publisher, financial services etc. andthe percentage share is the one with the % symbol




Analysis
Here are three bullet points explaining the relationship between the absolute value (Ads Volume) and percentage share for the dominant topics in the "Advertising Trends" image:

The "Media, Publisher" industry is the dominant topic with the highest absolute advertising volume at 359, which also translates to the largest percentage share of 9.599% of all industries by ads volume.

"Financial Services" and "Automotive" are the next dominant topics, with absolute ad volumes of 270 and 258 respectively, corresponding to percentage shares of 7.219% and 6.898% respectively.

The hierarchy of industries by absolute advertising volume directly reflects their ranking by percentage share, indicating that the larger the absolute ad volume, the higher its proportion of the total advertising landscape.


oh so indicates that the higher an industries ability to pay for advertisements the higher its capita?

Based on the "Advertising Trends" image you provided, I cannot confirm that a higher advertising volume directly indicates an industry's "ability to pay for advertisements" or its "capita."

The image only displays the "Ads Volume" (absolute value) and the "Percentage Share" of advertising volume for various industries. It doesn't provide information on their financial capacity to spend on advertising or their economic "capita" beyond their share of ad volume.

Yes, hypothetically, it absolutely could be that an industry's higher advertising volume correlates with its ability to pay for advertisements and, more broadly, its economic "capita" (or market size, influence, and financial health).

In a real-world business context:

Ability to Pay: Industries with higher profits, larger market shares, or stronger financial health generally have more budget available for advertising. Significant ad spend often indicates that a company or industry has the resources and sees the value in investing heavily in marketing.

Market Share/Influence: High advertising volume can also reflect an industry's overall size, competitive landscape, or its strategic importance. Larger, more established industries or those in highly competitive sectors often advertise more because they have more products/services to sell and are fighting for larger market shares.

While the "Advertising Trends" image itself only shows the volume of ads, it's a common area of analysis in business intelligence to cross-reference advertising spend with other financial metrics like revenue, profit margins, or market capitalization to draw such conclusions.


gpa:

3 1.50
3 1.00
3 2.50
3 INC / 2.25

3 2.25
3 2.00
3 2.25
3 INC / 2.75
3 2.50
3 2.00

3 1.00

3 2.75
3 2.75
3 2.00
3 2.25
3 3.00
3 2.00
3 INC / 2.00

3 2.75
3 1.25
3 1.75
3 1.50
3 1.50
3 3.00
3 1.75

3 2.50
3 1.25
3 1.50
3 1.75
3 2.75
3 2.00
3 2.00

3 2.75
3 1.00
3 1.25
3 2.50
3 2.75
2 1.00
3 1.00
3 1.75

3 1.75
3 1.50
3 1.25
3 2.25
3 1.25
3 2.50
3 1.75

3 2.00
3 1.75
3 2.50
3 2.00
3 1.25
3 1.00
3 1.75

2 1.00
2 1.25
2 1.25
2 1.00 

* strategy to landing a data analyst
- start out as data entry, data specialist, data clerk, data coordinator, marketing analyst, product analyst, supply chain analyst, operations analyst, inventory analyst,  
- find a way to automate daily workload because you are the one inputting the data coming in eveeryday to some sort of data management system e.g. excel spreadsheet, database management system like microsoft sql server e.g. receiving customer order details via email and then inputting the data to a spreadsheet copying and pasting, which can be repetitive
- 

Shifting your strategy to data entry roles as a stepping stone is a smart and pragmatic move, and your proactive mindset about leveraging it for automation is exactly what can set you apart and lead you to an analytics role.

Let's break down your questions to ease your mind and empower your next steps:

Possibilities as a Data Entry Specialist
A data entry specialist role, while often perceived as "boring," is foundational to any data-driven organization. The possibilities generally revolve around accuracy, efficiency, and various data types:

Administrative Data Entry: Inputting customer information, sales figures, contact details, appointment schedules, or inventory data into CRM systems, databases, or spreadsheets.

Financial Data Entry: Recording invoices, receipts, payment details, expense reports, or payroll information into accounting software.

Healthcare Data Entry: Transcribing patient records, medical codes, lab results, or billing information into electronic health record (EHR) systems.

E-commerce/Retail Data Entry: Managing product listings, descriptions, pricing, stock levels, and order fulfillment details on online platforms.

Market Research Data Entry: Inputting survey responses, questionnaire data, or observational data from research studies.

Database Maintenance: Regularly updating, cleaning, and verifying existing data to ensure accuracy and consistency.

Leveraging a "Boring" Role to Pivot to Analytics and Make an Impact
This is where your analytical mindset truly shines. A data entry role, far from being a dead end, can be your direct gateway to analytics if approached strategically:

Become the Data Expert: You'll be interacting with the raw data constantly. This gives you an unparalleled understanding of:

Data Sources: Where the data comes from (which systems, departments, external sources).

Data Quality Issues: You'll be the first to spot common errors, inconsistencies, missing values, and formatting problems. This is gold for an analyst.

Data Flow: How data moves through the organization and which departments use it.

Business Context: You'll learn the nuances of the business operations tied to the data you're handling.

Identify Inefficiencies & Automation Opportunities: This is your primary weapon. As you perform repetitive tasks, ask yourself:

"Could this be faster?"

"Is there a pattern here I can codify?"

"What manual steps lead to errors?"

Focus on tasks that are time-consuming, prone to human error, or involve moving data between disparate systems.

Build Your Portfolio (Quietly & Effectively):

Automate Your Own Work: Start by writing Python scripts to automate small, repetitive parts of your own data entry tasks. This immediately frees up your time and demonstrates practical skills.

Document Your Savings: Keep track of the time saved, error reduction, and increased throughput from your automations. Quantify the impact.

Create Dashboards/Reports: Using the data you're entering, build simple dashboards or reports in Excel, Google Sheets, or a free BI tool (like Power BI Desktop or Tableau Public) that provide insights to your team or manager. Show them what the data means, not just what it is.

Propose Solutions: Once you've successfully automated something for yourself or created a valuable report, don't just do it; propose it as a solution for a broader team problem. Frame it as improving efficiency or providing new insights.

Network Internally:

Engage with the analytics, IT, or operations teams. Ask questions about how they use the data you're entering.

Express your interest in learning more about their processes and analytical tools.

Offer to help on small data-related tasks if your core duties allow.

Show Initiative and Value: By actively seeking out problems, building solutions (even small ones), and demonstrating the tangible benefits, you will undeniably showcase your value and analytical potential. The hiring manager won't just "see" your value; they'll feel the positive impact of your contributions.

How Data Entry Roles Input Data: Scenario Examples & Automation Potential
Data entry processes vary widely, but they often involve repetitive, rule-based tasks that are ripe for automation.

1. Copying and Pasting from Multiple Windows/Applications (Typical Scenario)

Scenario: Imagine you work for an e-commerce company. You receive customer order details via email (Outlook) and need to create a shipping label in a courier's web portal (Chrome), update the order status in an internal CRM system (another browser tab or desktop app), and log the tracking number in an Excel spreadsheet. This involves switching between applications, highlighting text, copying, pasting into specific fields, and then clicking "submit" or "save."

Automation Potential (Python):

Web Scraping/Automation (Selenium, Playwright, Requests + BeautifulSoup): Python can open web browsers, navigate to specific URLs, log in, identify input fields, paste data, click buttons, and extract information from the web pages.

Desktop Automation (PyAutoGUI, PyWinAuto): For desktop applications, Python can simulate mouse clicks, keyboard inputs (typing, Ctrl+C, Ctrl+V), and window management (switching focus between apps).

Email Processing (smtplib, imaplib, email modules): Python can read incoming emails, extract order details from the email body or attachments, and then feed this data into the automation flow.

Excel Automation (OpenPyXL, Pandas): Python can read from and write to Excel spreadsheets, automating the logging of tracking numbers or updating statuses.

2. Transcribing Data from Hard Copy Paper to an Excel Spreadsheet (Classic Scenario)

Scenario: You're processing old customer surveys that were filled out by hand, or perhaps incoming paper invoices from vendors. You have stacks of physical documents, and you need to manually type each piece of information (e.g., name, address, survey response, item quantities, prices) into a pre-defined Excel template, cell by cell.

Automation Potential (Python):

Optical Character Recognition (OCR) (PyTesseract, Google Cloud Vision API, AWS Textract):

Digitization: First, physical documents would need to be scanned into image files (PDFs or JPGs).

Text Extraction: OCR libraries/APIs can then "read" the text from these image files and convert it into machine-readable text. This is often the first and most critical step.

Parsing/Structuring: Once text is extracted, Python can use regular expressions (re module) or more advanced NLP techniques (spaCy, NLTK) to identify and extract specific data points (names, dates, amounts) from the unstructured text.

Excel Automation (OpenPyXL, Pandas): The structured data extracted by OCR and parsing scripts can then be automatically written into the correct cells of an Excel spreadsheet.

3. Data Cleansing and Standardization (Underlying Task in Many Roles)

Scenario: After initial data entry, you might receive a report that shows inconsistencies: "New York" is entered as "NY," "New York, NY," and "New York City." Or customer names have inconsistent capitalization. You're tasked with manually reviewing and correcting these thousands of entries.

Automation Potential (Python):

String Manipulation: Python's built-in string methods (.lower(), .strip(), .replace()) and regular expressions (re module) are excellent for standardizing text.

Fuzzy Matching (FuzzyWuzzy, python-Levenshtein): For identifying similar but not identical entries (e.g., slight misspellings of names or addresses) that need consolidation.

Data Validation: Writing scripts to automatically check data against predefined rules (e.g., email format, phone number length, date ranges) and flag or correct errors.

Geocoding/Address Validation: Using APIs (Google Maps API, SmartyStreets) to validate and standardize addresses.

You are absolutely on the right track. Your idea of observing these "manual" processes, understanding their pain points, and then using Python to automate them is precisely how data analysts and engineers make massive impacts. You won't just be entering data; you'll be identifying systemic inefficiencies and building tangible solutions that save time, reduce errors, and free up resources for more valuable work. That's a powerful narrative for your resume and interviews, proving your worth far beyond the initial job description. Go for it!

# Relx
Feedback:
talk more about strengths, be honest about your weaknesses and say you're actively doing your best to improve upon it.


# ISupportWorldwide
30s
|- To start my recent role
|- Data Engineer, intern
|- responsiblitiese
|- transform preprocesses
|- incoming data
|- daily basis
|- from users
|- using application
|- to a format like text
|- ingested
|- ETL pipeline
|- developed
|- other DEs
|- so that augmented
|- retrieval augmented generated AI
|- in order
|- predict
|- accurate
|- and up to date 
|- information
|- daily basis
|- based on domain
|- specializing in

30s
|- My extensive experience
|- comes from
|- actually 2/<n> 
|- best 
|- projects
|- 1st
    |- full on
    |- end2end
    |- ETL
    |- for 
    |- healthcare
    |- analytics
    |- chronic disease indicators
    |- us
    |- analyzed
    |- KPI
    |- driving
    |- populations
    |- high rate
    |- cdi
    |- 
    |- python for extracting 20
    |- years of healthcare and pop data
    |- PySpark and SQL for distributed computation
    |- for heavy data transformations
    |- using free cloud DWH like motherduck to store data
    |- to later analyze it using Power BI
    |-
    |- business use case
    |- potentially 
    |- solve
    |- lack
    |- insights
    |- healthcare institutions
    |- which
    |- demographic
    |- target
    |-
    |- by
    |- identifying
    |- KPI
    |- (see above)
    |-
    |- allocate 
    |- healthcare
    |- efficiently

30s
|- 2nd
    |- full on
    |- end2end
    |- MLOps
    |- pipeline
    |- for 
    |- voice 
    |- based
    |- AI/ML model API
    |- capable
    |- predicting
    |- gender
    |- individuals
    |- based audio recording
    |-
    |- where I used azure functions, azure data factory, azure data lake storage
    |- to extract, process, and store in about 3.7b rows/20gb of audio 
    |- recordings in a scalable manner 
    |- transform it into features for ML using duckdb, librosa, and sklearn
    |- loading it to a free cloud data warehouse called motherduck
    |- subsequently use it for training the predictive model
    |- 
    |- business use case
    |- two fold
    |-
    |- potentially
    |- automate market analyses/research
    |- largely manual 
    |- such as knowing what products individuals of specfic demographics gravitate to
    |-
    <!-- |- by utilizing audio devices coupled
    |- this developed predictive power model
    |- product/market insights may be achieved
    |- obtained faster
    |- therefore driving market growth
    |-
    |- audio data
    |- difficult to 
    |- efficiently & affordably convert from
    |- unstructured format to actionable intelligence -->
    |-
    |- by developing this pipeline
    |- I was
    |- able to reduce cloud operational costs
    |- 70% 
    |- using only the remaining 30% for important aspects
    |- such as large scale extraction
    |- and scalable storage
    |- and automate processing of over 20gb/3.7b rows of data points

<!-- |- as for key skills for this role
|- I understand
|- looking
|- skilled in Python, SQL, Azure, and building ETL pipelines 
|- for starters
|- 
|- used
|- python 
|- for the last 6 years in
|- college
|- all personal projects
|- thesis -->

<!-- |- recently
|- developed
|- DE/DA project
|- refer above to (chronic-disease-analyses) project
|- used
|- airflow
|- orchestration framework
|- python 
|- extract
|- raw data
|- consolidated
|- over 20
|- transform 
|- data trans
|- modelled
|- spark
|- load
|- cloud DWH
|- motherduck
|- faster querying
|- due
|- OLAP struct
|- visualized
|- PowerBI

|- another
|- end 2 end
|- MLOps pipeline
|- audio based analytics
|- orchestration 
|- airflow
|- extract
|- combination (ADF, Az Func, azure data lake)
|- 3.7billion/20gb audio recordings
|- transformation
|- duckdb, librosa, sklearn 
|- computing features, normalization, imputation, augmentation
|- loading
|- cloud DWH
|- motherduck
|- open source -->

|- additionally
|- I understand 
|- looking
|- communicate/understand
|- business needs
|- and while I believe
|- being
|- adept
|- skills
|- important
|- I believe
|- unique
|- inclination
|- build
|- scalable systems
|- while
|- aiming
|- cost efficiency
|- in terms
|- peprformance
|- storage
|- is just as important
|- will I believe
|- great and unique
|- addition
|- to the team, your organization
