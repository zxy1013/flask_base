from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from apps import create_app
from ext import db
from apps.user.model import User

app = create_app() # 程序启动的入口，在apps包里的init文件中
manager = Manager(app=app)

migrate  = Migrate(app=app,db=db) #
manager.add_command('db',MigrateCommand) # 对manager添加命令db，实现方式为MigrateCommand


@manager.command
def init():
    print('初始化')



if __name__ == '__main__':
    manager.run()