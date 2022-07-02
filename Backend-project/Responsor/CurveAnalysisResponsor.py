from ResponsorHeader import *

@App.route('/search-page', methods=["GET","POST"])
def SerchGame():
    req=request.values
    ReqGameName=req['search_game-name']

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()

    resp = {'code': 200, 'game_name': ReqGameName, 'stat': ThisGame.stat, 'category_name':ThisGame.cates}

    return jsonify(resp)

#Unfinished------------------------------------------------------------------
@App.route('/data', methods=["GET","POST"])
def Curve():
    req=request.values
    ReqGameName=req['search_game-name']

    ThisGame=Game.query.filter_by(GameName=ReqGameName).first()
    Historys=History.query.filter_by(GameID=ThisGame.GameID).all()

    

    return 