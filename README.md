# SuperSurvey
A survey application for a Cloud Computing Course at Innopolis University
## Getting Started
These instruction will help you to set up a project environment on your local machine
### Prerequisites
* [Python interpreter of version 3.5](https://www.python.org/downloads/release/python-354/)
#### Installing
* Clone a repository into chosen directory:
```
git clone https://github.com/KKhanda/SuperSurvey.git
```
* Install required modules
```
pip install -U pip
pip install -r requirements.txt
```
#### Running in docker

```
docker-compose build
docker-compose up
```

#### Setup initial data

Run following command to add 3 basic questions

`python manage.py shell < add_initial_questions.py`
