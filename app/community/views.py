from flask import url_for,render_template,request,redirect
from app import db
from app.models import Repairation,Patrol,Staff,Infrastructure,Complaint,Owner,House,Choice
from app.community import community
import json
from datetime import datetime
@community.route('/repairation/',methods=['GET','POST'])
def repairation():
    queryall=Repairation.query.all()
    repairationcheck=request.args.getlist('repairationcheck')
    houseid=request.args.get('houseid')
    if (houseid != '' and houseid is not None) or (repairationcheck is not None and len(repairationcheck)!=0):
        if (houseid == '' or houseid is  None) and len(repairationcheck)==1:
            querys = Repairation.query.filter_by(repairationcheck=repairationcheck[0])
        elif ((len(repairationcheck) ==0 or repairationcheck is None)) or (len(repairationcheck)==2 and (houseid != '' and houseid is not None)) :

            querys = Repairation.query.filter_by(house_houseid=houseid)
        elif len(repairationcheck)==1:
            querys = Repairation.query.filter_by(house_houseid=houseid,repairationcheck=repairationcheck[0])
        else:
            querys=Repairation.query.all()
    else:
        querys = Repairation.query.all()
    return render_template('community/repairation.html',querys=querys,queryall=queryall)

@community.route('/repairation/apply',methods=['GET','POST'])
def repairation_apply():
    query_owner=Owner.query.all()
    query_house=House.query.all()
    query_staff=Staff.query.all()

    return render_template('community/repairation_apply.html',query_owner=query_owner)

@community.route('/repairation/apply/post',methods=['POST','GET'])
def repairation_apply_post():
    repairation=Repairation(house_houseid=request.form.get('add_house_houseid'),
                repairationcontent=request.form.get('add_repairationcontent'),repairationestimatedcost=request.form.get('add_repairationestimatedcost'),
                repairationactualcost=request.form.get('add_repairationactualcost'),repairationresperson=request.form.get('add_repairationresperson'),
                        repairationresphone=request.form.get('add_repairationresphone'),repairationsupervisitor=request.form.get('add_repairationsupervisitor'),repairationtime=datetime.strptime((request.form.get('add_repairationtime')).strip(),"%Y-%m-%d"),
                        repairationcomptime=datetime.strptime((request.form.get('add_repairationcomptime')).strip(),"%Y-%m-%d"),repairationcheck=request.form.get('add_repairationcheck'))
    repairation.repairationreplytime=datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    repairation.repairationid=str(repairation.repairationreplytime)+repairation.house_houseid
    query= Owner.query.filter_by(house_houseid=repairation.house_houseid).first()
    if query is not None:
        repairation.owner_ownername = query.ownername
    else:
        repairation.owner_ownername = ''
    db.session.add(repairation)
    db.session.commit()
    return redirect(url_for('community.repairation'))
@community.route('/repairation/detail/post',methods=['POST','GET'])
def repairation_detail_post():
    repairation=Repairation.query.filter_by(repairationid=request.form.get("add_repairationid")).first()
    repairation.repairationcontent=request.form.get('add_repairationcontent')
    repairation.repairationestimatedcost=request.form.get('add_repairationestimatedcost')
    repairation.repairationactualcost=request.form.get('add_repairationactualcost')
    repairation.repairationresperson=request.form.get('add_repairationresperson')
    repairation.repairationresphone=request.form.get('add_repairationresphone')
    repairation.repairationsupervisitor=request.form.get('add_repairationsupervisitor')
    repairation.repairationtime=datetime.strptime((request.form.get('add_repairationtime')).strip(),"%Y-%m-%d")
    repairation.repairationcomptime=datetime.strptime((request.form.get('add_repairationcomptime')).strip(),"%Y-%m-%d")
    repairation.repairationcheck=request.form.get('add_repairationcheck')

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

@community.route('/repairation/detail/<string:repairationid>',methods=['GET','POST'])
def repairation_detail(repairationid):
    query=Repairation.query.filter_by(repairationid=repairationid).first()
    return render_template('community/repairation_detail.html',query=query)

@community.route('/patrol',methods=['GET','POST'])
def patrol():
    eventtype = request.args.get('eventtype')
    query_all=Patrol.query.all()
    if eventtype != '' and eventtype is not None:
        query_patrol =Patrol.query.filter_by(eventtype=eventtype)
    else:
        query_patrol=Patrol.query.all()
    return render_template('community/patrol.html',query_patrol=query_patrol,query_all=query_all)

@community.route('/patrol/add',methods=['GET','POST'])
def patrol_add():
    query_staff=Staff.query.all()
    query_choice = Choice.query.filter_by(choicetype="保安巡逻")
    return render_template('community/add_patrol.html',query_staff=query_staff,query_choice=query_choice)

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
    query_all=Infrastructure.query.all()
    infrastructuretype=request.args.get('infrastructuretype')
    if infrastructuretype is not None and infrastructuretype !='':
        query_infrastructure=Infrastructure.query.filter_by(infrastructuretype=infrastructuretype)
    else:
        query_infrastructure=Infrastructure.query.all()
    return render_template('community/infrastructure.html',query_all=query_all,query_infrastructure=query_infrastructure)

@community.route('/infrastructure/add',methods=['GET','POST'])
def infrastructure_add():
    query_choice=Choice.query.filter_by(choicetype="绿化基建")
    return render_template('community/add_infrastructure.html',query_choice=query_choice)

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
    query_all= Complaint.query.all()
    complainttype=request.args.get('complainttype')
    if complainttype is not None or complainttype !='':
        query_complaint=Complaint.query.filter_by(complainttype=complainttype)
    else:
        query_complaint=Complaint.query.all()
    return render_template('community/complaint.html',query_all=query_all,query_complaint=query_complaint)

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