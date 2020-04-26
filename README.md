# Sentimentext backend
Backend for the sentimentext Chrome extension.
It is a simple Flask app, written in Python.

## Usage

### Requirements

Python3 (developed and tested on python 3.7)

### Setup

Get the dependencies. The following command should be run in the root directory of the project.

```
pip3 install -r ./requirements.txt
```

### Starting the application
In order to run the application set the environment
variable below.
```
Windows
set FLASK_APP=run.py

Unix
export FLASK_APP=run.py
```
Then run the command below to start the application.
```
flask run
```

### Deployment 

The Flask app is configured to be deployed with heroku.
It is specifying its configuration with `gunicorn` in the `Procfile` file, in the root folder.
