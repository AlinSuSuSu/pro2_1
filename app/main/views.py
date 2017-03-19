from . import main
from flask import render_template,make_response,redirect,url_for,request,flash
from .forms import StaffMessageForm
from ..models import Staff

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/personnel_management/<string:page>',methods=['GET','POST'])
def personnel_management(page):
    form = StaffMessageForm()
    page = request.cookies.get("page",'')
    a = form.validate_on_submit();
    if form.validate_on_submit():
        if form.staffid.data is not None:
            querystaffs=Staff.query.filter_by(staffid=form.staffid.data).all()
            for stafs in querystaffs:
                b=stafs.staffid;
            return render_template('personnel_management.html',page=page,form=form,querystaffs=querystaffs)
        flash("meiyoushuju")
    return render_template('personnel_management.html',page=page,form=form)

@main.route("/staffmessage",methods=['GET','POST'])
def staff_message():
    resp = make_response(redirect(url_for('.personnel_management')))
    resp.set_cookie("page","staffmessage", max_age=30 * 24 * 60 * 60)
    return resp