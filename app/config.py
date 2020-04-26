import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False