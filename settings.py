# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/3/12 15:27
# @ File:settings.py

# 公共环境
class Config:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    # 配置数据库的连接路径 数据库+驱动+用户名+密码+@ip地址+端口号+数据库名
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zxy19981013@127.0.0.1:3306/fwbzz'
    # 配置数据库的不追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 开发环境
class DevelopmentConfig(Config):
    ENV = 'development'

# production环境
class ProductionConfig(Config):
    ENV = 'production'
    DDEBUG = False
