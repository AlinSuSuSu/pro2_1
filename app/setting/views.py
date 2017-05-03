from flask import render_template,flash,redirect,request,url_for,make_response
from . import setting
from ..models import User,Role,Staff,Choice,Waterfee,House
from flask_login import login_user,logout_user,login_required,current_user
from app import db
import json

@setting.route('/',methods=['POST','GET'])
def set():
    return render_template('setting/setting.html')

@setting.route('/staff_setting',methods=['POST','GET'])
def staff_setting():
    queryall = Staff.query.all()
    job = request.args.getlist('job')
    staffname = request.args.get('staffname')
    if (len(job) != 0 and job is not None) or (staffname is not None and staffname != ''):
        if (staffname == '' or staffname is None) and len(job)==1:
            querys = Staff.query.filter_by(job=job[0])
        elif (len(job) == 0 or job is None)or (len(job)==2 and (staffname != '' and staffname is not None)):
            querys = Staff.query.filter_by(staffname=staffname)
        elif len(job)==1:
            querys = Staff.query.filter_by(staffname=staffname,job=job[0])
        else:
         querys = Staff.query.all()
    else:
        querys = Staff.query.all()
    return  render_template('setting/staff_setting.html',queryall=queryall,querys=querys)
#添加员工页面
@setting.route('/staff/add',methods=['POST','GET'])
def staff_add():
    return render_template('setting/staff_add.html')

@setting.route('/staff/add/post',methods=['POST','GET'])
def staff_add_post():
    password=request.form.get('add-password')
    staff=Staff(staffid=request.form.get('add-staffid'),staffname=request.form.get('add-staffname'),
                phone=request.form.get('add-phone'),idcard=request.form.get('add-idcard'),
                salary=request.form.get('add-salary'),job=request.form.get('add-job'),
                age=request.form.get('add-age'),password=request.form.get('add-password'),gender=request.form.get('add-gender'),role_id='4')
    db.session.add(staff)
    db.session.commit()
    return redirect(url_for('staff.staff_message'))
#删除员工
@setting.route('/staff/delete/<string:staffid>',methods=['POST','GET'])
def staff_delete(staffid):
    res = {
        "status": 1,
        "message": "success"
    }
    staff=Staff.query.filter_by(staffid=staffid).first()
    db.session.delete(staff)
    db.session.commit()
    return json.dumps(res)

@setting.route('/staff/detail/<string:staffid>',methods=['POST','GET'])
def staff_detail(staffid):
    return render_template('setting/staff_detail.html')

@setting.route('/choice_setting',methods=['POST','GET'])
def choice_setting():
    choicecharge=True
    choicecharge=bool(request.cookies.get('choicecharge', ''))
    query_patrol=Choice.query.filter_by(choicetype='保安巡逻')
    query_infrastructure=Choice.query.filter_by(choicetype='绿化基建')
    query_house=House.query.all()

    return render_template('/setting/choice_setting.html',choicecharge=choicecharge,query_infrastructure=query_infrastructure,query_house=query_house,query_patrol=query_patrol)

@setting.route('/choice/choicecharge')
def choicecharge():
    resp=make_response(redirect(url_for('setting.choice_setting')))
    resp.set_cookie('choicecharge','1',max_age=30 * 24 * 60 * 60)
    return resp
@setting.route('/choice/choicenotcharge')
def choicenotcharge():
    resp=make_response(redirect(url_for('setting.choice_setting')))
    resp.set_cookie('choicecharge','',max_age=30 * 24 * 60 * 60)
    return resp


@setting.route('/choice/add',methods=['POST','GET'])
def choice_add():
    patrol_add=request.form.get('patrol_add')
    infrastructure_add=request.form.get('infrastructure_add')
    if patrol_add !='' and patrol_add is not None:
        choice=Choice(choicetype='保安巡逻',choicename=patrol_add)
        db.session.add(choice)
        db.session.commit()
    if infrastructure_add !='' and infrastructure_add is not None:
        choice=Choice(choicetype='绿化基建',choicename=infrastructure_add)
        db.session.add(choice)
        db.session.commit()
    return redirect(url_for('setting.choice_setting'))
@setting.route('/choice/delete/<int:id>',methods=['POST','GET'])
def choice_delete(id):
    res = {
        "status": 1,
        "message": "success"
    }
    choice = Choice.query.filter_by(id=id).first()
    db.session.delete(choice)
    db.session.commit()
    return json.dumps(res)

@setting.route('/choice/price_setting',methods=['POST','GET'])
def price_setting():
    priceitem=request.form.get('setitem')
    price=request.form.get('price')
    if priceitem is not None and priceitem !='':
        c=Waterfee()
        c.pricesetter(float(price))
    return  redirect(url_for('setting.choice_setting'))
