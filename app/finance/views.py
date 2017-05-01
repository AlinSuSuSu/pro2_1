from flask import render_template,url_for,redirect,request,make_response,flash
from app.finance import finance
from app.models import Waterfee,House,Electricfee,Gasfee,Cleaningfee
import json
from app import db
import time
from datetime import date
from flask_moment import Moment
import datetime
@finance.route('/waterfee')
def waterfee():
    charge=True
    query_house = House.query.all()
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    #j=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
    #n=Waterfee.query.first()
    #l=Waterfee.query.all()
    #order=False
    order=bool(request.cookies.get('waterfeeorder',''))
    if charge:
        #querys=Waterfee.query.all()
        querys=Waterfee.query.filter_by(enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()).all()
    else:
        if order:
            querys=Waterfee.query.order_by(Waterfee.enddate.desc()).all()
        else:
            querys=Waterfee.query.order_by(Waterfee.enddate.asc()).all()
    return render_template('/finance/waterfee.html',charge=charge,querys=querys,query_house=a)
@finance.route('/waterfee/orderdesc')
def orderdesc():
    resp=make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('waterfeeorder','1',max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/orderasc')
def orderasc():
    resp=make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('waterfeeorder','',max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/charge')
def watercharge():
    resp = make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/notcharge')
def waternotcharge():
    resp = make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/add',methods=['POST','GET'])
def waterfee_add():
    waterfee=Waterfee(house_houseid=request.form.get('finance-houseid'),startdegree=float(request.form.get('startdegree')),enddegree=float(request.form.get('startdegree')))
    a=(request.form.get('startdate')).strip()
    b=datetime.datetime.strptime(a,'%Y-%m-%d').date()
    waterfee.startdate=b
    waterfee.enddate=waterfee.startdate
    waterfee.waterfeeid=str(waterfee.enddate)+str(waterfee.startdate)+waterfee.house_houseid
    waterfee.priceperdegree=1.0
    waterfee.totalprice=0
    db.session.add(waterfee)
    db.session.commit()
    return redirect(url_for('finance.waterfee'))
@finance.route('/waterfee/create/',methods=['GET','POST'])
def waterfee_create():

    query_house=House.query.all()
    query_waterfee=Waterfee.query.first()
    date=datetime.datetime.now()
    if query_waterfee is not None:
        if query_waterfee.startdate.year==date.year and query_waterfee.startdate.month==date.month-1:
            flash("已经生成了账单")
    else:
        for v in query_house:
            waterfee=Waterfee(house_houseid=v.houseid,totalprice=0)
            waterfee.startdate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month-1)+"01","%Y%m%d").date()
            waterfee.startdegree=0
            waterfee.enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
            waterfee.enddegree=waterfee.startdegree
            waterfee.waterfeeid=str(waterfee.enddate)+str(waterfee.startdate)+waterfee.house_houseid
            #waterfee.waterfeeid=datetime.datetime.strftime("%Y%m%d",waterfee.startdate)+waterfee.house_houseid
            db.session.add(waterfee)
            db.session.commit()
    return redirect(url_for("finance.waterfee"))

@finance.route('/waterfee/delete/<string:houseid>',methods=['GET','POST'])
def waterfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    waterfee = Waterfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(waterfee)
    db.session.commit()
    return json.dumps(res)
@finance.route('/waterfee/modify/<string:houseid>',methods=['POST','GET'])
def waterfee_modify(houseid):
    return render_template("/finance/waterfee_modify.html")

@finance.route("/waterfeee/save/<string:waterfeeid>",methods=['POST','GET'])
def waterfee_save(waterfeeid):
    data = json.loads(request.form.get('data'))
    query=Waterfee.query.filter_by(waterfeeid=waterfeeid).first()
    query.startdegree=data['startdegree']
    return redirect(url_for('finance.waterfee'))

@finance.route('/electricfee')
def electricfee():
    charge=True
    query_house = House.query.all()
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    order = bool(request.cookies.get('electricfeeorder', ''))
    if charge:
        # querys=Waterfee.query.all()
        querys = Electricfee.query.filter_by(enddate=datetime.datetime.strptime(
            str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + "01", "%Y%m%d").date()).all()
    else:
        if order:
            querys = Electricfee.query.order_by(Electricfee.enddate.desc()).all()
        else:
            querys = Electricfee.query.order_by(Electricfee.enddate.asc()).all()

    return render_template('/finance/electricfee.html',charge=charge,querys=querys,query_house=a)

