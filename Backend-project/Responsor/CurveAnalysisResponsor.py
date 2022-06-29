from ResponsorHeader import *

#Unfinished------------------------------------------------------------------
@App.route('/', methods=["GET"])
def SerchGame():
    req=request.values
    ReqGameName=req['search_game-name']

    ThisGame=Game.query.filter_by(GameName=ReqGameName).first()

    resp = {'code': 200, 'game_name': ReqGameName, 'stat': ThisGame.stat, 'category_name':ThisGame.CategoryName}

    return jsonify(resp)

#Unfinished------------------------------------------------------------------
@App.route('/curve', methods=["GET"])
def Curve():
    req=request.values
    ReqGameName=req['search_game-name']

    ThisGame=Game.query.filter_by(GameName=ReqGameName).first()
    Historys=History.query.filter_by(GameID=ThisGame.GameID).all()

    

    return 