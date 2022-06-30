from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import Config as Conf 

App = Flask(__name__)
App.config.from_object(Conf)
DB=SQLAlchemy(App)
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
    App.run(host='0.0.0.0',port=8002,debug=True)
