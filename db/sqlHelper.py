# -*- coding:utf-8 -*-
import re
import config
import MySQLdb

try:
    conn = MySQLdb.connect(
        host=config.HOST,
        port=config.PORT,
        user=config.USER,
        passwd=config.PASSWD,
        db=config.DB
    )
    cur = conn.cursor()
except Exception as e:
    print e


class sqlHelper(object):
    def __init__(self):

        # 数据库连接初始化


        # 检查数据库是否存在表
        cur.execute(config.SHOW_TABLES)
        list = re.findall(r"\(\'(.*?)\',\)", str(cur.fetchall()))
        if config.TABLE_NAME not in list:
            cur.execute(config.CREATE_TABLE % (config.TABLE_NAME))

        if config.VTABLE_NAME not in list:
            cur.execute(config.CREATE_TABLE % (config.VTABLE_NAME))

    def select(self, sql):
        c = cur.execute(sql)
        info = cur.fetchmany(c)

        return info

    def select_type(self, type):
        sql = "select *from %s where type = '%s'" % (
            config.TABLE_NAME,
            type
        )
        c = cur.execute(sql)

        info = cur.fetchmany(c)

        return info

    def insert(self, table, data):
        sql = "insert into " + table + "(type,proxy) VALUES (%s,%s)"
        cur.executemany(sql, data)
        conn.commit()

        pass

    def truncate(self):
        cur.execute("truncate table verification")
        pass

    def executeSQL(self, table, type, data):
        sql = ""
        if type == 'i':
            sql = "insert into " + table + "(type,proxy) VALUES (%s,%s)"

        elif type == "d":
            sql = "delete from proxies where proxy = %s"

        cur.executemany(sql, data)
        conn.commit()

    def update(self):
        conn.commit()
        pass

    def delete(self,sql,data):
        cur.executemany(sql, data)
        conn.commit()


    def destroy(self):
        conn.close()
        cur.close()
