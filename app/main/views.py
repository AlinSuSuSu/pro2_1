from . import main
from flask import render_template,make_response,redirect,url_for,request,flash
from .forms import StaffMessageForm
from ..models import Staff

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/personnel_management/',methods=['GET','POST'])
def personnel_management():
    '''TODO'''
    s = request.args.get('staffid')
    querys = []

    if s is not None and (s != '' ):
        querys = Staff.query.filter_by(gender=s).all()
    a=querys
    return render_template('personnel_management.html',s=s,querys=querys)

'''
@main.route("/staff_message",methods=['GET','POST'])
def staff_message():
    data = request.get_json()
    resp = make_response(redirect(url_for('.personnel_management')))
    if data is not None and (data['staffid'] != '' or data['staffname'] != ''):
        resp.set_cookie("staffid",data['staffid'], max_age=30 * 24 * 60 * 60)
    return resp
'''