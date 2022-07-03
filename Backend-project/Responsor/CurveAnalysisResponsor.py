from .ResponsorHeader import *

@App.route('/search-page', methods=["GET","POST"])
def SerchGame():
    req=request.values
    ReqGameName=req['search_game-name']
    resp=[]

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()

    resp.append({'code': 200, 'game_name': ReqGameName, 'stat': ThisGame.stat, \
        'category_name':ThisGame.cates}) 

    return jsonify(resp)

@App.route('/data', methods=["GET","POST"])
def Curve():
    req=request.values
    ReqGameName=req['game_name']
    resp=[]

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()
    LineDict=[{"date":ThisGame.time_list,"scoredata":ThisGame.stat_list, \
        "pricedata":ThisGame.price_list}]

    resp.append({'code': 200, 'status': 'success', 'Line': LineDict})

    return jsonify(resp)