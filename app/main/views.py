from . import main
from flask import render_template,make_response,redirect,url_for,request,flash
from .forms import StaffBonusForm,StaffAddForm
from ..models import Staff
from .. import db
import json
@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/personnel_message',methods=['GET','POST'])
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
    return render_template('staff/personnel_management.html',querys=querys)


@main.route('/detail/<int:staff_id>/delete',methods=['POST','GET'])
def staff_delete(staff_id):
    res = {
        "status": 1,
        "message": "success"
    }
    staff=Staff.query.filter_by(staffid=staff_id).first()
    db.session.delete(staff)
    db.session.commit()
    return json.dumps(res)

@main.route('/personnel_management/add',methods=['POST','GET'])
def staff_add():
    form = StaffAddForm()
    if form.validate_on_submit():
        staff = Staff(staffid=form.staffid.data, staffname=form.staffname.data, phone=form.staffphone.data,
                      gender=form.staffgender.data)
        db.session.add(staff)
        db.session.commit()
        flash("添加成功")
        return redirect(url_for('main.personnel_management'))
    return render_template('staff/add_staff.html', form=form)


@main.route('/personnel_management/detail/<int:staffid>',methods=['POST','GET'])
def staff_add_1():
    form = StaffAddForm()
    if form.validate_on_submit():
        staff = Staff(staffid=form.staffid.data, staffname=form.staffname.data, phone=form.staffphone.data,
                      gender=form.staffgender.data)
        db.session.add(staff)
        db.session.commit()
        flash("添加成功")
        return redirect(url_for('main.personnel_management'))
    return render_template('staff/add_staff.html', form=form)

###########人事管理，员工福利

@main.route('/personnel_bonus',methods=['GET','POST'])
def personnel_bonus():
    form=StaffBonusForm()
    return render_template('staff/personnel_bonus.html',form=form)

@main.route('/personnel_message',methods=['GET','POST'])
def personnel_message():
    return render_template('staff/personnel_message.html')