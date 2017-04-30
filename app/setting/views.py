from flask import render_template,flash,redirect,request,url_for
from . import setting
from ..models import User,Role
from flask_login import login_user,logout_user,login_required,current_user
from app import db

@setting.route('/',methods=['POST','GET'])
def set():
    return render_template('setting/setting.html')
