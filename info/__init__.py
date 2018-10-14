from flask import Flask,session
from flask_session import Session #指定session存储位置
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf import CSRFProtect
from config import config_dict

def create_app(config_name):
    app = Flask(__name__)

    #根据传入的config_name,取出对应的运行环境
    config = config_dict.get(config_name)

    #加载配置类到app
    app.config.from_object(config)

    # 创建SQLAlchemy对象,关联app
    db = SQLAlchemy(app)

    # 创建redis对象
    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

    # 使用CSRFProtect,对app做请求保护
    CSRFProtect(app)

    # 使用Session,关联app,指定存储位置
    Session(app)

    return app