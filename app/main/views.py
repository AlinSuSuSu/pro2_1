from app.main import main
from flask_login import login_required,login_user
from flask import render_template,redirect,request,url_for,flash
from app.auth.forms import  LoginForm
from app.models import User

@main.route('/',methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password((form.password.data)):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('house.house_message'))
        flash("用户名或密码错误")
    return render_template('index.html',form=form)