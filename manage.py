import os
from app import create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from app.models import Staff,Role,Reimbursement,Holiday
app = create_app(os.getenv("FLASK_CONFIG") or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app = app, db = db,Staff=Staff,Role=Role,Reimbursement=Reimbursement,Holiday=Holiday)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def deploy():
    from flask_migrate import upgrade
    from app.models import Role, Staff
    # 把数据库迁移到最新修订版本
    upgrade()
    # 创建用户角色
    Role.insert_roles()

if __name__ == '__main__':
    manager.run()#script扩展下，服务器使用manager.run()启动，启动后能够解析命令行