from . import db
from flask_login import UserMixin
from datetime import datetime


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
    users=db.relationship('User',backref='role',lazy='dynamic')

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
    __tablename__ = 'users'
    Staff_id = db.Column(db.Integer,primary_key=True)#员工编号
    staffname = db.Column(db.String(64),unique=True,index=True)#员工姓名
    age= db.Column(db.Integer)#年龄
    password_hash =db.Column(db.String(128))#密码
    last_seen = db.Column(db.DateTime(),default=datetime.utcnow)#上次登录
    gender = db.Column(db.Boolean(),Default=True)#性别
    glossary = db.Column(db.Integer)#薪资
    phone = db.Column(db.String(11),unique=True)#联系方式
    idcard = db.Column(db.String(18),unique=True)#身份证号
    job = db.Column(db.String(18))#工种

    role_id = db.Column(db.String(64))#角色