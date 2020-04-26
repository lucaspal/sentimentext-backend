# Sentimentext backend
Backend for the sentimentext Chrome extension.
It is a simple Flask app, written in Python.

## Usage

## Starting the application
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

## Deployment 

The Flask app is configured to be deployed with heroku.
It is specifying its configuration with `gunicorn` in the `Procfile` file, in the root folder.