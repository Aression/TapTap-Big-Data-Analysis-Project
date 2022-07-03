from .ResponsorHeader import *

route_curve = Blueprint('', __name__)

@route_curve.route('/search-page', methods=["GET","POST"])
def SerchGame():
    req=request.values
    ReqGameName=req['search_game-name']

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()

    resp={'code': 200, 'tableData':[{'game_name': ReqGameName, 'stat': ThisGame.stat, \
        'category_name':ThisGame.cates}]}

    return jsonify(resp)

@route_curve.route('/data', methods=["GET","POST"])
def Curve():
    req=request.values
    ReqGameName=req['game_name']

    ThisGame=game_list.query.filter_by(game_name=ReqGameName).first()
    ThisPrice=[]
    ThisTime = [datetime.date(2022,6,i) for i in range(22,30)]
    a_center = int(float(ThisGame.stat_list))
    ThisStat = [random.randint(int(a_center-i/8),int(a_center+i/8)) for i in range(8)]
    a_center= int(float(ThisGame.price_list))
    ThisPrice= [random.randint(a_center,int(a_center+i/2)) for i in range(8)]
    LineDict=[{"date":ThisTime,"scoredata":ThisStat, \
        "pricedata":ThisPrice}]
    emoji = ThisGame.emoji
    resp={'code': 200, 'status': 'success', 'Line': LineDict, "com_emoji": [int(i) for i in emoji.split(',')]}

    return jsonify(resp)