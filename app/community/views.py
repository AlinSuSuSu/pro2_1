from flask import url_for,render_template,request,redirect
from app import db
from app.models import Repairation,Patrol,Staff,Infrastructure,Complaint
from app.community import community
import json
from datetime import datetime
@community.route('/repairation/',methods=['GET','POST'])
def repairation():
    queryall=Repairation.query.all()
    repairationid=request.args.get('repairationid')
    houseid=request.args.get('houseid')
    if (houseid != '' and houseid is not None) or (repairationid is not None and repairationid != ''):
        if houseid == '' or houseid is  None:
            querys = Repairation.query.filter_by(repairationid=repairationid)
        elif repairationid == '' or repairationid is None:
            querys = Repairation.query.filter_by(house_houseid=houseid)
        else:
            querys = Repairation.query.filter_by(house_houseid=houseid,repairationid=repairationid)
    else:
        querys = Repairation.query.all()
    return render_template('community/repairation.html',querys=querys,queryall=queryall)

@community.route('/repairation/apply',methods=['GET','POST'])
def repairation_apply():
    return render_template('community/repairation_apply.html')

@community.route('/repairation/apply/post',methods=['POST','GET'])
def repairation_apply_post():
    repairation=Repairation(repairationid=request.form.get('add_repairationid'),house_houseid=request.form.get('add_house_houseid'),owner_ownername=request.form.get('add_ownername'),
                repairationcontent=request.form.get('add_repairationcontent'),repairationestimatedcost=request.form.get('add_repairationestimatedcost'),
                repairationactualcost=request.form.get('add_repairationactualcost'),repairationresperson=request.form.get('add_repairationresperson'),
                        repairationresphone=request.form.get('add_repairationresphone'),repairationsupervisitor=request.form.get('add_repairationsupervisitor'),repairationtime=request.form.get('add_repairationtime'),
                        repairationcomptime=request.form.get('add_repairationcomptime'),repairationcheck=request.form.get('add_repairationcheck'))
    db.session.add(repairation)
    db.session.commit()
    return redirect(url_for('community.repairation'))


@community.route('/repairation/delete/<string:repairationid>',methods=['GET','POST'])
def repairation_delete(repairationid):
    res = {
        "status": 1,
        "message": "success"
    }
    repairation = Repairation.query.filter_by(repairationid=repairationid).first()
    db.session.delete(repairation)
    db.session.commit()
    return json.dumps(res)

@community.route('/repairation/detail/<int:repairationid>',methods=['GET','POST'])
def repairation_detail(repairationid):
    query=Repairation.query.filter_by(repairationid=repairation)
    return render_template('community/repairation_detail.html',query=query)

@community.route('/patrol',methods=['GET','POST'])
def patrol():
    query_patrol=Patrol.query.all()
    return render_template('community/patrol.html',query_patrol=query_patrol)

@community.route('/patrol/add',methods=['GET','POST'])
def patrol_add():
    query_staff=Staff.query.all()
    return render_template('community/add_patrol.html',query_staff=query_staff)

@community.route('/patrol/add/post',methods=['GET','POST'])
def patrol_add_post():
    patrol=Patrol(patrolid=request.form.get('patrol_patrolid'),eventtype=request.form.get('patrol_eventtype'),eventtime=datetime.strptime(request.form.get('patrol_eventtime'), "%Y-%m-%d-%H"),
                  solveperson=request.form.get('patrol_solveperson'),personinvolved=request.form.get('patrol_personinvolved'),
                  phoneinvolved=request.form.get('patrol_phoneinvolved'),eventresult=request.form.get('patrol_eventresult'),eventdetail=request.form.get('patrol_eventdetail'))
    db.session.add(patrol)
    db.session.commit()
    return redirect(url_for('community.patrol'))
