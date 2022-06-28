from AppStartDataBase import App
from ResponseFunctionLibrary import *
from flask import Blueprint,make_response

route_curve = Blueprint('curve', __name__)

@route_curve.route('/', methods=["GET","POST"])
def CurveList():
    
    return


@route_curve.route('/details', methods=["GET","POST"])
def Curve():
    
    return 