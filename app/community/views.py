from flask import url_for,render_template,request,redirect
from app import db
from app.models import Repairation,Patrol,Staff,Infrastructure,Complaint,Owner,House,Choice
from app.community import community
import json
from flask_login import current_user,login_required
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
    return render_template('community/repairation_apply.html',query_owner=query_owner)

@community.route('/repairation/apply/post',methods=['POST','GET'])
def repairation_apply_post():
    repairation=Repairation(house_houseid=request.form.get('add_house_houseid'),
                repairationcontent=request.form.get('add_repairationcontent'),repairationestimatedcost=request.form.get('add_repairationestimatedcost'),
                repairationtime=datetime.strptime((request.form.get('add_repairationtime')).strip(),"%Y-%m-%d"))


    repairation.repairationreplytime=datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    repairation.repairationid=str(repairation.repairationreplytime)+repairation.house_houseid
    query= Owner.query.filter_by(house_houseid=repairation.house_houseid).first()
    if query is not None:
        repairation.owner_ownername = query.ownername
    else:
        repairation.owner_ownername = ''
    db.session.add(repairation)
    db.session.commit()
    return redirect(url_for('community.repairation_apply'))
@community.route('/repairation/detail/post',methods=['POST','GET'])
def repairation_detail_post():
    repairation=Repairation.query.filter_by(repairationid=request.form.get("detail_repairationid")).first()
    if request.form.get('detail_repairationcontent') is not None and request.form.get('detail_repairationcontent') !='':
        repairation.repairationcontent=request.form.get('detail_repairationcontent')
    repairation.repairationestimatedcost=request.form.get('detail_repairationestimatedcost')
    repairation.repairationactualcost=request.form.get('detail_repairationactualcost')
    repairation.repairationresperson=request.form.get('detail_repairationresperson')
    repairation.repairationresphone=request.form.get('detail_repairationresphone')
    repairation.repairationsupervisitor=request.form.get('detail_repairationsupervisitor')
    repairation.repairationtime=datetime.strptime((request.form.get('detail_repairationtime')).strip(),"%Y-%m-%d")
    repairation.repairationcomptime=datetime.strptime((request.form.get('detail_repairationcomptime')).strip(),"%Y-%m-%d")
    repairation.repairationcheck=request.form.get('detail_repairationcheck')

    db.session.add(repairation)
    db.session.commit()
    return redirect(url_for('community.repairation'))

@community.route('/apply/owner',methods=['GET','POST'])
def repairation_detail_owner():
    query = Repairation.query.filter_by(house_houseid=current_user.house_houseid)
    return render_template('community/owner_apply.html',query=query)


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
    query_staff=Staff.query.all()

    return render_template('community/repairation_detail.html',query=query,query_staff=query_staff)

@community.route('/patrol',methods=['GET','POST'])
def patrol():
    eventtype = request.args.get('eventtype')
    query_all=Patrol.query.all()
    query_choice=Choice.query.filter_by(choicetype="保安巡逻")
    if eventtype != '' and eventtype is not None:
        query_patrol =Patrol.query.filter_by(eventtype=eventtype)
    else:
        query_patrol=Patrol.query.all()
    return render_template('community/patrol.html',query_patrol=query_patrol,query_all=query_all,query_choice=query_choice)

@community.route('/patrol/add',methods=['GET','POST'])
def patrol_add():
    query_staff=Staff.query.all()
    query_choice = Choice.query.filter_by(choicetype="保安巡逻")
    return render_template('community/add_patrol.html',query_staff=query_staff,query_choice=query_choice)

