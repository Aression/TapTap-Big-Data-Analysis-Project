from .ResponsorHeader import *

route_basicdata = Blueprint('BasicData', __name__)
# 获取对应榜单的游戏类型数据,返回字典，比如{'MMORPG': 1, '二次元': 1, '冒险': 1, '魔幻': 1, '3D ': 1}
def getHotTableChart(list_name):
    if (list_name == "热门榜"):
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
    if (list_name == "热玩榜"):
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
    if (list_name == "预约榜"):
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
    if (list_name == "厂商榜"):
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
    charts=[]
    chartdata = getHotTableChart(reqlist)
    for i in chartdata.items():
        charts.append({'category_name':i[0],'amount':i[1]})

    resp={'code': 200, 'status': 'success','chart_data':charts}
    return jsonify(resp)

@route_basicdata.route('/getHotTable', methods=["GET","POST"])
def HotTable():
    req=request.values
    reqlist=req['list_name']

    hotstr=[]
    RankCnt=0
    MaxCnt=50
    if reqlist=="热门榜":
        TpGames = game_list.query.order_by(game_list.heat_rank.desc()).all()
        RankGame=[]
        for i in TpGames:
            if RankCnt>=MaxCnt:
                break
            if i.heat_rank!=0:
                RankCnt+=1
                RankGame.append(i)
    elif reqlist=="热玩榜":
        TpGames = game_list.query.order_by(game_list.played_rank.desc()).all()
        RankGame=[]
        for i in TpGames:
            if RankCnt>=MaxCnt:
                break
            if i.played_rank!=0:
                RankCnt+=1
                RankGame.append(i)
    elif reqlist=="预约榜":
        TpGames = game_list.query.order_by(game_list.reserved_rank.desc()).all()
        RankGame=[]
        for i in TpGames:
            if RankCnt>=MaxCnt:
                break
            if i.reserved_rank!=0:
                RankCnt+=1
                RankGame.append(i)
            else:
                RankCnt+=1
                i.reserved_rank=i
                RankGame.append(i)
        RankGame.sort(key=lambda x:x.reserved_rank)

        for i in RankGame:
            hotstr.append({'game_name':i.game_name,'stat':i.reserved_rank,'category_name':i.cates})  

        resp={'code': 200, 'status': 'success', 'tableData': hotstr}
        return jsonify(resp)
    elif reqlist=="厂商榜":
        TpComp=company_list.query.order_by(company_list.stat.desc()).all()
        RankGame=[]
        for i in TpComp:
            if RankCnt>=MaxCnt:
                break
            if i.stat!=0:
                RankCnt+=1
                RankGame.append(i)

        for i in RankGame:
            hotstr.append({'category_name':i.company_name,'stat':i.stat})

        resp={'code': 200, 'status': 'success', 'tableData': hotstr}
        return jsonify(resp)

    else:
        resp = {'code': 200, 'status': 'failed'}
        return jsonify(resp)

    for i in RankGame:
        hotstr.append({'game_name':i.game_name,'stat':i.stat,'category_name':i.cates})

    resp={'code': 200, 'status': 'success', 'tableData': hotstr}
    return jsonify(resp)
