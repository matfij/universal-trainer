## Universal trainer
One project to rule all the Kaggle challenges

### Requirements
 - Python 3.6+ (3.10.0rc1 was used for this project)
 - Docker, docker-compose (optional)
 - Upgrade pip: `pip install --upgrade pip`

### Packages
 - Virtual environment setup: `py -m venv .venv`
 - Activating environment: `.venv\Scripts\activate`
 - Installing requirements: `pip install -r requirements.txt`
 - Adding new dependencies: `pip install <package_name>`
 - Listing current dependencies: `pip freeze`

### Starting application
 - From command line: `sh run`
 - From Docker: `docker-compose up`
