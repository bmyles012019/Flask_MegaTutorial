import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    """
        Flask-SQLALCHEMY extension that takes the location of the 
        applicaion's database from the SQLALCHEMY_DATABASE_URI 
        configuration variable. If not environment variable the
        set the path to a sqlite db file.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False