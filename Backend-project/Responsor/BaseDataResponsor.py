from .ResponsorHeader import *

route_basicdata = Blueprint('basicdata', __name__)

#Unfinished------------------------------------------------------------------
@route_basicdata.route('/getHotTableChart', methods=["GET","POST"])
def HotTableChart():
    req=request.values
    reqlist=req['list_name']

    Cates=cate_list.query.all()
    #if reqlist==
    #Find hot of category from data analysis.

    resp = {'code': 200, 'status': 'failed'}
    return jsonify(resp)

@route_basicdata.route('/getHotTable', methods=["GET","POST"])
def HotTable():
    req=request.values
    reqlist=req['list_name']

    hotstr=[]
    if reqlist=="heat_rank":
        TpGames = game_list.query.order_by(game_list.heat_rank).all()
        RankGame=[]
        for i in TpGames:
            if i.heat_rank!=0:
                RankGame.append(i)
    elif reqlist=="played_rank":
        TpGames = game_list.query.order_by(game_list.played_rank).all()
        RankGame=[]
        for i in TpGames:
            if i.played_rank!=0:
                RankGame.append(i)
    elif reqlist=="reserved_rank":
        TpGames = game_list.query.order_by(game_list.reserved_rank).all()
        RankGame=[]
        for i in TpGames:
            if i.reserved_rank!=0:
                RankGame.append(i)
    elif reqlist=="sold_rank":
        TpGames = game_list.query.order_by(game_list.sold_rank).all()
        RankGame=[]
        for i in TpGames:
            if i.sold_rank!=0:
                RankGame.append(i)
    else:
        resp = {'code': 200, 'status': 'failed'}
        return jsonify(resp)

    for i in RankGame:
        hotstr.append('game_name:{},stat:{},category_name:{}'. \
            format(i.game_name,i.stat,i.cates))

    resp = {'code': 200, 'status': 'success', 'tableData': hotstr}
    return jsonify(resp)
