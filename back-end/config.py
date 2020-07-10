import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'urmomisgay'
    FLASK_ENV = "development"
    FLASK_DEBUG = 1
    # Disabled for non-html client request
    WTF_CSRF_ENABLED = False
    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAZESIZE = 10

