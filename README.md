# Manage-Hackathon

First create a virtual envirnoment using following command
```
virtualenv env
```
Than activate the environment
```
source env/bin/activate
```
Nativate to the directory where there is requirement.txt file. After than run follwoing command to install all required
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
or you can simply run 
```
./mmr.sh
```
