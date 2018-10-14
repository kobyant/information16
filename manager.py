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
from flask import Flask,session
from flask_session import Session #指定session存储位置
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf import CSRFProtect

app = Flask(__name__)

#设置配置信息
class Config(object):
    #调试模式
    DEBUG = True
    SECRET_KEY = "fjdkfjkdjfkd"

    #数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/information16"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 3600*24*2 #两天有效期,单位默认就是秒


app.config.from_object(Config)

#创建SQLAlchemy对象,关联app
db = SQLAlchemy(app)

#创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,decode_responses=True)

#使用CSRFProtect,对app做请求保护
CSRFProtect(app)

#使用Session,关联app,指定存储位置
Session(app)

@app.route('/')
def hello_world():

    #测试redis,存取数据
    redis_store.set("name","laowang")
    print(redis_store.get("name"))

    #测试session,存取数据
    session["age"] = "13"
    print(session.get("age"))

    return "helloworld100"

if __name__ == '__main__':
    app.run()