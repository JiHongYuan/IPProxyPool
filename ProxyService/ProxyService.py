# coding:utf-8
import json
from db.sqlHelper import *
import web

sqlHelper = sqlHelper()


class http:
    def GET(self):
        sql = 'SELECT type,proxy FROM proxies WHERE type="http" ' \
              'AND _id >= (SELECT floor(RAND() * (SELECT MAX(_id) ' \
              'FROM proxies)))  ORDER BY _id LIMIT 5;'
        return json.dumps(sqlHelper.select(sql))



class https:
    def GET(self):
        sql = 'SELECT type,proxy FROM proxies WHERE type="https" ' \
              'AND _id >= (SELECT floor(RAND() * (SELECT MAX(_id)' \
              ' FROM proxies)))  ORDER BY _id LIMIT 5'';'
        return json.dumps(sqlHelper.select(sql))

urls = (
    "/http","http",
    "/https","https",
)
def startService():
    web.sys.argv.append("0.0.0.0:8081")
    app = web.application(urls, globals())
    app.run()