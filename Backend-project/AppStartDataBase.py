from flask import Flask
from pyhive import hive
#from Constructor.ConstructHelper import ConstructAll

App = Flask(__name__)

#Hive
HiveConnection = hive.Connection(host='ip地址', port='端口号', username='用户名', database='数据库名')
HiveDB = HiveConnection.cursor()

#start
#called when open localhost if database use localhost as uri config
#do database base construct or other database init operations
#can remove if use database manager or .sql
@App.route('/')
def Start():
    '''
    db.drop_all()
    db.create_all()
    ConstructAll(1384635792)
    '''
    #RegisterBaseRequest('RegTest','XXXX',183023)
    #Register002Request('RegTest002',3,'NoHardware')
    #Login002Request('Ayanami','UnInitedHardwareCode')

    return "hello"

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase
    App.run(host='0.0.0.0',port=8002,debug=True)
