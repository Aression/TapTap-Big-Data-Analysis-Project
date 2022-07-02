from sqlalchemy import null
from .ResponsorHeader import *

route_complex = Blueprint('Comprehensive', __name__)

@route_complex.route('/ManuScore', methods=["GET","POST"])
def ComprehensiveAnalysis():
    req=request.values
    reqlist=req['manufacturer']
    resp = {'code': 200, 'status': 'failed','error_msg':'','data_list':[]}
    
    Comp=company_list.query.filter_by(company_name=reqlist).first()
    if Comp!=null:
        resp['data_list']=[Comp.one_star,Comp.two_star,Comp.three_star, \
            Comp.four_star,Comp.five_star]
    else:
        resp['error_msg']='Invalid CompName'

    return jsonify(resp)

@route_complex.route('/GameTypeAnalysis', methods=["GET","POST"])
def TypeAnalysis():
    req=request.values
    reqlist=req['gametype_list']
    resp = {'code': 200, 'status': 'failed','error_msg':'','data_list':[]}

    if reqlist=="游戏类型评分分析":
        BaseDict={}
        Cates=cate_list.query_all()
        for i in Cates:
            BaseDict['game_typename']=i.cate_name
            BaseDict['download_list']=i.downlo
            BaseDict['score_list']=i.stat
            resp['data_list'].append(BaseDict)
        pass
    else:
        resp['error_msg']='Invalid ListName'

    return jsonify(resp)

#Unfinished------------------------------------------------------------------
@route_complex.route('/GetTableAC', methods=["GET","POST"])
def CompanyAnalysis():
    req=request.values
    reqlist=req['list_name']
    resp = {'code': 200, 'status': 'failed','error_msg':'','list_info':[]}


    if reqlist=="com_attention":
        #Do calculate
        pass
    elif reqlist=="call_set":
        #Do caluculate
        pass
    else:
        resp['error_msg']='Invalid ListName'

    return jsonify(resp)
