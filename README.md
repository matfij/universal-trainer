## Universal trainer
One project to rule all the Kaggle challenges

### Requirements
 - Python 3.6+ (3.9 was used for this project)
 - Docker, docker-compose, Make*
 - Upgrade pip: `pip install --upgrade pip`

### Quick start*
 - make docker.build
 - make docker.run

### Packages
 - Virtual environment setup: `py -m venv .venv`
 - Activating environment: `.venv\Scripts\activate`
 - Installing requirements: `pip install -r requirements.txt`
 - Adding new dependencies: `pip install <package_name>`
 - Listing current dependencies: `pip freeze`

### Starting application
 - From command line: `sh run`
 - From Docker: `docker-compose up`
