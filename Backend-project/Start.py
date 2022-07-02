from AppStartDataBase import *
from Responsor.CurveAnalysisResponsor import *
from Responsor.ComplexAnalysisResponsor import *
from Responsor.BaseDataResponsor import *

App.register_blueprint(route_basicdata, url_prefix="/basicdata")
App.register_blueprint(route_complex, url_prefix="/Comprehensive")

#launch
#launch databse local debug
if __name__ == '__main__':
    #LocalDataBase
    '''
    from DataBase.Models.Models import *
    SQLDB.drop_all()
    SQLDB.create_all()
    from DataBase.Constructor.DBConstructor import ConstructAll
    ConstructAll()
    '''
    #from Analyzer.Analyzer import update_game_list,update_cate_list,update_company_list
    #update_game_list()
    #update_cate_list()
    #update_company_list()

    App.run(host='0.0.0.0',port=8002,debug=True)
