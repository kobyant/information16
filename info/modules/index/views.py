from info import redis_store
from . import index_blu
from flask import render_template,current_app

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

    return render_template("news/index.html")

#处理网站logo
#每个浏览器在访问服务器的时候,会自动向该服务器发送GET请求,地址是:/favicon.ico
#获取静态文件夹资源: current_app.send_static_file("文件路径"),会自动寻找static静态文件夹的资源
@index_blu.route('/favicon.ico')
def web_logo():

    return current_app.send_static_file("news/favicon.ico")