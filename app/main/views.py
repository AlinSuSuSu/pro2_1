from . import main
from flask import render_template,make_response,redirect,url_for,request,flash
from .forms import StaffMessageForm
from ..models import Staff
from .. import db
@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/personnel_management/',methods=['GET','POST'])
def personnel_management():
    staffid = request.args.get('staffid')
    staffname= request.args.get("staffname")
    staffgender=request.args.get("staffgender")
    querys = Staff.query.all()
    if (staffid !='' and staffid is not None) or (staffname !='' and staffname is not None):
        if staffid =='':
            querys = Staff.query.filter_by(staffname=staffname).all()
        if staffname =='':
            querys = Staff.query.filter_by(staffid=staffid).all()
        else:
            querys = Staff.query.filter_by(staffid=staffid,staffname=staffname).all()
    '''else:
        flash("请输入查询项")
    if querys == []:
        flash("没有数据")'''
    return render_template('personnel_management.html',querys=querys)


@main.route('/detail/<int:staff_id>/delete',methods=['POST','GET'])
def staff_delete(staff_id):
    staff=Staff.query.filter_by(staffid=staff_id).first()
    db.session.delete(staff)
    db.session.commit()
    resp = make_response(redirect(url_for('.personnel_management')))
    return resp


'''
@main.route('/personnel_management/',methods=['GET','POST'])
def personnel_management():
    data=request.args
    querys=Staff.query.filter_by()
    for key in data:
        querys=querys.filter_by(getname(key)=data[key])
    return render_template('personnel_management.html',data=data,querys=querys)
'''
'''
@main.route("/staff_message",methods=['GET','POST'])
def staff_message():
    data = request.get_json()
    resp = make_response(redirect(url_for('.personnel_management')))
    if data is not None and (data['staffid'] != '' or data['staffname'] != ''):
        resp.set_cookie("staffid",data['staffid'], max_age=30 * 24 * 60 * 60)
    return resp
'''