@community.route('/patrol/add/post',methods=['GET','POST'])
def patrol_add_post():
    patrol=Patrol(eventtype=request.form.get('patrol_eventtype'),eventtime=datetime.strptime(request.form.get('patrol_eventtime').strip(),"%Y-%m-%d"),
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

@community.route('/patrol/detail/<int:patrolid>',methods=['POST','GET'])
def patrol_detail(patrolid):
    query_staff=Staff.query.all()
    query = Patrol.query.filter_by(patrolid=patrolid).first()
    return render_template('community/patrol_detail.html', query=query,query_staff=query_staff)

@community.route('/patrol/detail/post',methods=['POST','GET'])
def patrol_detail_post():
    query = Patrol.query.filter_by(patrolid=request.form.get('patrol_detail_patrolid')).first()
    query.eventtype=request.form.get('patrol_detail_eventtype')
    query.eventtime=datetime.strptime(request.form.get('patrol_detail_eventtime').strip(),"%Y-%m-%d")
    query.solveperson=request.form.get('patrol_detail_solveperson')
    query.personinvolved=request.form.get('patrol_detail_personinvolved')
    query.phoneinvolved=request.form.get('patrol_detail_phoneinvolved')
    query.eventresult=request.form.get('patrol_detail_eventresult')
    query.eventdetail=request.form.get('patrol_detail_eventdetail')
    db.session.add(query)
    db.session.commit()
    return redirect(url_for('community.patrol'))
@community.route('/infrastructure',methods=['GET','POST'])
def infrastructure():
    query_all=Infrastructure.query.all()
    query_choice=Choice.query.filter_by(choicetype="绿化基建")
    infrastructuretype=request.args.get('infrastructuretype')
    if infrastructuretype is not None and infrastructuretype !='':
        query_infrastructure=Infrastructure.query.filter_by(infrastructuretype=infrastructuretype)
    else:
        query_infrastructure=Infrastructure.query.all()
    return render_template('community/infrastructure.html',query_all=query_all,query_choice=query_choice,query_infrastructure=query_infrastructure)

@community.route('/infrastructure/add',methods=['GET','POST'])
def infrastructure_add():
    query_choice=Choice.query.filter_by(choicetype="绿化基建")
    query_staff=Staff.query.all()
    return render_template('community/add_infrastructure.html',query_choice=query_choice,query_staff=query_staff)

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

@community.route('/infrastructure/detail/<int:infrastructureid>',methods=['GET','POST'])
def infrastructure_detail(infrastructureid):
    query = Infrastructure.query.filter_by(infrastructureid=infrastructureid).first()
    query_choice=Choice.query.filter_by(choicetype="绿化基建")
    query_staff=Staff.query.all()
    return render_template('community/infrastructure_detail.html',query=query,query_choice=query_choice,query_staff=query_staff)


@community.route('/infrastructure/add/post',methods=['GET','POST'])
def infrastructure_add_post():
    infrastructure = Infrastructure(infrastructuretype=request.form.get('add_infrastructuretype'),
                                    infrastructuretime=datetime.strptime(request.form.get('add_infrastructuretime').strip(), "%Y-%m-%d"),
                                    infrastructurearea=request.form.get('add_infrastructurearea'),
                                    resperson=request.form.get('add_resperson'),
                                    resphone=request.form.get('add_resphone'),
                                    supervisitor=request.form.get('add_supervisitor'),
                                    check=request.form.get('add_check'),detail=request.form.get('add_detail'))
    db.session.add(infrastructure)
    db.session.commit()
    return redirect(url_for('community.infrastructure'))
@community.route('/infrastructure/detail/post',methods=['GET','POST'])
def infrastructure_detail_post():
    infrastructure=Infrastructure.query.filter_by(infrastructureid=request.form.get('detail_infrastructureid')).first()
    infrastructure.infrastructuretype=request.form.get('detail_infrastructuretype')
    infrastructure.infrastructuretime=datetime.strptime(request.form.get('detail_infrastructuretime').strip(), "%Y-%m-%d")
    infrastructure.infrastructurearea=request.form.get('detail_infrastructurearea')
    infrastructure.resperson=request.form.get('detail_resperson')
    infrastructure.resphone=request.form.get('detail_resphone')
    infrastructure.supervisitor=request.form.get('detail_supervisitor')
    infrastructure.check=request.form.get('detail_check')
    infrastructure.detail=request.form.get('detail_detail')
    db.session.add(infrastructure)
    db.session.commit()
    return redirect(url_for('community.infrastructure'))

@community.route('/complaint',methods=['GET','POST'])
def complaint():
    query_all= Complaint.query.all()
    complainttype=request.args.get('complainttype')
    if complainttype is not None and complainttype !='':
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
    complaint = Complaint(complainttype=request.form.get('add_complainttype'),house_houseid=request.form.get('add_houseid'),complaintdetail=request.form.get('add_complaintdetail'))
    complaint.complainttime=datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    db.session.add(complaint)
    db.session.commit()
    return redirect(url_for('community.complaint'))

@community.route('/complaint/<int:complaintid>',methods=['GET','POST'])
def complaint_detail(complaintid):
    query = Complaint.query.filter_by(complaintid=complaintid).first()
    return render_template('community/complaint_detail.html',query=query)

@community.route('/complaint/detail/post',methods=['GET','POST'])
def complaint_detail_post():
    complaint = Complaint.query.filter_by(complaintid=request.form.get('detail_repairationid'))
    complaint.complaintstatus=request.form.get('detail_complaintstatus')
    complaint.replystaff=request.form.get('detail_replystaff')
    complaint.complaintsolvetime=datetime.strptime(request.form.get('detail_complaintsolvetime').strip(),"%Y-%m-%d")
    db.session.add(complaint)
    db.session.commit()
    return redirect(url_for('community.complaint'))
@community.route('/complaint/owner',methods=['GET','POST'])
def complaint_owner():
    query = Complaint.query.filter_by(house_houseid=current_user.house_houseid)
    return render_template('community/complaint_owner.html',query=query)
