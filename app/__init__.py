from flask import Flask
from .config import DevConfig 
from flask_bootstrap import Bootstrap


#Initializing Nouvelles
app =   Flask(__name__)

#Setting up configuration
app.config.from_object(DevConfig)

#Initializing Flask extensions
bootstrap = Bootstrap(app)


from app import views
from app import error
