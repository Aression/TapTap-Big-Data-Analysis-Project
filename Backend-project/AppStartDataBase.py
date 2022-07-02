from flask import Flask
import Config.BaseConfig as Conf 
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)
App.config.from_object(Conf)
SQLDB=SQLAlchemy(App)
SQLDB.init_app(App)
DBS=SQLDB.session

#debug start
@App.route('/')
def Start():
    #Check whether we have connected.
    #Can add customs code when offline debug.
    return 'hello'
