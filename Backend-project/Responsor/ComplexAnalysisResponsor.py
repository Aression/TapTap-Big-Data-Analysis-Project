from .ResponsorHeader import *

route_complex = Blueprint('Comprehensive', __name__)

@route_complex.route('/ManuScore', methods=["GET","POST"])
def ComprehensiveAnalysis():
    
    return

@route_complex.route('/GameTypeAnalysis', methods=["GET","POST"])
def TypeAnalysis():
    
    return

@route_complex.route('/GetTableAC', methods=["GET","POST"])
def CompanyAnalysis():
    
    return 
