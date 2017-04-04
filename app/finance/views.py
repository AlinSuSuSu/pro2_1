from flask import render_template,url_for,redirect,request,make_response
from app.finance import finance
from app.models import Waterfee,House

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
    db.session.add(waterfee)
    db.session.commit()
    return redirect(url_for('finance.waterfee'))