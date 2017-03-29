from flask import render_template,url_for,redirect,request,flash
from . import house
from app import db
from app.models import House,Owner
import json


@house.route('/house_message/',methods=['POST','GET'])
def house_message():
    queryall=House.query.all()
    houseid=request.args.get('houseid')
    ownername=request.args.get('ownername')
    if (houseid != '' and houseid is not None) or (ownername is not None and ownername != ''):
        if houseid == '' or houseid is  None:
            querys = House.query.filter_by(owner_ownername=ownername)
        elif ownername == '' or ownername is None:
            querys = House.query.filter_by(houseid=houseid)
        else:
            querys = House.query.filter_by(houseid=houseid,owner_ownername=ownername)
    else:
        querys = House.query.all()
    return render_template('house/house_message.html',querys=querys,queryall=queryall)

@house.route('/house_message/house_add',methods=['POST','GET'])
def house_add():
    owner_querys=Owner.query.all()
    return render_template('house/add_house.html',owner_querys=owner_querys)

@house.route('/house_message/add/post',methods=['POST','GET'])
def house_add_post():
    house=House(houseid=request.form.get('add_houseid'),owner_ownername=request.form.get('add_ownername'),
                housetype=request.form.get('add_housetype'),housestatus=request.form.get('add_housestatus'),
                housespace=request.form.get('add_housespace'),housecommunity=request.form.get('add_housecommunity'),
                houseaddress=request.form.get('add_houseaddress'),houseremark=request.form.get('add_houseremark'))
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

@house.route('/house_owner/',methods=['POST','GET'])
def house_owner():
    queryall=Owner.query.all()
    houseid = request.args.get('houseid')
    ownername = request.args.get('ownername')
    if (houseid != '' and houseid is not None) or (ownername is not None and ownername != ''):
        if houseid == '' or houseid is None:
            querys = Owner.query.filter_by(ownername=ownername)
        elif ownername == '' or ownername is None:
            querys = Owner.query.filter_by(house_houseid=houseid)
        else:
            querys = Owner.query.filter_by(house_houseid=houseid, ownername=ownername)
    else:
        querys = Owner.query.all()
    return render_template('house/house_owner.html',querys=querys,queryall=queryall)

@house.route('/house_owner/owner_add',methods=['POST','GET'])
def owner_add():
    return render_template('house/add_owner.html')


@house.route('/house_owner/add/post', methods=['POST', 'GET'])
def owner_add_post():
    owner=Owner(ownername=request.form.get('add_ownername'),house_houseid=request.form.get('add_house_houseid'),
                ownerphone=request.form.get('add_ownerphone'),owneridcard=request.form.get('add_owneridcard'),
                owneryears=request.form.get('add_owneryears'),ownerstatus=request.form.get('add_ownerstatus'),ownerdate=request.form.get('ownerdate'))
    db.session.add(owner)
    db.session.commit()
    return redirect(url_for('house.house_owner'))

@house.route('/house_owner/delete/<int:house_id>',methods=['POST','GET'])
def owner_delete(house_id):
    res = {
        "status": 1,
        "message": "success"
    }
    owner = Owner.query.filter_by(house_houseid=house_id).first()
    db.session.delete(owner)
    db.session.commit()
    return json.dumps(res)

@house.route('/house_owner/detail/<int:house_id>',methods=['POST','GET'])
def owner_detail(house_id):
    query=Owner.query.filter_by(house_houseid=house_id).first()
    return render_template('house/owner_detail.html',query=query)
