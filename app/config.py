from app.sensive import Sensive as sensive
from os import environ

class Config: 
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql://oqnquahjgszyqj:483eee03100b1ab916889ecc904e65cfe8c61342ccfa021fd58e6be95d88fdc1@ec2-34-193-113-223.compute-1.amazonaws.com:5432/dcensg8a8knisj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    #JWT_SECRET_KEY = sensive.JWT_SECRET_KEY