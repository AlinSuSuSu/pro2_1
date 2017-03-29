from flask import url_for,render_template,request,redirect
from app import db
from app.models import Repairation
from app.community import community
import json

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

@community.route('/repairation/detail/<string:repairationid>',methods=['GET','POST'])
def repairation_detail(repairationid):
    query=Repairation.query.filter_by(repairationid=repairation)
    return render_template('community/repairation_detail.html',query=query)

@community.route('/safety',methods=['GET','POST'])
def safety():
    return render_template('community/safety.html')

@community.route('/plant',methods=['GET','POST'])
def plant():
    return render_template('community/plant.html')

@community.route('/complaint',methods=['GET','POST'])
def complaint():
    return render_template('community/complaint.html')
