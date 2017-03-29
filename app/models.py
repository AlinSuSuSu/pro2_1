from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
import random
#加载用户的回调函数
@login_manager.user_loader
def load_user(staff_staffid):
    return Staff.query.get(int(staff_staffid))

class Permission:
    ADMINISTRATOR=0x80
    READ=0x01
    ADD=0x02
    MODIFY=0x03
    DELETE=0x04
    DISTRIBUTE=0x05

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    default=db.Column(db.Boolean,default=False,index=True)
    permissions = db.Column(db.Integer)
    staff=db.relationship('Staff',backref='role',lazy='dynamic')

    #创建角色
    @staticmethod
    def insert_roles():
        roles = {
            'User':(Permission.READ,True),
            'Moderator':(Permission.READ|
                         Permission.DELETE|
                         Permission.MODIFY|
                         Permission.ADD,False),
            'Administrator':(0xff,False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name

class Staff(UserMixin, db.Model):
    __tablename__ = 'staffs'
    staffid = db.Column(db.String(64),primary_key=True,index=True)#员工编号
    staffname = db.Column(db.String(64),unique=True,index=True)#员工姓名
    age= db.Column(db.Integer)#年龄
    password_hash =db.Column(db.String(128))#密码散列
    entertime = db.Column(db.DateTime(),default=datetime.utcnow)#上次登录
    gender = db.Column(db.String(4))#性别
    salary = db.Column(db.Integer)#薪资
    phone = db.Column(db.String(11),unique=True)#联系方式
    idcard = db.Column(db.String(18),unique=True)#身份证号
    job = db.Column(db.String(18))#工种
    role_id = db.Column(db.String(64),db.ForeignKey('roles.id'))#角色
    holiday_holidayid = db.relationship('Holiday', backref='staff', lazy='dynamic')
    reimbursement_reimbursementid=db.relationship('Reimbursement',backref='staff',lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
         return check_password_hash(self.password_hash, password)
    '''
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
'''
    #定义默认角色
    def __init__(self, **kwargs):
        super(Staff, self).__init__(**kwargs)
        if self.role is None:
            if self.staffname == 'admin':
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    #检查用户是否有指定的权限
    def can(self,permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions
    def is_administrator(self):
        return self.can(Permission.ADMINISTRATOR)

    # 刷新用户的最后访问时间,每次用户请求时都要调用ping()方法。
    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

class Holiday(UserMixin, db.Model):
    __tablename__='holidays'
    holidayid=db.Column(db.String(64),primary_key=True,index=True)#请假编号
    holidayreason=db.Column(db.String(300))#请假原因
    holidaytype=db.Column(db.String(10))#请假类型
    holidaytime=db.Column(db.String(50))#请假时间
    staff_phone=db.Column(db.String(11))#角色
    staff_staffid=db.Column(db.String(64),db.ForeignKey('staffs.staffid'))#角色


class Reimbursement(UserMixin,db.Model):
    __tablename__='reimbursements'
    reimbursementid=db.Column(db.String(64),primary_key=True,index=True)
    reimbursementtype=db.Column(db.String(64))
    reimbursementitem=db.Column(db.String(128))
    reimbursementcost=db.Column(db.String(64))
    reimbursementtime=db.Column(db.String(64),default=datetime.utcnow())
    staff_staffid=db.Column(db.String,db.ForeignKey('staffs.staffid'))



class Owner(UserMixin,db.Model):
    __tablename__='owners'
    house_houseid=db.Column(db.String(64),db.ForeignKey('houses.houseid'),primary_key=True,index=True)
    ownername=db.Column(db.String(64))
    ownerphone=db.Column(db.String(11))
    owneridcard=db.Column(db.String(20))
    owneryears=db.Column(db.String(20))
    ownerstatus=db.Column(db.String(20))
    ownerdate=db.Column(db.String(20))

class House(UserMixin,db.Model):
    __tablename__='houses'
    houseid=db.Column(db.String(64),primary_key=True,index=True)
    housestatus=db.Column(db.String(10))
    housetype=db.Column(db.String(64))
    housespace=db.Column(db.String(64))
    housecommunity=db.Column(db.String(64))
    houseremark=db.Column(db.String(64))
    houseaddress=db.Column(db.String(64))
    owner_ownername=db.Column(db.String(64))

class Repairation(UserMixin,db.Model):
    __tablename__ = 'repairations'
    house_houseid = db.Column(db.String(64),db.ForeignKey('houses.houseid'),index=True)
    owner_ownername=db.Column(db.String(64))
    repairationid = db.Column(db.String(64),primary_key=True,index=True)
    repairationcontent=db.Column(db.String(128))
    repairationestimatedcost=db.Column(db.String(64))#预计费用
    repairationactualcost=db.Column(db.String(64))#实际费用
    repairationresperson=db.Column(db.String(64))#负责人
    repairationresphone=db.Column(db.String(64))#负责人电话
    repairationsupervisitor=db.Column(db.String(64))#监督人，从志愿中选
    repairationtime=db.Column(db.String(64))#报修时间
    repairationcomptime=db.Column(db.String(64))#竣工时间
    repairationcheck=db.Column(db.String(4),default='否')#是否审核，默认未审核


class Waterfee(UserMixin,db.Model):
    __tablename__='waterfees'
    house_houseid = db.Column(db.String(64),db.ForeignKey('houses.houseid'),primary_key=True,index=True)
    owner_ownername=db.Column(db.String(64))
    startdegree=db.Column(db.String(16))#月初度数
    enddegree=db.Column(db.String(16))#月末度数
    priceperdegree=db.Column(db.String(8))#每度价格
    totalprice=db.Column(db.String(16))
    item=db.Column(db.String(8),default='水费')
    pay=db.Column(db.String(4),default='否')#是否缴纳


    @property
    def totalprice(self,totalprice):
        self.totalprice=(self.enddegree-self.startdegree)*self.priceperdegree



