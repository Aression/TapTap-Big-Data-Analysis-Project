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
#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase
    from DataBase.Models.Models import *
    SQLDB.drop_all()
    SQLDB.create_all()
    from DataBase.Constructor.DBConstructor import ConstructAll
    ConstructAll()
    App.run(host='0.0.0.0',port=8002,debug=True)
