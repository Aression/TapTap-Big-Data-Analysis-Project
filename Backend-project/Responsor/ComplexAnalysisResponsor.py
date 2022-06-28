from AppStartDataBase import App
from ResponseFunctionLibrary import *
from flask import Blueprint,make_response

route_complex = Blueprint('complex', __name__)

@route_complex.route('/comprehensive', methods=["GET","POST"])
def ComprehensiveAnalysis():
    
    return

@route_complex.route('/type', methods=["GET","POST"])
def TypeAnalysis():
    
    return

@route_complex.route('/company', methods=["GET","POST"])
def CompanyAnalysis():
    
    return 

@route_complex.route('/score', methods=["GET","POST"])
def ScoreAnalysis():
    
    return 