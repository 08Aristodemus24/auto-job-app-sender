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

# Final interview might consist of the common...

## Why do you want to work here?
I think the idea of collecting and operating on large swathes of data
and using data from news articles, technological trends, medical data to allow other clients
to make their own decisions based on the data we could process for them really caught my eye
because in all honesty I'm just someone who's fond of doing so and i think doing it on the job will be a
great learning experience 

##   Why should we hire you?
In all humility apart from obvious skills, I draw from my personal experience of quite frankly being always a lone developer
if there is such a term, and if I'm given the opportunity here to collaborate with a team of like minded individuals someone as wanting to grow just as much as me, and wanting to contribute just as much as me, I'll be driven to do my best to give back to this organization by doing my due diligence to always committing to the tasks at hand 

# Describing their workflow:
* ung meron naman impediments like yung siguro nahihirapan sa tasks ganun kilangan iresolve kasi every week dapat may milestone na natatapos
* they use agile methodology to develop applications, scrum to be specific. 2 - 4 weeks sprints. After these 2 or 4 weeks may natatapos na na feature ng application or nakapagpush na sa dev then into production branch. As a result some tools you really need to learn are docker for containerization, pulling from development branch and then merging in this branch
* product backlog - list of tasks for all sprints
* sprint backlog - specific tasks in the product backlog for a specific sprint lasting 1 to 4 weeks. E.g. for week 1 these are the tasks
* after completing tasks in the sprint after say 1 week there will be a presentation of your work to your colleagues