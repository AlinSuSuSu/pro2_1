from flask import render_template,url_for
from . import house

@house.route('/house_message',methods=['POST','GET'])
def house_message():
    return render_template('house/house_message.html')