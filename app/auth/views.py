from flask import render_template,flash,redirect,request,url_for
from . import auth
from ..models import Staff
from .forms import LoginForm,RegistrationForm,ChangePasswordForm,ChangeMessageForm,ProfileForm
from flask_login import login_user,logout_user,login_required,current_user
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


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("您已退出登录")
    return redirect(url_for('main.index'))

@auth.route('/change_message',methods=['GET','POST'])
@login_required
def change_message():
    form = ChangeMessageForm()
    if form.validate_on_submit():
        current_user.salary=form.salary.data
        current_user.phone=form.phone.data
        current_user.phone=form.phone.data
        current_user.idcard=form.idcard.data
        current_user.job=form.job.data
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('auth/change_message.html',form=form)

@auth.route('/change_password',methods=['GET','POST'])
@login_required
def change_password():
    form = ChangePasswordForm()

    return render_template('auth/change_password.html',form=form)

@auth.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form = ProfileForm()


    return render_template('auth/profile.html',form=form)
