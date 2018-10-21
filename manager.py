"""
项目的初始化配置信息:
项目的初始化配置信息:

1.数据库配置

2.redis配置

3.csrf配置,对'POST', 'PUT', 'PATCH', 'DELETE'请求方式做保护

4.session配置,为了后续登陆保持,做铺垫

5.日志信息配置

6.数据库迁移配置

"""""
from datetime import datetime,timedelta
import random

from info import create_app,db,models #导入目的,只是为了让当前项目知道有该文件的存在
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

#调用业务模块获取app
from info.models import User

app = create_app("develop")

#创建Manager对象,关联app
manager = Manager(app)

#使用 Migrate,关联app,db
Migrate(app,db)

#给manager添加操作命令
manager.add_command("db",MigrateCommand)

#创建管理员方法
#@manager.option 装饰方法,可以通过命令行的方式调用
#参数1: 表示传递的名称   参数2: 是参数名称的解释  参数3: 传递到形式参数的变量
@manager.option('-p', '--password', dest='password')
@manager.option('-u', '--username', dest='username')
def create_superuser(username,password):

    #1.创建管理员对象
    admin = User()

    #2.设置属性
    admin.nick_name = username
    admin.password = password
    admin.mobile = username
    admin.is_admin = True

    #3.保存管理员到数据库
    try:
        db.session.add(admin)
        db.session.commit()
    except Exception as e:
        return "注册失败"

    return "注册成功"

#添加测试用户
@manager.option('-t', '--test', dest='test')
def add_test_user(test):

    # 用户容器
    user_list = []

    for i in range(0,1000):
        # 创建用户
        user = User()
        # 设置属性
        user.nick_name = "老王%d"%i
        user.mobile = "138%08d"%i
        user.password_hash = "pbkdf2:sha256:50000$OfJMHM9l$a45e1cb75b5c010ddc329af10837637b2af93bf5fae510a4ec6a2f8377fdce66"

        # 设置随机,设置最后登陆时间, 在31天内的随机登陆时间
        user.last_login = datetime.now() - timedelta(seconds=random.randint(0,3600*24*31))

        # 添加用户到容器中
        user_list.append(user)

    #添加到数据库
    try:
        db.session.add_all(user_list)
        db.session.commit()
    except Exception as e:
        return "添加失败"

    return "添加成功"



if __name__ == '__main__':
    manager.run()