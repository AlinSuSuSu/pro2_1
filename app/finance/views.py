from flask import render_template,url_for,redirect,request,make_response
from app.finance import finance
from app.models import Waterfee,House,Electricfee,Gasfee,Cleaningfee
import json
from app import db
@finance.route('/waterfee')
def waterfee():
    charge=True
    query_house = House.query.all()
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys=Waterfee.query.filter_by(pay='是').all()
    else:
        querys=Waterfee.query.filter_by(pay='否').all()
    return render_template('/finance/waterfee.html',charge=charge,querys=querys,query_house=a)

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
    waterfee=Waterfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    waterfee.totalprice=(waterfee.enddegree-waterfee.startdegree)*waterfee.priceperdegree
    db.session.add(waterfee)
    db.session.commit()
    return redirect(url_for('finance.waterfee'))

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

@finance.route('/electricfee')
def electricfee():
    charge=True
    query_house = House.query.all()
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys=Electricfee.query.filter_by(pay='是').all()
    else:
        querys=Electricfee.query.filter_by(pay='否').all()
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