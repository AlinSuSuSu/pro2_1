import json
from datetime import datetime
from flask import render_template,flash,redirect,url_for,request
from flask_login import login_required,current_user
from app import db
from app.staff import staff
from app.models import Staff,Holiday,Reimbursement
from app.staff.forms import StaffBonusForm,StaffHolidayForm,StaffReimbursementForm
from app.decorators import owner_required
#员工管理主页
@staff.route('/',methods=['GET','POST'])
def index():
    return render_template('auth/staff_message.html')

################staff_message
#员工信息
@staff.route('/staff_message/',methods=['GET','POST'])

def staff_message():
    staffid = request.args.get('staffid')
    staffname= request.args.get("staffname")
    #staffgender=request.args.get("staffgender")
    queryall = Staff.query.all()
    if (staffid !='' and staffid is not None) or (staffname !='' and staffname is not None):
        if staffid =='' or staffid is None:
            querys = Staff.query.filter_by(staffname=staffname).all()
        elif staffname =='' or staffid is None:
            querys = Staff.query.filter_by(staffid=staffid).all()
        else:
            querys = Staff.query.filter_by(staffid=staffid,staffname=staffname).all()
    else:
        querys = Staff.query.all()

    '''else:
        flash("请输入查询项")
    if querys == []:
        flash("没有数据")'''
    return render_template('staff/staff_message.html',querys=querys,queryall=queryall)

#删除员工
@staff.route('/staff_message/delete/<int:staff_id>',methods=['POST','GET'])
def staff_delete(staff_id):
    res = {
        "status": 1,
        "message": "success"
    }
    staff=Staff.query.filter_by(staffid=staff_id).first()
    db.session.delete(staff)
    db.session.commit()
    return json.dumps(res)
#添加员工，post请求
@staff.route('/staff_message/add/post',methods=['POST','GET'])
def staff_add_post():
    password=request.form.get('add-password')
    staff=Staff(staffid=request.form.get('add-staffid'),staffname=request.form.get('add-staffname'),
                phone=request.form.get('add-phone'),idcard=request.form.get('add-idcard'),
                salary=request.form.get('add-salary'),job=request.form.get('add-job'),
                age=request.form.get('add-age'),password=request.form.get('add-password'),gender=request.form.get('add-gender'),role_id='4')
    db.session.add(staff)
    db.session.commit()
    return redirect(url_for('staff.staff_message'))

#添加员工页面
@staff.route('/staff_message/add',methods=['POST','GET'])
def staff_add():
    return render_template('staff/add_staff.html')


##############################################################

##########staff_bonus
#员工福利页面
@staff.route('/staff_bonus',methods=['GET','POST'])
def staff_bonus():
    form=StaffBonusForm()
    return render_template('staff/staff_bonus.html',form=form)

###############################################################

############staff_holiday
@staff.route('/staff_holiday',methods=['GET','POST'])
@login_required
def staff_holiday():
    form = StaffHolidayForm()
    bb=holidaytime = form.holidaytime.data
    aa=Staff.query.filter_by(staffid=current_user.get_id()).first().phone
    if form.validate_on_submit():
        holiday=Holiday(holidayid=form.holidayid.data,staff_staffid=current_user.get_id(),staff_phone=Staff.query.filter_by(staffid=current_user.get_id()).first().phone,holidaytype=form.holidaytype.data,holidaytime=form.holidaytime.data,holidayreason=form.holidayreason.data)
        db.session.add(holiday)
        db.session.commit()
        flash("登记成功")
    return render_template('staff/staff_holiday.html',form=form)

##########################################################################

@staff.route('/staff_reimbursement',methods=['POST','GET'])
@login_required
def staff_reimbursement():
    form = StaffReimbursementForm()
    if form.validate_on_submit():
        reimbursement=Reimbursement(reimbursementid=form.reimbursementid.data,reimbursementtype=form.reimbursementtype.data,reimbursementitem=form.reimbursementitem.data,
                                    reimbursementcost=form.reimbursementcost.data,reimbursementtime=datetime.utcnow(),staff_staffid=current_user.get_id())
        db.session.add(reimbursement)
        db.session.commit()
        flash("申请成功")
    return render_template('staff/staff_reimbursement.html',form=form)