@finance.route('/electricfee/charge')
def electriccharge():
    resp = make_response(redirect(url_for('finance.electricfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/electricfee/notcharge')
def electricnotcharge():
    resp = make_response(redirect(url_for('finance.electricfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/electric/orderdesc')
def electricorderdesc():
    resp=make_response(redirect(url_for('finance.electricfee')))
    resp.set_cookie('electricfeeorder','1',max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/electric/orderasc')
def electricorderasc():
    resp=make_response(redirect(url_for('finance.electricfee')))
    resp.set_cookie('electricfeeorder','',max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/electric/create/',methods=['GET','POST'])
def electricfee_create():

    query_house=House.query.all()
    query_electricfee=Electricfee.query.first()
    date=datetime.datetime.now()
    if query_electricfee is not None:
        if query_electricfee.startdate.year==date.year and query_electricfee.startdate.month==date.month-1:
            flash("已经生成了账单")
    else:
        for v in query_house:
            electricfee=Electricfee(house_houseid=v.houseid,totalprice=0)
            electricfee.startdate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month-1)+"01","%Y%m%d").date()
            electricfee.startdegree=0
            electricfee.enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
            electricfee.enddegree=electricfee.startdegree
            electricfee.electricfeeid=str(electricfee.enddate)+str(electricfee.startdate)+electricfee.house_houseid
            #waterfee.waterfeeid=datetime.datetime.strftime("%Y%m%d",waterfee.startdate)+waterfee.house_houseid
            db.session.add(electricfee)
            db.session.commit()
    return redirect(url_for("finance.electricfee"))
@finance.route('/electricfee/add',methods=['POST','GET'])
def electricfee_add():
    electricfee=Electricfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    electricfee.totalprice=(electricfee.enddegree-electricfee.startdegree)*electricfee.priceperdegree
    db.session.add(electricfee)
    db.session.commit()
    return redirect(url_for('finance.electricfee'))

@finance.route('/electricfee/delete/<string:houseid>',methods=['GET','POST'])
def electricfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    electricfee = Electricfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(electricfee)
    db.session.commit()
    return json.dumps(res)

@finance.route('/gasfee')
def gasfee():
    charge=True
    query_house = House.query.all()
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys=Gasfee.query.filter_by(pay='是').all()
    else:
        querys=Gasfee.query.filter_by(pay='否').all()
    return render_template('/finance/gasfee.html',charge=charge,querys=querys,query_house=a)

@finance.route('/gasfee/charge')
def gascharge():
    resp = make_response(redirect(url_for('finance.gasfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/gasfee/notcharge')
def gasnotcharge():
    resp = make_response(redirect(url_for('finance.gasfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/gasfee/add',methods=['POST','GET'])
def gasfee_add():
    gasfee=Gasfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    gasfee.totalprice=(gasfee.enddegree-gasfee.startdegree)*gasfee.priceperdegree
    db.session.add(gasfee)
    db.session.commit()
    return redirect(url_for('finance.gasfee'))

@finance.route('/gasfee/delete/<string:houseid>',methods=['GET','POST'])
def gasfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    gasfee = Gasfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(gasfee)
    db.session.commit()
    return json.dumps(res)
#############天然气费

###
@finance.route('/cleaningfee')
def cleaningfee():
    charge=True
    query_house = House.query.all()
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys=Cleaningfee.query.filter_by(pay='是').all()
    else:
        querys=Cleaningfee.query.filter_by(pay='否').all()
    return render_template('/finance/cleaningfee.html',charge=charge,querys=querys,query_house=a)

@finance.route('/cleaningfee/charge')
def cleaningcharge():
    resp = make_response(redirect(url_for('finance.cleaningfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/cleaningfee/notcharge')
def cleaningnotcharge():
    resp = make_response(redirect(url_for('finance.cleaningfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/cleaningfee/add',methods=['POST','GET'])
def cleaningfee_add():
    cleaningfee=Cleaningfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    cleaningfee.totalprice=(cleaningfee.enddegree-cleaningfee.startdegree)*cleaningfee.priceperdegree
    db.session.add(cleaningfee)
    db.session.commit()
    return redirect(url_for('finance.cleaningfee'))

@finance.route('/cleaningfee/delete/<string:houseid>',methods=['GET','POST'])
def cleaningfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    cleaningfee = Cleaningfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(cleaningfee)
    db.session.commit()
    return json.dumps(res)