from AppStartDataBase import App
from ResponseFunctionLibrary import *
from flask import Blueprint,make_response

route_rank = Blueprint('rank', __name__)

@route_rank.route('/heat', methods=["GET"])
def HeatRank():

    return 

@route_rank.route('/played', methods=["GET"])
def PlayedRank():
    
    return 

@route_rank.route('/reserved', methods=["GET"])
def ReservedRank():
    
    return 

@route_rank.route('/sold', methods=["GET"])
def SoldRank():
    
    return 