from flask import render_template,flash,redirect,request,url_for
from . import auth
from ..models import Staff
from .forms import LoginForm,RegistrationForm
from flask_login import login_user
from app import db

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        staff = Staff.query.filter_by(staffid=form.staffid.data).first()
        if staff is not None and staff.verify_password((form.password.data)):
            login_user(staff,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("用户名或密码错误")
    return render_template('auth/login.html',form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        staff = Staff(staffid = form.staffid.data,staffname=form.staffname.data,password=form.password.data)
        db.session.add(staff)
        db.session.commit()
        flash("注册成功")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form )