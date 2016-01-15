import os
import cloudinary


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/newapp.db"

DEBUG = True

cloudinary.config( 
  cloud_name = "da2bogsxm", 
  api_key = "566777878874789", 
  api_secret = "ha4fe7-ypsxy24L7Ld4wi7oIPYk" 
)