@community.route("/patrol/delete/<string:patrolid>",methods=['POST','GET'])
def patrol_delete(patrolid):
    res = {
        "status": 1,
        "message": "success"
    }
    patrol = Patrol.query.filter_by(patrolid=patrolid).first()
    db.session.delete(patrol)
    db.session.commit()
    return json.dumps(res)

@community.route('/patrol/detail/<string:patrolid>',methods=['POST','GET'])
def patrol_detail(patrolid):
    query = Patrol.query.filter_by(patrolid=patrolid)
    return render_template('community/patrol_detail.html', query=query)

@community.route('/infrastructure',methods=['GET','POST'])
def infrastructure():
    return render_template('community/infrastructure.html')

@community.route('/infrastructure/add',methods=['GET','POST'])
def infrastructure_add():
    return render_template('community/add_infrastructure.html')

@community.route('/infrastructure/delete/<string:infrastructureid>',methods=['GET','POST'])
def infrastructure_delete(infrastructureid):
    res = {
        "status": 1,
        "message": "success"
    }
    infrastructure = Infrastructure.query.filter_by(infrastructureid=infrastructureid).first()
    db.session.delete(infrastructure)
    db.session.commit()
    return json.dumps(res)

@community.route('/infrastructure/detail/<string:infrastructureid>',methods=['GET','POST'])
def infrastructure_detail(infrastructureid):
    query = Infrastructure.query.filter_by(infrastructureid=infrastructureid)
    return render_template('community/infrastructure_detail.html',query=query)


@community.route('/infrastructure/add/post',methods=['GET','POST'])
def infrastructure_add_post():
    infrastructure = Infrastructure(infrastructureid=request.form.get('infrastructure_infrastructureid'), infrastructuretype=request.form.get('infrastructure_infrastructuretype'),
                                    infrastructuretime=datetime.strptime(request.form.get('infrastructure_infrastructuretime'), "%Y-%m-%d"),
                                    infrastructurearea=request.form.get('infrastructure_infrastructurearea'),
                                    resperson=request.form.get('infrastructure_resperson'),
                                    resphone=request.form.get('infrastructure_resphone'),
                                    supervisitor=request.form.get('infrastructure_supervisitor'),
                                    check=request.form.get('infrastructure_check'),detail=request.form.get('infrastructure_detail'))
    db.session.add(infrastructure)
    db.session.commit()
    return redirect(url_for('community.infrastructure'))

@community.route('/complaint',methods=['GET','POST'])
def complaint():
    return render_template('community/complaint.html')

@community.route('/complaint/delete/<string:complaintid>',methods=['GET','POST'])
def complaint_delete(complaintid):
    res = {
        "status": 1,
        "message": "success"
    }
    complaint = Complaint.query.filter_by(complaintid=complaintid).first()
    db.session.delete(complaint)
    db.session.commit()
    return json.dumps(res)

@community.route('/complaint/add',methods=['GET','POST'])
def complaint_add():
    return render_template('community/add_complaint.html')

@community.route('/complaint/add/post',methods=['GET','POST'])
def complaint_add_post():
    complaint = Complaint(infrastructureid=request.form.get('complaint_infrastructureid'),
                                    infrastructuretype=request.form.get('complaint_infrastructuretype'),
                                    infrastructuretime=datetime.strptime(
                                        request.form.get('complaint_infrastructuretime'), "%Y-%m-%d"),
                                    infrastructurearea=request.form.get('complaint_infrastructurearea'),
                                    resperson=request.form.get('complaint_resperson'),
                                    resphone=request.form.get('complaint_resphone'),
                                    supervisitor=request.form.get('complaint_supervisitor'),
                                    check=request.form.get('complaint_check'),
                                    detail=request.form.get('complaint_detail'))
    db.session.add(complaint)
    db.session.commit()
    return redirect(url_for('community.complaint'))

@community.route('/complaint/<string:complaintid>',methods=['GET','POST'])
def complaint_detail(complaintid):
    query = Infrastructure.query.filter_by(complaintid=complaintid)
    return render_template('community/complaint_detail.html',query=query)