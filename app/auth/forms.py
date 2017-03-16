from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,SubmitField,BooleanField
from wtforms.validators import Regexp,Required,EqualTo
from ..models import Staff
from wtforms import ValidationError

class LoginForm(FlaskForm):
    staffid = StringField("员工编号", validators=[Required()])
    password = PasswordField("密码", validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField("登录")


class RegistrationForm(FlaskForm):
    staffid = StringField('员工编号',validators=[])
    staffname = StringField("员工姓名",validators=[])
    age = StringField("年龄",validators=[Required()])
    password =PasswordField('密码',validators=[Required(),EqualTo('password2',message='密码不匹配')])
    password2 = PasswordField('确认密码',validators=[Required()])
    #last_seen = db.Column(db.DateTime(), default=datetime.utcnow)  # 上次登录
    gender = SelectField('性别',coerce=str)  # 性别
    salary = StringField('薪资',validators=[Required()])  # 薪资
    phone = StringField('手机号码', validators=[Required()])  # 联系方式
    idcard = StringField('身份证号', )  # 身份证号
    job = StringField('职位')  # 工种
    submit = SubmitField('注册')

    def __init__(self,*args,**kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.gender.choices = [('nan','男'),('nv','女')]


    def validate_staffid(self,field):
        if Staff.query.filter_by(staffid = field.data).first():
            return ValidationError("编号已经被注册过")
    def validate_phone(self,field):
        if Staff.query.filter_by(phone=field.data).first():
            return ValidationError("手机号已经被注册过")

    def validate_staffname(self,field):
        if Staff.query.filter_by(staffname=field.data).first():
            return ValidationError("姓名已经被注册过")
    def validate_idcard(self,field):
        if Staff.query.filter_by(idcard=field.data).first():
            return ValidationError("身份证号已经被注册过")

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("旧密码",validators=[Required()])
    password = PasswordField('新密码',validators=[Required(), EqualTo('password2', message="password must match")])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('确认')


