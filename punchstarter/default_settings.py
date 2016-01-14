import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/newapp.db"

DEBUG = True