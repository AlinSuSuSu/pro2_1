from flask import render_template,url_for,redirect,request,make_response,flash
from app.finance import finance
from app.models import Waterfee,House,Electricfee,Gasfee,Cleaningfee
import json
from app import db
import time
from datetime import date
from flask_moment import Moment
import datetime
@finance.route('/waterfee')
def waterfee():
    charge=True
    query_house = House.query.all()
    query_all=Waterfee.query.all()
    waterfeepay=request.args.getlist('waterfeepay')
    houseid=request.args.get('houseid')
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys=Waterfee.query.filter_by(enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()).all()
    else:
        if (houseid != '' and houseid is not None) or (waterfeepay is not None and len(waterfeepay) != 0):
            if (houseid == '' or houseid is None) and len(waterfeepay) == 1:
                querys = Waterfee.query.filter_by(pay=waterfeepay[0])
            elif ((len(waterfeepay) == 0 or waterfeepay is None)) or (
                            len(waterfeepay) == 2 and (houseid != '' and houseid is not None)):

                querys = Waterfee.query.filter_by(house_houseid=houseid)
            elif len(waterfeepay) == 1:
                querys = Waterfee.query.filter_by(house_houseid=houseid, pay=waterfeepay[0])
            else:
                querys = Waterfee.query.all()
        else:
            querys = Waterfee.query.all()
    return render_template('/finance/waterfee.html',charge=charge,query_all=query_all,querys=querys,query_house=a)
