from flask import Flask
import Config.BaseConfig as Conf 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Conf)
CORS(app, resources={r'/*': {'origins': '*', 'supports_credentials': True, 'Access-Control-Allow-Origin': '*'}})


SQLDB=SQLAlchemy(app)
SQLDB.init_app(app)
DBS=SQLDB.session

# #debug start
# @app.route('/')
# def Start():
#     #Check whether we have connected.
#     #Can add customs code when offline debug.
#     return 'hello'

@app.route('/update_data')
def update_data():
    # from DataBase.Models.Models import *
    from DataBase.Constructor.DBConstructor import ConstructAll
    from Analyzer.Analyzer import update_game_list, update_cate_list, update_company_list
    SQLDB.drop_all()
    SQLDB.create_all()
    ConstructAll()
    update_game_list()
    update_cate_list()
    update_company_list()
    return 'update request accepted'

    
# @app.route('/construct_base')
# def ConstructBase():
#     SQLDB.drop_all()
#     SQLDB.create_all()
#     ConstructAll()
#     return 'construct_base accepted'
    
# @app.route('/construct_analyse')
# def ConstructAnalyse():
#     update_game_list()
#     update_cate_list()
#     update_company_list()
#     return 'construct_analyse accepted'
    
#launch
#launch databse local debug
# if __name__ == '__main__':
    # from DataBase.Models.Models import *
    # from DataBase.Constructor.DBConstructor import ConstructAll
    # from Analyzer.Analyzer import *
    # SQLDB.create_all()
    # update_game_list()
    # update_cate_list()
    # update_company_list()
    # app.run(host='0.0.0.0',port=8003,debug=True)