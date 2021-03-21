from flask import Flask
import settings
from apps.user.view import user_bp

# 为app设置配置文件，此时使用蓝图分发路径
from ext import db


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    # app是一个核心对象，设置模板文件夹以及静态文件夹，路径为apps的上级目录hello_flask的的子目录
    app.config.from_object(settings.DevelopmentConfig)  # 加载配置改为类
    db.init_app(app) # 将db对象和app进行关联
    # 注册蓝图对象 需要手动注册蓝图，才会建立上url和视图函数的映射关系
    app.register_blueprint(user_bp)

    return app

