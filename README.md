# Manage-Hackathon
A little about the Project: this is a general Hackathon Management System.

First Participants need to fill out the registration form for the event that is currently going on.

After that, they will be provided with an email and password in the leader's email.

After logging in using the credentials, the team of hackers will have their own dashboard.

It will display all the general information that teams need to know during the hackathon.

Like their mentors' timing, event schedule, etc.


First, create a virtual environment using the following command
```
virtualenv env
```
Then activate the environment
```
source env/bin/activate
```
Navigate to the directory where there is a requirement.txt file. After that run the following command to install all required
dependencies
```
pip install -r requirements.txt
```
Than run
```
python3 manage.py makemigrations
python3 manage.py makemigrate
python3 manage.py runserver
```
or you can run 
```
./mmr.sh
```
