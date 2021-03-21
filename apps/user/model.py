# ORM类 ----> 表
# 类对象 ---->表中的记录
from datetime import datetime
from ext import db

# create table user(id int primarykey auto_increment,username varchar(20) not null,..)
class User(db.Model):
    # db.Column(类型，约束)  映射表中的列
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    isdelete = db.Column(db.Boolean, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    def __str__(self):
        return self.username
