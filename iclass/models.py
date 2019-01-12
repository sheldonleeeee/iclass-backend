from datetime import datetime

from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class Permission:
    Student = 1
    Teacher = 2
    ADMIN = 16


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(64), primary_key=True, doc="学号，员工编号")
    role = db.Column(db.String(64), unique=True, index=True, doc="学生：1，老师：2")
    role_id = db.Column(db.Integer, doc='roles.id')
    username = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


class ClassRoom(db.Model):
    __tablename__ = 'class_room'
    id = db.Column(db.Integer, primary_key=True)
    floor = db.Column(db.Integer, doc="几号楼")
    college = db.Column(db.String(64), doc="哪个学院")
    classroom_number = db.Column(db.String(20), doc="教室号")


class ApplicationInfo(db.Model):
    __tablename__ = 'application_info'
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(64), primary_key=True, doc="申请人学号、员工号")
    approver = db.Column(db.String(64), primary_key=True, doc="审批人学号、员工号")
    floor = db.Column(db.Integer, doc="几号楼")
    application_timestamp = db.Column(db.DateTime, index=True, default=datetime.now())  # 日期
    period = db.Column(db.Integer, doc=" 时间段，上中下午")
    purpose = db.Column(db.TEXT, doc="申请 目的，用途")
    category = db.Column(db.String(20), doc="申请活动的类别")
    status = db.Column(db.SMALLINT, default=0, doc="状态，是否处理;审批通过，拒绝等")
    college = db.Column(db.String(64), doc="哪个学院")
    classroom_number = db.Column(db.String(20), doc="教室号")
    update_time = db.Column(db.DateTime, index=True, default=datetime.now(), doc="日期")
    create_time = db.Column(db.DateTime, index=True, default=datetime.now(), doc="日期")
