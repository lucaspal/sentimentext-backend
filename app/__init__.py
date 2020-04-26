import os
from flask import Flask

# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.BaseConfig'
)
app.config.from_object(app_settings)

# Import the application views
from app import views
