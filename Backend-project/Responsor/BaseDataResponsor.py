from .ResponsorHeader import *

route_basicdata = Blueprint('basicdata', __name__)

#Unfinished------------------------------------------------------------------
@route_basicdata.route('/getHotTableChart', methods=["GET"])
def HotTableChart():
    
    Cates=Category.query.all()
    #Find hot of category from data analysis.

    return 

#Unfinished------------------------------------------------------------------
@route_basicdata.route('/getHotTable', methods=["GET"])
def HotTable():
    req=request.values

    hots=[]
    hotstr=[]
    Games = History.query.order_by(History.UpdateTime.asc()).all()
    LastUpdate=Games.first().UpdateTime
    for i in Games:
        if i.UpdateTime!=LastUpdate:
            break

        hots.append(i)

    hots.sort(key=HeatRank,reverse=True)

    for i in hots:
        gameobject=Game.query.get(i.GameID)
        hotstr.append('game_name:{},stat:{},category_name:{}'.format(gameobject.GameName,gameobject.CategoryName,i.HeatRank))

    resp = {'code': 200, 'status': 'success', 'tableData': hots}
    return jsonify(resp)
