from .ResponsorHeader import *

@App.route('/search-page', methods=["GET","POST"])
def SerchGame():
    req=request.values
    ReqGameName=req['search_game-name']

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()

    resp={'code': 200, 'tableData':[{'game_name': ReqGameName, 'stat': ThisGame.stat, \
        'category_name':ThisGame.cates}]}

    return jsonify(resp)

@App.route('/data', methods=["GET","POST"])
def Curve():
    req=request.values
    ReqGameName=req['game_name']

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()
    LineDict=[{"date":ThisGame.time_list,"scoredata":ThisGame.stat_list, \
        "pricedata":ThisGame.price_list}]

    resp={'code': 200, 'status': 'success', 'Line': LineDict, "com-emoji": ThisGame.emoji}

    return jsonify(resp)