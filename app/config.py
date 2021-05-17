from app.sensive import Sensive as sensive
from os import environ

class Config: 
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URL = 'postgres://awmxbjemscipfr:00a94aee34e26ff35d55b9a8fe66baf572c3a73057cc3b06e21666ce38ea8be0@ec2-18-215-111-67.compute-1.amazonaws.com:5432/dek5p97di3qk5h'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    #JWT_SECRET_KEY = sensive.JWT_SECRET_KEY