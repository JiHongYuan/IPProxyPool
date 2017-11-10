# -*- coding:utf-8 -*-
# 参数配置
MAX = 100

# 网络配置
TIMEOUT = 3
MAX_THREADS = 5
SLEEP_TIME = 3

# 测试代理网站
URL_HTTPS_TEXT = "https://httpbin.org/get"
URL_HTTP_TEXT  = "http://httpbin.org/get"

# 数据库配置
HOST = "localhost"
PORT = 3306
USER = "root"
PASSWD = "123456"
DB = "proxies_db"

# 数据表语句
VTABLE_NAME = "verification"
TABLE_NAME = "proxies"
CREATE_TABLE = """
    create table %s(
      _id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
      type VARCHAR(8),
      proxy VARCHAR(30)
    )
"""
SHOW_TABLES = "show tables"
DROP_TABLE  = "DROP TABLE %s"
SELECT = "select *from %s"
