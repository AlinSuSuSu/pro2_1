from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,SelectField,DateField,SubmitField,BooleanField,RadioField
from wtforms.validators import Regexp,Required,EqualTo
from app.models import Staff
from datetime import datetime
from flask_login import current_user
from wtforms import ValidationError

class StaffBonusForm(FlaskForm):
    staffid = StringField("员工编号")
    staffname = StringField("员工姓名")
    staffphone = StringField("联系方式")
    staffgender = RadioField("性别", choices=[('男', '男'), ('女', '女')])
    submit = SubmitField("添加")

class StaffHolidayForm(FlaskForm):
    holidayid=StringField("申请编号")
    holidayreason=TextAreaField("请假原因")
    holidaytype=SelectField("休假类型",choices=[('事假','事假'),('病假','病假')])
    holidaytime=DateField("休假时间")
    submit = SubmitField("提交")

class StaffReimbursementForm(FlaskForm):
    reimbursementid=StringField("申请编号")
    reimbursementitem=TextAreaField("费用项目")
    reimbursementtype=TextAreaField("类别")
    reimbursementcost=StringField("金额")
    submit = SubmitField("提交")