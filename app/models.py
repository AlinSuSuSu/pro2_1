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
    COMMONSTAFF=0x04
    HOUSEOWNER=0x02
    VISITOR=0x01


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
            'Visitor': (Permission.VISITOR, True),
            'Staff':(Permission.COMMONSTAFF|Permission.VISITOR,False),
            'Houseowner':(Permission.HOUSEOWNER|Permission.VISITOR,False),
            'Administrator':(Permission.VISITOR|Permission.COMMONSTAFF|Permission.HOUSEOWNER,False)
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
                self.role = Role.query.filter_by(permissions=0x07).first()
           # if self.role is None:
             #   self.role = Role.query.filter_by(permissions=0x05).first()

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
    house_houseid=db.Column(db.String(10),db.ForeignKey('houses.houseid'),primary_key=True,index=True)
    ownername=db.Column(db.String(16),nullable=False)
    ownerphone=db.Column(db.String(11),nullable=False,unique=True)
    owneridcard=db.Column(db.String(20),nullable=False,unique=True)
    owneryears=db.Column(db.String(4),nullable=False,default='70')
    ownerstatus=db.Column(db.String(16),nullable=False)
    ownerdate=db.Column(db.Date,nullable=False)#进户日期

class House(UserMixin,db.Model):
    __tablename__='houses'
    houseid=db.Column(db.String(10),primary_key=True,nullable=False)#房屋编号
    housestatus=db.Column(db.String(8),default='闲置')#房屋状态
    housetype=db.Column(db.String(20))#房型
    housespace=db.Column(db.String(10))#房屋面积
    housecommunity=db.Column(db.String(20))#小区名称
    houseremark=db.Column(db.String(64))#备注
    houseyears = db.Column(db.String(4),default='70')#房产年限
    houseaddress=db.Column(db.String(128))#具体地址
    owner_ownername=db.Column(db.String(16))#业主姓名

class Repairation(UserMixin,db.Model):
    __tablename__ = 'repairations'
    house_houseid = db.Column(db.String(10),db.ForeignKey('houses.houseid'),nullable=False,unique=True)
    owner_ownername=db.Column(db.String(16))
    repairationid = db.Column(db.String(16),primary_key=True,index=True)
    repairationcontent=db.Column(db.String(128))
    repairationestimatedcost=db.Column(db.String(8))#预计费用
    repairationactualcost=db.Column(db.String(8))#实际费用
    repairationresperson=db.Column(db.String(16))#负责人
    repairationresphone=db.Column(db.String(11))#负责人电话
    repairationsupervisitor=db.Column(db.String(16))#监督人，从志愿中选
    repairationtime=db.Column(db.Date)#
    # 报修时间
    repairationcomptime=db.Column(db.Date)#竣工时间
    repairationreplytime=db.Column(db.DateTime)#申请时间
    repairationcheck=db.Column(db.String(4),nullable=False,default='未审核')#进度，分为未审核，审核通过，审核失败，默认未审核


class Waterfee(UserMixin,db.Model):
    __tablename__='waterfees'
    house_houseid = db.Column(db.String(10),db.ForeignKey('houses.houseid'),primary_key=True,index=True)
    owner_ownername=db.Column(db.String(16))
    startdegree=db.Column(db.String(16))#月初度数
    enddegree=db.Column(db.String(16))#月末度数
    priceperdegree=db.Column(db.String(8),default='1')#每度价格
    totalprice=db.Column(db.String(16))
    item=db.Column(db.String(8),default='水费')
    pay=db.Column(db.String(4),default='否')#是否缴纳


    @property
    def totalprice(self,totalprice):
        self.totalprice=(self.enddegree-self.startdegree)*self.priceperdegree



class Patrol(UserMixin,db.Model):
    __tablename__='patrols'
    patrolid = db.Column(db.String(10),primary_key=True,index=True)
    eventtype = db.Column(db.String(32),nullable=False)
    eventtime = db.Column(db.DateTime,nullable=False)
    solveperson = db.Column(db.String(16),nullable=False)#处理人
    #solvephone = db.Column(db.String(16),nullable=False)#处理人电话
    personinvolved = db.Column(db.String(16),nullable=False)#当事人
    phoneinvolved = db.Column(db.String(16),nullable=False)#当事人电话
    eventresult = db.Column(db.String(32),nullable=False)#处理结果
    eventdetail = db.Column(db.String(200),nullable=False)#事件概要

class Infrastructure(UserMixin,db.Model):
    __tablename__='infrastructures'
    infrastructureid=db.Column(db.String(10),primary_key=True,index=True)
    infrastructuretype=db.Column(db.String(32),nullable=False)
    infrastructuretime=db.Column(db.Date,nullable=False)
    infrastructurearea=db.Column(db.String(32),nullable=False)
    resperson=db.Column(db.String(16),nullable=False)
    resphone=db.Column(db.String(16),nullable=False)
    supervisitor=db.Column(db.String(16),nullable=False)
    check=db.Column(db.String(8),nullable=False)
    detail=db.Column(db.String(200),nullable=False)
