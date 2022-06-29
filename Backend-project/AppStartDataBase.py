from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import Config as Conf 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

App = Flask(__name__)
App.config.from_object(Conf)
HiveDB=SQLAlchemy(App)

engine=create_engine('presto://localhost:8080/hive/default')
Base = declarative_base(engine)

class students(Base):
    id = Column('student_id', Integer, primary_key = True)
    name = Column(String(100))
    city = Column(String(50))  
    addr =Column(String(200))
    pin = Column(String(10))

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
    Base.metadata.drop_all()
    Base.metadata.create_all()
    App.run(host='0.0.0.0',port=8002,debug=True)
