from . import main
from flask import render_template,make_response,redirect,url_for


@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/personnel_management/<string:page>',methods=['GET','POST'])
def personnel_management(page):
    return render_template('personnel_management.html',page=page)

@main.route("/staff_message",methods=['GET','POST'])
def staff_message():
    resp = make_response(redirect(url_for('.personnel_management',page="staff_message")))


    return resp