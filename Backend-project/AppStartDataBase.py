from flask import Flask
import Config.BaseConfig as Conf 
from flask_sqlalchemy import SQLAlchemy
from DB.Constructor.DBConstructor import ConstructAll

App = Flask(__name__)
App.config.from_object(Conf)
DB=SQLAlchemy(App)
DB.init_app(App)
DBS=DB.session

#debug start
@App.route('/')
def Start():
    #Check whether we have connected.
    #Can add customs code when offline debug.
    return 'hello'
#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase
    from DB.Models.Models import *
    #DB.drop_all()
    #DB.create_all()
    ConstructAll()
    App.run(host='0.0.0.0',port=8002,debug=True)
