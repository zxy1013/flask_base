import hashlib
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_, and_, not_

from apps.user.model import User
from ext import db

# 创建蓝图
user_bp = Blueprint('user', __name__)

# 注册
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 注册用户
            # 1. 找到模型类并创建对象
            user = User( )
            # 2. 给对象的属性赋值
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest( )
            user.phone = phone
            # 添加并提交
            # 3.将user对象添加到session中（类似缓存）
            db.session.add(user)
            # 4.提交数据
            db.session.commit( )
            return redirect(url_for('user.user_center'))
        else:
            return '两次密码不一致！'
    return render_template('user/register.html')

# 主页面
@user_bp.route('/')
def user_center():
    # 查询数据库中的数据
    users = User.query.filter(User.isdelete == False).all( )  # 查询所有 select * from user;
    return render_template('user/center.html', users=users)

# 登录
@user_bp.route('/login', methods=[ 'GET', 'POST' ])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest( )
        # 查询  select * from user where username='xxxx';
        # user_list = User.query.filter_by(username=username)
        user_list = User.query.filter(and_(User.isdelete == False),User.username==username)
        for u in user_list:
            # 此时的u表示的就是用户对象
            if u.password == new_password:
                return '用户登录成功！'
        else:
            return render_template('user/login.html', msg='用户名或者密码有误！')
    return render_template('user/login.html')

# 检索
@user_bp.route('/search')
def search():
    keyword = request.args.get('search')  # 用户名或手机号
    # 多条件查询
    user_list = User.query.filter(and_(or_(User.username.contains(keyword),User.phone.contains(keyword))),User.isdelete == False).all()
    return render_template('user/center.html', users=user_list)

# 删除
@user_bp.route('/delete')
def delete():
    # 获取id
    id = request.args.get('id')

    # 获取该id的用户
    user = User.query.get(id)
    # 逻辑删除：
    user.isdelete = True
    # 提交
    db.session.commit()

    # # 物理删除 从数据库中删除
    # user = User.query.get(id)
    # # 将对象放到缓存准备删除
    # db.session.delete(user)
    # # 提交删除
    # db.session.commit()

    return redirect(url_for('user.user_center'))

# 用户信息更新
@user_bp.route('/update', endpoint='update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')
        # 找用户
        user = User.query.get(id)
        # 改用户信息
        user.phone = phone
        user.username = username
        # 提交
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)

# 查找函数
@user_bp.route('/test')
def test():
    # url:http://127.0.0.1:5000/test?username=2001121***

    # 查询所有 select * from user;
    users = User.query.all( )  # [<User 1>, <User 2>]

    # 模型类.query.filter_by(字段名 = 值)
    # select * from user where username='xxxx';
    username = request.args.get('username')
    user_list = User.query.filter_by(username=username)
    # for i in user_list:
    #     print(i.username)
    user = User.query.filter_by(username=username).all( ) # [<User 1>, <User 2>] 列表 后可以用切片
    # select * from user where 字段=值 limit(1)；
    user = User.query.filter_by(username=username).first( ) # 2001121*** 对象

    # 模型类.query.filter(模型名.字段名 == 值)
    user = User.query.get(1)  # 根据主键查询用户使用get（主键值）返回值是一个用户对象 2001121***
    user = User.query.filter(User.username == '2001121***').all() # [<User 1>, <User 2>] 后可以用切片
    user = User.query.filter(User.username == '20011210338').first() # 20011210338

    # select * from user where username like '%z';
    user = User.query.filter(User.username.endswith('8')).all( ) # [<User 1>, <User 2>]
    # select * from user where username like 'z%';
    user= User.query.filter(User.username.like('2%')).all( ) # [<User 1>, <User 2>]
    user= User.query.filter(User.username.startswith('2')).all( ) # [<User 1>, <User 2>]
    # select * from user where username like '%z%';
    user= User.query.filter(User.username.contains('1')).all( ) # [<User 1>, <User 2>]

    # 多条件查询
    user_list = User.query.filter(or_(User.username.like('1%'), User.username.contains('4'))).all()
    # select * from user where username like '1%' or username like '%4%';
    # __gt__,__lt__,__ge__(>=),__le__(<=) -----> 通常应用在范围（整型，日期）也可以直接使用 >  <  >=  <=  !=
    user_list = User.query.filter(and_(User.username.contains('2'), User.rdatetime.__gt__('2021-03-21 20:26:22'))).all()
    user_list = User.query.filter(and_(User.username.contains('2'), User.rdatetime > '2021-03-21 20:26:22')).all()
    user_list = User.query.filter(not_(User.username.contains('i'))).all()
    # select * from user where age in [17,18,20,22];
    user_list = User.query.filter(User.phone.in_(['12345678900','75964823657'])).all()

    # 排列
    user_list = User.query.filter(User.username.contains('2')).order_by(-User.rdatetime).all() # 负排列
    user_list = User.query.order_by(-User.id).all() # 负排列 [<User 4>, <User 3>, <User 1>]

    # limit的使用 + offset
    user_list = User.query.limit(2).all() # 显示前两个
    user_list = User.query.offset(1).limit(2).all( ) # 取出前一个后显示前两个
    return 'test'


