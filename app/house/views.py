from flask import render_template,url_for
from . import house

@house.route('/house_management',methods=['POST','GET'])
def house_management():
    return