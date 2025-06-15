import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
print("Base Dir:", BASEDIR)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'transcripts.db')
    # Allow SQLite use across threads
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {'check_same_thread': False}
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = os.path.join(BASEDIR, 'app.log')
