from flask import render_template,url_for
from . import house

@house.route('/house_message',methods=['POST','GET'])
def house_message():
    return render_template('house/house_message.html')

@house.route('/house_message/house_add',methods=['POST','GET'])
def house_add():
    return render_template('house/add_house.html')

@house.route('/house_message/delete/<int:house_id>',methods=['POST','GET'])
def house_delete(houseid):
    return render_template('house/add_house.html')

@house.route('/house_message/detail/<int:house_id>',methods=['POST','GET'])
def house_detail(houseid):
    return render_template('house/add_house.html')

@house.route('/house_owner',methods=['POST','GET'])
def house_owner():
    return render_template('house/house_owner.html')

