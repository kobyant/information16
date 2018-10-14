from info import redis_store
from . import index_blu

@index_blu.route('/')
def hello_world():

    #测试redis,存取数据
    redis_store.set("name","laowang")
    print(redis_store.get("name"))

    #测试session,存取数据
    # session["age"] = "13"
    # print(session.get("age"))

    #使用loggin日志模块输出内容
    # logging.debug("调试信息1")
    # logging.info("详细信息1")
    # logging.warning("警告信息1")
    # logging.error("错误信息1")

    #上面的方式可以使用current_app输出,在控制台输出的时候有华丽分割线,写入到文件是一样的
    # current_app.logger.debug("调试信息2")
    # current_app.logger.info("详细信息2")
    # current_app.logger.warning("警告信息2")
    # current_app.logger.error("错误信息2")

    return "helloworld100"