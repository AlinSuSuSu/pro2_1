from flask import render_template,url_for,redirect,request
from . import house
from app import db
from app.models import House
import json


@house.route('/house_message',methods=['POST','GET'])
def house_message():
    querys=House.query.all()
    return render_template('house/house_message.html',querys=querys)

@house.route('/house_message/house_add',methods=['POST','GET'])
def house_add():
    return render_template('house/add_house.html')

@house.route('/house_message/add/post',methods=['POST','GET'])
def house_add_post():
    house=House(houseid=request.form.get('add-houseid'),owner_ownername=request.form.get('add-ownername'),
                housetype=request.form.get('add-housetype'),housestatus=request.form.get('add-housestatus'),
                housespace=request.form.get('add-housespace'),housecommunity=request.form.get('add-housecommunity'),
                houseaddress=request.form.get('add-houseaddress'),houseremark=request.form.get('add-houseremark'))
    db.session.add(house)
    db.session.commit()
    return redirect(url_for('house.house_message'))

@house.route('/house_message/delete/<int:house_id>',methods=['POST','GET'])
def house_delete(house_id):
    res = {
        "status": 1,
        "message": "success"
    }
    house = House.query.filter_by(houseid=house_id).first()
    db.session.delete(house)
    db.session.commit()
    return json.dumps(res)

@house.route('/house_message/detail/<int:house_id>',methods=['POST','GET'])
def house_detail(house_id):
    query=House.query.filter_by(houseid=house_id).first()
    return render_template('house/house_detail.html',query=query)

#####################################################################

@house.route('/house_owner',methods=['POST','GET'])
def house_owner():
    return render_template('house/house_owner.html')

