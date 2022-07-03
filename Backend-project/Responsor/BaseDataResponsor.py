from .ResponsorHeader import *

route_basicdata = Blueprint('BasicData', __name__)
# 获取对应榜单的游戏类型数据,返回字典，比如{'MMORPG': 1, '二次元': 1, '冒险': 1, '魔幻': 1, '3D ': 1}
def getHotTableChart(list_name):
    if (list_name == "heat_rank"):
        heat_games = game_list.query.filter(game_list.heat_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for heat_game in heat_games:
            heat_game_cateList = str(heat_game.cates).split(',')
            for i in heat_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count
    if (list_name == "played_rank"):
        played_games = game_list.query.filter(game_list.played_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for played_game in played_games:
            played_game_cateList = str(played_game.cates).split(',')
            for i in played_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count
    if (list_name == "reserved_rank"):
        reserved_games = game_list.query.filter(game_list.reserved_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for reserved_game in reserved_games:
            reserved_game_cateList = str(reserved_game.cates).split(',')
            for i in reserved_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count
    if (list_name == "sold_rank"):
        sold_games = game_list.query.filter(game_list.sold_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for sold_game in sold_games:
            sold_game_cateList = str(sold_game.cates).split(',')
            for i in sold_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count

@route_basicdata.route('/getHotTableChart', methods=["GET","POST"])
def HotTableChart():
    req=request.values
    reqlist=req['list_name']

    resp = {'code': 200, 'status': 'success','chart_data':getHotTableChart(reqlist)}
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
