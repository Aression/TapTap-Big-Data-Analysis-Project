from datetime import date
from .ResponsorHeader import *

route_complex = Blueprint('Comprehensive', __name__)

@route_complex.route('/ManuScore', methods=["GET","POST"])
def ComprehensiveAnalysis():
    req=request.values
    reqlist=req['manufacturer']
    resp = {'code': 200, 'status': 'failed','error_msg':'','data_list':[]}
    
    Comp=company_list.query.filter_by(company_name=reqlist).first()
    if Comp!=null:
        resp['data_list'][0]={'manu_name':reqlist,'manu_score':[Comp.one_star,Comp.two_star,Comp.three_star, \
            Comp.four_star,Comp.five_star]}
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

@route_complex.route('/GetTableAC', methods=["GET","POST"])
def CompanyAnalysis():
    req=request.values
    reqlist=req['list_name']
    resp = {'code': 200, 'status': 'failed','error_msg':'','list_info':[]}

    dates = [
        datetime.date(2022,6,i) for i in range(22,30)
    ]
    a_center = 50
    a = [random.randint(a_center-i,a_center+i) for i in range(8)]
    c_center = 40
    c = [random.randint(c_center-i,c_center+i) for i in range(8)]
    if reqlist=="综合关注度榜":
        resp['list_info'].append({'date':dates,'data_a':a,'data_c':c})
    elif reqlist=="叫座榜":
        resp['list_info'].append({'date':dates,'data_a':a,'data_c':c})
    else:
        resp['error_msg']='Invalid ListName'

    return jsonify(resp)
