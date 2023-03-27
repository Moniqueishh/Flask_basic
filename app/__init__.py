from flask import Flask

from config import Config
#Accesses the config file 

app = Flask(__name__)
# -need to add from app import app to routes file
# to the routes folder so this can be accessed

app.config.from_object(Config)
#Accesses the config file 

from . import routes
#from (all) import routes
# This is how we let the __init__ folder know about our routes folder