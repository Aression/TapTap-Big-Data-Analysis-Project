from flask import Flask
from pyhive import hive
import prestodb
#from Constructor.ConstructHelper import ConstructAll

App = Flask(__name__)

#Hive & Presto
HiveConnection = prestodb.dbapi.connect(host='localhost',port="8080",catalog="hive")
HiveDB = HiveConnection.cursor()

#debug start
@App.route('/')
def Start():
    #Check whether we have connected.
    #Can add customs code when offline debug.

    return "hello"

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase
    App.run(host='0.0.0.0',port=8002,debug=True)
