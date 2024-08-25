import os

class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:admin@localhost/task_db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.urandom(24)