@finance.route('/waterfee/orderdesc')
def orderdesc():
    resp=make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('waterfeeorder','1',max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/orderasc')
def orderasc():
    resp=make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('waterfeeorder','',max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/charge')
def watercharge():
    resp = make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/waterfee/notcharge')
def waternotcharge():
    resp = make_response(redirect(url_for('finance.waterfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/add',methods=['POST','GET'])
def fee_add():
    type=request.form.get('type')
    if type is not None and type != '':
        if type =='水费':
            addfee=Waterfee(house_houseid=request.form.get('finance-houseid'),startdegree=0,enddegree=0)
            addfee.startdate = datetime.datetime.strptime(request.form.get('startdate').strip(), '%Y-%m-%d').date()
            addfee.enddate = addfee.startdate
            addfee.waterfeeid = str(addfee.enddate) + str(addfee.startdate) + addfee.house_houseid
            addfee.totalprice = 0
            q_water = Waterfee.query.filter_by(waterfeeid=addfee.waterfeeid).first()
            if q_water is  None:
                db.session.add(addfee)
                db.session.commit()
            else:
                flash("已经生成过该条记录")
            return redirect(url_for('finance.waterfee'))
        elif type=='电费':
            addfee=Electricfee(house_houseid=request.form.get('finance-houseid'),startdegree=0,enddegree=0)
            addfee.startdate = datetime.datetime.strptime(request.form.get('startdate').strip(), '%Y-%m-%d').date()
            addfee.enddate = addfee.startdate
            addfee.electricfeeid = str(addfee.enddate) + str(addfee.startdate) + addfee.house_houseid
            addfee.totalprice = 0
            q_electric = Electricfee.query.filter_by(electricfeeid=addfee.electricfeeid).first()
            if q_electric is None:
                db.session.add(addfee)
                db.session.commit()
            else:
                flash("已经生成过该条记录")
            return redirect(url_for('finance.electricfee'))
        elif type=='天然气费':
            addfee=Gasfee(house_houseid=request.form.get('finance-houseid'),startdegree=0,enddegree=0)
            addfee.startdate = datetime.datetime.strptime(request.form.get('startdate').strip(), '%Y-%m-%d').date()
            addfee.enddate = addfee.startdate
            addfee.gasfeeid = str(addfee.enddate) + str(addfee.startdate) + addfee.house_houseid
            addfee.totalprice = 0
            q_gas = Gasfee.query.filter_by(gasfeeid=addfee.gafeeid).first()
            if q_gas is None:
                db.session.add(addfee)
                db.session.commit()
            else:
                flash("已经生成过该条记录")
            return redirect(url_for('finance.gasfee'))
        elif type=='卫生费':
            addcleaningfee=Cleaningfee(house_houseid=request.form.get('finance-houseid'))
            addcleaningfee.startdate=datetime.datetime.strptime(request.form.get('startdate').strip(),"%Y-%m-%d").date()
            addcleaningfee.enddate=addcleaningfee.startdate
            addcleaningfee.cleaningfeeid=str(addcleaningfee.enddate)+str(addcleaningfee.startdate)+addcleaningfee.house_houseid
            q_cleaning = Cleaningfee.query.filter_by(cleaningfeeid=addcleaningfee.cleaningfeeid).first()
            if q_cleaning is None:
                db.session.add(addcleaningfee)
                db.session.commit()
            else:
                flash("已经生成过该条记录")
            return redirect(url_for('finance.cleaningfee'))
    return redirect(url_for('finance.waterfee'))
@finance.route('/waterfee/create/',methods=['GET','POST'])
def waterfee_create():
    query_house=House.query.all()
    query_waterfee=Waterfee.query.first()
    date=datetime.datetime.now()
    if query_waterfee is not None and (query_waterfee.startdate.year==date.year and query_waterfee.startdate.month==date.month-1):
        flash("本月已经生成了账单")
    else:
        for v in query_house:
            waterfee=Waterfee(house_houseid=v.houseid,totalprice=0)
            waterfee.startdate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month-1)+"01","%Y%m%d").date()
            waterfee.startdegree=0
            waterfee.enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
            waterfee.enddegree=waterfee.startdegree
            waterfee.waterfeeid=str(waterfee.enddate)+str(waterfee.startdate)+waterfee.house_houseid
            #waterfee.waterfeeid=datetime.datetime.strftime("%Y%m%d",waterfee.startdate)+waterfee.house_houseid
            q_waterfee=Waterfee.query.filter_by(waterfeeid = waterfee.waterfeeid).first()
            if q_waterfee is None:
                db.session.add(waterfee)
                db.session.commit()

    return redirect(url_for("finance.waterfee"))

@finance.route('/waterfee/delete/<string:houseid>',methods=['GET','POST'])
def waterfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    waterfee = Waterfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(waterfee)
    db.session.commit()
    return json.dumps(res)
@finance.route('/waterfee/modify/<string:houseid>',methods=['POST','GET'])
def waterfee_modify(houseid):
    query=Waterfee.query.filter_by(house_houseid=houseid).first()
    return render_template("/finance/waterfee_modify.html",query=query)
@finance.route('/waterfee/modify/post',methods=['POST','GET'])
def waterfee_modify_post():
    waterfee=Waterfee.query.filter_by(waterfeeid=request.form.get('detail_waterfeeid')).first()
    waterfee.startdegree=request.form.get('detail_startdegree')
    waterfee.enddegree=request.form.get('detail_enddegree')
    waterfee.startdate=datetime.datetime.strptime(request.form.get('detail_startdate').strip(),"%Y-%m-%d")
    waterfee.enddate=datetime.datetime.strptime(request.form.get('detail_enddate').strip(),"%Y-%m-%d")
    waterfee.pay=request.form.get("detail_pay")
    if float(waterfee.enddegree) - float(waterfee.startdegree) > 0:
        waterfee.totalprice=float('%0.2f'%((float(waterfee.enddegree)-float(waterfee.startdegree))*float(waterfee.priceperdegree)))
    else:
        waterfee.totalprice=0
    db.session.add(waterfee)
    db.session.commit()
    return redirect(url_for('finance.waterfee'))

@finance.route("/waterfeee/save/<string:waterfeeid>",methods=['POST','GET'])
def waterfee_save(waterfeeid):
    data = json.loads(request.form.get('data'))
    query=Waterfee.query.filter_by(waterfeeid=waterfeeid).first()
    query.startdegree=data['startdegree']
    return redirect(url_for('finance.waterfee'))

@finance.route('/electricfee')
def electricfee():
    charge=True
    query_house = House.query.all()
    query_all = Electricfee.query.all()
    waterfeepay = request.args.getlist('electricfeepay')
    houseid = request.args.get('houseid')
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        # querys=Waterfee.query.all()
        querys = Electricfee.query.filter_by(enddate=datetime.datetime.strptime(
            str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + "01", "%Y%m%d").date()).all()
    else:
        if (houseid != '' and houseid is not None) or (waterfeepay is not None and len(waterfeepay) != 0):
            if (houseid == '' or houseid is None) and len(waterfeepay) == 1:
                querys = Electricfee.query.filter_by(pay=waterfeepay[0])
            elif ((len(waterfeepay) == 0 or waterfeepay is None)) or (
                            len(waterfeepay) == 2 and (houseid != '' and houseid is not None)):

                querys = Electricfee.query.filter_by(house_houseid=houseid)
            elif len(waterfeepay) == 1:
                querys = Electricfee.query.filter_by(house_houseid=houseid, pay=waterfeepay[0])
            else:
                querys = Electricfee.query.all()
        else:
            querys = Electricfee.query.all()

    return render_template('/finance/electricfee.html',charge=charge,querys=querys,query_house=a,query_all=query_all)

@finance.route('/electricfee/charge')
def electriccharge():
    resp = make_response(redirect(url_for('finance.electricfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/electricfee/notcharge')
def electricnotcharge():
    resp = make_response(redirect(url_for('finance.electricfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp

@finance.route('/electric/create/',methods=['GET','POST'])
def electricfee_create():

    query_house=House.query.all()
    query_electricfee=Electricfee.query.first()
    date=datetime.datetime.now()
    if query_electricfee is not None and query_electricfee.startdate.year==date.year and query_electricfee.startdate.month==date.month-1:
        flash("已经生成了账单")
    else:
        for v in query_house:
            electricfee=Electricfee(house_houseid=v.houseid,totalprice=0)
            electricfee.startdate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month-1)+"01","%Y%m%d").date()
            electricfee.startdegree=0
            electricfee.enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
            electricfee.enddegree=electricfee.startdegree
            electricfee.electricfeeid=str(electricfee.enddate)+str(electricfee.startdate)+electricfee.house_houseid
            q_electric = Electricfee.query.filter_by(electricfeeid=electricfee.electricfeeid).first()
            if q_electric is None:
                db.session.add(electricfee)
                db.session.commit()

    return redirect(url_for("finance.electricfee"))
@finance.route('/electricfee/add',methods=['POST','GET'])
def electricfee_add():
    electricfee=Electricfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    electricfee.totalprice=(electricfee.enddegree-electricfee.startdegree)*electricfee.priceperdegree
    db.session.add(electricfee)
    db.session.commit()
    return redirect(url_for('finance.electricfee'))

@finance.route('/electricfee/delete/<string:houseid>',methods=['GET','POST'])
def electricfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    electricfee = Electricfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(electricfee)
    db.session.commit()
    return json.dumps(res)
@finance.route('/electricfee/modify/<string:houseid>',methods=['POST','GET'])
def electric_modify(houseid):
    query=Electricfee.query.filter_by(house_houseid=houseid).first()
    return render_template("/finance/electricfee_modify.html",query=query)
@finance.route('/electricfee/modify/post',methods=['POST','GET'])
def electric_modify_post():
    electricfee=Electricfee.query.filter_by(electricfeeid=request.form.get('detail_waterfeeid')).first()
    electricfee.startdegree=request.form.get('detail_startdegree')
    electricfee.enddegree=request.form.get('detail_enddegree')
    electricfee.startdate=datetime.datetime.strptime(request.form.get('detail_startdate').strip(),"%Y-%m-%d")
    electricfee.enddate=datetime.datetime.strptime(request.form.get('detail_enddate').strip(),"%Y-%m-%d")
    electricfee.pay=request.form.get("detail_pay")
    if float(electricfee.enddegree) - float(electricfee.startdegree) > 0:
        electricfee.totalprice=float('%0.2f'%((float(electricfee.enddegree)-float(electricfee.startdegree))*float(electricfee.priceperdegree)))
    else:
        electricfee.totalprice=0
    db.session.add(electricfee)
    db.session.commit()
    return redirect(url_for('finance.electricfee'))


@finance.route('/gasfee')
def gasfee():
    charge=True
    query_house = House.query.all()
    query_all = Electricfee.query.all()
    waterfeepay = request.args.getlist('gasfeepay')
    houseid = request.args.get('houseid')
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        # querys=Waterfee.query.all()
        querys = Gasfee.query.filter_by(enddate=datetime.datetime.strptime(
            str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + "01", "%Y%m%d").date()).all()
    else:
        if (houseid != '' and houseid is not None) or (waterfeepay is not None and len(waterfeepay) != 0):
            if (houseid == '' or houseid is None) and len(waterfeepay) == 1:
                querys = Gasfee.query.filter_by(pay=waterfeepay[0])
            elif ((len(waterfeepay) == 0 or waterfeepay is None)) or (
                            len(waterfeepay) == 2 and (houseid != '' and houseid is not None)):

                querys = Gasfee.query.filter_by(house_houseid=houseid)
            elif len(waterfeepay) == 1:
                querys = Gasfee.query.filter_by(house_houseid=houseid, pay=waterfeepay[0])
            else:
                querys = Gasfee.query.all()
        else:
            querys = Gasfee.query.all()

    return render_template('/finance/gasfee.html',charge=charge,querys=querys,query_house=a,query_all=query_all)

@finance.route('/gasfee/charge')
def gascharge():
    resp = make_response(redirect(url_for('finance.gasfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/gasfee/notcharge')
def gasnotcharge():
    resp = make_response(redirect(url_for('finance.gasfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp

@finance.route('/gasfee/create/',methods=['GET','POST'])
def gasfee_create():
    query_house=House.query.all()
    query_gasfee=Gasfee.query.first()
    date=datetime.datetime.now()
    if query_gasfee is not None and query_gasfee.startdate.year==date.year and query_gasfee.startdate.month==date.month-1:
        flash("本月已经生成了账单")
    else:
        for v in query_house:
            gasfee=Gasfee(house_houseid=v.houseid,totalprice=0)
            gasfee.startdate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month-1)+"01","%Y%m%d").date()
            gasfee.startdegree=0
            gasfee.enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
            gasfee.enddegree=gasfee.startdegree
            gasfee.gasfeeid=str(gasfee.enddate)+str(gasfee.startdate)+gasfee.house_houseid
            q_gasfee = Gasfee.query.filter_by(gasfeeid=gasfee.gasfeeid).first()
            if q_gasfee is None:
                db.session.add(gasfee)
                db.session.commit()
    return redirect(url_for("finance.gasfee"))
@finance.route('/gasfee/add',methods=['POST','GET'])
def gasfee_add():
    gasfee=Gasfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    gasfee.totalprice=(gasfee.enddegree-gasfee.startdegree)*gasfee.priceperdegree
    db.session.add(gasfee)
    db.session.commit()
    return redirect(url_for('finance.gasfee'))

@finance.route('/gasfee/delete/<string:houseid>',methods=['GET','POST'])
def gasfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    gasfee = Gasfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(gasfee)
    db.session.commit()
    return json.dumps(res)

@finance.route('/gasfee/modify/<string:houseid>',methods=['POST','GET'])
def gas_modify(houseid):
    query=Gasfee.query.filter_by(house_houseid=houseid).first()
    return render_template("/finance/gasfee_modify.html",query=query)
@finance.route('/gasfee/modify/post',methods=['POST','GET'])
def gas_modify_post():
    gasfee=Gasfee.query.filter_by(gasfeeid=request.form.get('detail_waterfeeid')).first()
    gasfee.startdegree=request.form.get('detail_startdegree')
    gasfee.enddegree=request.form.get('detail_enddegree')
    gasfee.startdate=datetime.datetime.strptime(request.form.get('detail_startdate').strip(),"%Y-%m-%d")
    gasfee.enddate=datetime.datetime.strptime(request.form.get('detail_enddate').strip(),"%Y-%m-%d")
    gasfee.pay=request.form.get("detail_pay")
    if float(gasfee.enddegree) - float(gasfee.startdegree) > 0:
        gasfee.totalprice=float('%0.2f'%((float(gasfee.enddegree)-float(gasfee.startdegree))*float(gasfee.priceperdegree)))
    else:
        gasfee.totalprice=0
    db.session.add(gasfee)
    db.session.commit()
    return redirect(url_for('finance.gasfee'))

#############天然气费

###
@finance.route('/cleaningfee')
def cleaningfee():
    charge=True
    query_house = House.query.all()
    query_all = Electricfee.query.all()
    waterfeepay = request.args.getlist('cleaningfeepay')
    houseid = request.args.get('houseid')
    a=[]
    for querya  in query_house:
        a.append(querya.houseid)
    charge = bool(request.cookies.get('charge', ''))
    if charge:
        querys = Cleaningfee.query.filter_by(enddate=datetime.datetime.strptime(
            str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + "01", "%Y%m%d").date()).all()
    else:
        if (houseid != '' and houseid is not None) or (waterfeepay is not None and len(waterfeepay) != 0):
            if (houseid == '' or houseid is None) and len(waterfeepay) == 1:
                querys = Cleaningfee.query.filter_by(pay=waterfeepay[0])
            elif ((len(waterfeepay) == 0 or waterfeepay is None)) or (
                            len(waterfeepay) == 2 and (houseid != '' and houseid is not None)):

                querys = Cleaningfee.query.filter_by(house_houseid=houseid)
            elif len(waterfeepay) == 1:
                querys = Cleaningfee.query.filter_by(house_houseid=houseid, pay=waterfeepay[0])
            else:
                querys = Cleaningfee.query.all()
        else:
            querys = Cleaningfee.query.all()
    return render_template('/finance/cleaningfee.html',charge=charge,querys=querys,query_house=a,query_all=query_all)

@finance.route('/cleaningfee/charge')
def cleaningcharge():
    resp = make_response(redirect(url_for('finance.cleaningfee')))
    resp.set_cookie('charge', '1', max_age=30 * 24 * 60 * 60)
    return resp
@finance.route('/cleaningfee/notcharge')
def cleaningnotcharge():
    resp = make_response(redirect(url_for('finance.cleaningfee')))
    resp.set_cookie('charge', '', max_age=30 * 24 * 60 * 60)
    return resp

@finance.route('/cleaning/create/',methods=['GET','POST'])
def cleaningfee_create():
    query_house=House.query.all()
    query_cleaningfee=Cleaningfee.query.first()
    date=datetime.datetime.now()
    if query_cleaningfee is not None and query_cleaningfee.startdate.year==date.year and query_cleaningfee.startdate.month==date.month-1:
        flash("本月已经生成了账单")
    else:
        for v in query_house:
            cleaningfee=Cleaningfee(house_houseid=v.houseid)
            cleaningfee.startdate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month-1)+"01","%Y%m%d").date()
            cleaningfee.enddate=datetime.datetime.strptime(str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+"01","%Y%m%d").date()
            cleaningfee.cleaningfeeid=str(cleaningfee.enddate)+str(cleaningfee.startdate)+cleaningfee.house_houseid
            q_cleaningfee = Cleaningfee.query.filter_by(cleaningfeeid=cleaningfee.cleaningfeeid).first()
            if q_cleaningfee is None:
                db.session.add(cleaningfee)
                db.session.commit()
    return redirect(url_for("finance.cleaningfee"))


@finance.route('/cleaningfee/add',methods=['POST','GET'])
def cleaningfee_add():
    cleaningfee=Cleaningfee(house_houseid=request.form.get('finance-houseid'),startdegree=request.form.get('startdegree'),enddegree=request.form.get('enddegree'))
    cleaningfee.totalprice=(cleaningfee.enddegree-cleaningfee.startdegree)*cleaningfee.priceperdegree
    db.session.add(cleaningfee)
    db.session.commit()
    return redirect(url_for('finance.cleaningfee'))

@finance.route('/cleaningfee/delete/<string:houseid>',methods=['GET','POST'])
def cleaningfee_delete(houseid):
    res = {
        "status": 1,
        "message": "success"
    }
    cleaningfee = Cleaningfee.query.filter_by(house_houseid=houseid).first()
    db.session.delete(cleaningfee)
    db.session.commit()
    return json.dumps(res)
@finance.route('/cleaningfee/modify/<string:houseid>',methods=['POST','GET'])
def cleaningfee_modify(houseid):
    query=Cleaningfee.query.filter_by(house_houseid=houseid).first()
    return render_template("/finance/cleaningfee_modify.html",query=query)
@finance.route('/cleaningfee/modify/post',methods=['POST','GET'])
def cleaningfee_modify_post():
    cleaningfee=Cleaningfee.query.filter_by(cleaningfeeid=request.form.get('detail_waterfeeid')).first()
    cleaningfee.startdate=datetime.datetime.strptime(request.form.get('detail_startdate').strip(),"%Y-%m-%d")
    cleaningfee.enddate=datetime.datetime.strptime(request.form.get('detail_enddate').strip(),"%Y-%m-%d")
    cleaningfee.pay=request.form.get("detail_pay")
    db.session.add(cleaningfee)
    db.session.commit()
    return redirect(url_for('finance.cleaningfee'))



#业主个人缴费情况
@finance.route('/charge/personal/<string:houseid>',methods=['POST','GET'])
def personal_charge(houseid):
    query_water=Waterfee.query.filter_by(house_houseid=houseid)
    query_electric=Electricfee.query.filter_by(house_houseid=houseid)
    query_gas=Gasfee.query.filter_by(house_houseid=houseid)
    query_cleaning=Cleaningfee.query.filter_by(house_houseid=houseid)
    return render_template('/finance/personal_charge.html',query_water=query_water,query_electric=query_electric,query_gas=query_gas,query_cleaning=query_cleaning)