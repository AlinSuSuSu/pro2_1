import json

from flask import render_template, redirect,url_for,request

from app import db
from app.staff import staff
from app.models import Staff
from app.staff.forms import StaffBonusForm


@staff.route('/',methods=['GET','POST'])
def index():
    return render_template('auth/staff_message.html')

@staff.route('/staff_message',methods=['GET','POST'])
def staff_message():
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
    return render_template('staff/staff_message.html',querys=querys)


@staff.route('/detail/delete/<int:staff_id>',methods=['POST','GET'])
def staff_delete(staff_id):
    res = {
        "status": 1,
        "message": "success"
    }
    staff=Staff.query.filter_by(staffid=staff_id).first()
    db.session.delete(staff)
    db.session.commit()
    return json.dumps(res)

@staff.route('/staff_message/add/post',methods=['POST','GET'])
def staff_add_post():
    staff=Staff(staffid=request.form.get('add-staffid'),staffname=request.form.get('add-staffid'),
                phone=request.form.get('add-phone'),idcard=request.form.get('add-idcard'),
                salary=request.form.get('add-salary'),job=request.form.get('add-job'),
                age=request.form.get('add-age'),password=request.form.get('add-password'),gender=request.form.get('add-gender'))
    db.session.add(staff)
    db.session.commit()
    return redirect(url_for('staff.staff_message'))

@staff.route('/staff_message/add',methods=['POST','GET'])
def staff_add():

    return render_template('staff/add_staff.html')

###########人事管理，员工福利

@staff.route('/staff_bonus',methods=['GET','POST'])
def staff_bonus():
    form=StaffBonusForm()
    return render_template('staff/staff_bonus.html',form=form)


