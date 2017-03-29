from flask import render_template,url_for,redirect,request,make_response
from app.finance import finance
from app.models import Waterfee

@finance.route('/waterfee')
def waterfee():
    charge=False
    #querys=Waterfee.query.all()
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys=Waterfee.query.filter_by(pay='否').all()
    else:
        querys=Waterfee.query.filter_by(pay='是').all()
    return render_template('/finance/waterfee.html',charge=charge,querys=querys)

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
@finance.route('/waterfee/add')
def waterfee_add():
    return render_template('/finance/waterfee_add.html')