from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,SubmitField,BooleanField,RadioField
from wtforms.validators import Regexp,Required,EqualTo
from app.models import Staff
from wtforms import ValidationError



class StaffAddForm(FlaskForm):
    staffid = StringField("员工编号")
    staffname = StringField("员工姓名")
    staffphone = StringField("联系方式")
    staffgender = RadioField("性别", choices=[('男', '男'), ('女', '女')])
    submit=SubmitField("添加")

class StaffBonusForm(FlaskForm):
    staffid = StringField("员工编号")
    staffname = StringField("员工姓名")
    staffphone = StringField("联系方式")
    staffgender = RadioField("性别", choices=[('男', '男'), ('女', '女')])
    submit = SubmitField("添加")

