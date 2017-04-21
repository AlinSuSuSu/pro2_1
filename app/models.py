from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
import random
#加载用户的回调函数
@login_manager.user_loader
def load_user(user_username):
    return User.query.get(user_username)

class Permission:
    HOUSEOWNER=0x02
    ADMIN=0x01


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    default=db.Column(db.Boolean,default=False,index=True)
    permissions = db.Column(db.Integer)
    user = db.relationship('User', backref='role', lazy='dynamic')

    #创建角色
    @staticmethod
    def insert_roles():
        roles = {
            'Houseowner': (Permission.HOUSEOWNER, True),
            'Admin':(Permission.ADMIN,False)
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

class User(UserMixin,db.Model):
    __tablename__='users'
    house_houseid=db.Column(db.String(10),primary_key=True)#房产编号
    username=db.Column(db.String(16),unique=True)#用户名，用于登录，业主初始用户名为房产编号
    password_hash=db.Column(db.String(128))#密码散列
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #定义默认角色
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.house_houseid == '000':
                self.role = Role.query.filter_by(permissions=0x01).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    #检查用户是否有指定的权限
    def can(self,permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions
    def is_administrator(self):
        return self.can(Permission.ADMIN)

    # 刷新用户的最后访问时间,每次用户请求时都要调用ping()方法。
    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

class Staff(UserMixin, db.Model):
    __tablename__ = 'staffs'
    staffid = db.Column(db.String(64),primary_key=True,index=True)#员工编号
    staffname = db.Column(db.String(64),unique=True,index=True)#员工姓名
    age= db.Column(db.Integer)#年龄
    gender = db.Column(db.String(4))#性别
    phone = db.Column(db.String(11),unique=True)#联系方式
    idcard = db.Column(db.String(18),unique=True)#身份证号
    job = db.Column(db.String(18))#工种
    enterdate=db.Column(db.Date)#入职时间

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

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = Owner(ownername=forgery_py.internet.user_name(False),
                      house_houseid=forgery_py.basic.text(length=10,digits=False),
                      ownerphone=forgery_py.address.phone(),
                      owneridcard=forgery_py.basic.text(length=18,digits=True),
                      owneryears=70,
                      ownerstatus='购买',
                      ownerdate=forgery_py.date.date(True))

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

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

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = House(owner_ownername=forgery_py.internet.user_name(False),
                      houseid=forgery_py.basic.text(length=10, digits=True),
                      housetype='二室二厅二卫一厨',
                      housespace=forgery_py.basic.text(at_least=2,at_most=4,digits=True),
                      housecommunity='天生小区',
                      houseremark='待售',
                      houseyears='70',
                      houseaddress=forgery_py.address.street_address(),
                      housestatus='闲置')

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

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

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = Patrol(patrolid=forgery_py.basic.text(length=10,digits=False),
                       eventtype=forgery_py.basic.text(at_most=16,at_least=2, digits=False),
                       solveperson=forgery_py.basic.text(at_most=16,at_least=2, digits=False),
                       personinvolved=forgery_py.basic.text(at_most=16,at_least=2, digits=False),
                       phoneinvolved=forgery_py.basic.text(at_most=16,at_least=2, digits=False),
                       eventresult=forgery_py.basic.text(at_most=32,at_least=2, digits=False),
                       eventtime=datetime.strptime('2017-01-01-12', "%Y-%m-%d-%H"),
                       eventdetail=forgery_py.basic.text(at_most=200,at_least=20, digits=False),
                       )
            u.totalprice = 200.00
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()



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
class Complaint(UserMixin,db.Model):
    __tablename__='complaints'
    complaintid=db.Column(db.String(10),primary_key=True,index=True)
    complainttime=db.Column(db.DateTime,nullable=False)
    house_houseid=db.Column(db.String(32),db.ForeignKey('houses.houseid'),nullable=False)
    complainttype=db.Column(db.String(32),nullable=False)
    complaintstatus=db.Column(db.String(16),nullable=False)
    complainttime=db.Column(db.DateTime,nullable=False)
    replystaff=db.Column(db.String(16),nullable=False)
    complaintdetail=db.Column(db.String(200),nullable=False)



class Waterfee(UserMixin,db.Model):
    __tablename__='waterfees'
    waterfeeid=db.Column(db.String(20),primary_key=True,index=True)
    house_houseid = db.Column(db.String(10))
    startdegree=db.Column(db.Float)#月初度数
    enddegree=db.Column(db.Float)#月末度数
    priceperdegree=db.Column(db.Float,default='1.0')#每度价格
    totalprice=db.Column(db.Float)
    item=db.Column(db.String(8),default='水费')
    startdate=db.Column(db.Date)
    enddate=db.Column(db.Date)
    pay=db.Column(db.String(4),default='否')#是否缴纳

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = Waterfee(waterfeeid=forgery_py.basic.text(length=10,digits=True),
                         house_houseid=forgery_py.basic.text(length=10, digits=True),
                         startdegree=10.0,
                         enddegree=20.0,
                         priceperdegree=1.0,
                         item='水费',
                         startdate=datetime.strptime('2017-01-01',"%Y-%m-%d"),
                         enddate=datetime.strptime('2017-02-01',"%Y-%m-%d"),
                         pay=random.choice(['是','否'])
                         )
            u.totalprice=200.00
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()



class Electricfee(UserMixin,db.Model):
    __tablename__='electricfees'
    electricfeeid=db.Column(db.String(10),primary_key=True,index=True)
    house_houseid = db.Column(db.String(10),db.ForeignKey('houses.houseid'),)
    startdegree=db.Column(db.Float)#月初度数
    enddegree=db.Column(db.Float)#月末度数
    priceperdegree=db.Column(db.Float,default='1.0')#每度价格
    totalprice=db.Column(db.Float)
    item=db.Column(db.String(8),default='电费')
    startdate=db.Column(db.Date)
    enddate=db.Column(db.Date)
    pay=db.Column(db.String(4),default='否')#是否缴纳

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = Electricfee(electricfeeid=forgery_py.basic.text(lenth=10,digits=True),
                         house_houseid=forgery_py.basic.text(length=10, digits=True),
                         startdegree=10.0,
                         enddegree=20.0,
                         priceperdegree=1.0,
                         item='电费',
                         startdate=datetime.strptime('2017-01-01',"%Y-%m-%d"),
                         enddate=datetime.strptime('2017-02-01',"%Y-%m-%d"),
                         pay=random.choice(['是','否'])
                         )
            u.totalprice=200.00
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
class Gasfee(UserMixin,db.Model):
    __tablename__='gasfees'
    gasfeeid=db.Column(db.String(10),primary_key=True,index=True)
    house_houseid = db.Column(db.String(10),db.ForeignKey('houses.houseid'),)
    startdegree=db.Column(db.Float)#月初度数
    enddegree=db.Column(db.Float)#月末度数
    priceperdegree=db.Column(db.Float,default='1.0')#每度价格
    totalprice=db.Column(db.Float)
    item=db.Column(db.String(8),default='燃气费')
    startdate=db.Column(db.Date)
    enddate=db.Column(db.Date)
    pay=db.Column(db.String(4),default='否')#是否缴纳

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = Gasfee(gasfeeid=forgery_py.basic.text(lenth=10,digits=True),
                         house_houseid=forgery_py.basic.text(length=10, digits=True),
                         startdegree=10.0,
                         enddegree=20.0,
                         priceperdegree=1.0,
                         item='燃气费',
                         startdate=datetime.strptime('2017-01-01',"%Y-%m-%d"),
                         enddate=datetime.strptime('2017-02-01',"%Y-%m-%d"),
                         pay=random.choice(['是','否'])
                         )
            u.totalprice=200.00
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
class Cleaningfee(UserMixin,db.Model):
    __tablename__='cleaningfees'
    cleaningfeeid=db.Column(db.String(10),primary_key=True,index=True)
    house_houseid = db.Column(db.String(10),db.ForeignKey('houses.houseid'),)
    priceperyear=db.Column(db.Float,default='20')#每度价格
    item=db.Column(db.String(8),default='卫生费')
    recordeyear=db.Column(db.String(8))
    pay=db.Column(db.String(4),default='否')#是否缴纳

    @staticmethod
    def generate_fake(count=50):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = Cleaningfee(cleaningfeeid=forgery_py.basic.text(lenth=10,digits=True),
                         house_houseid=forgery_py.basic.text(length=10, digits=True),
                         priceperdegree=20,
                         item='卫生费',
                         recordyear='2016',
                         pay=random.choice(['是','否'])
                         )
            u.totalprice=200.00
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()