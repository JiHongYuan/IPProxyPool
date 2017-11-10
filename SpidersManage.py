# -*- coding:utf-8 -*-
from webRules import parserList
from spiders.HtmlDownloader import *
from spiders.HtmlPraser import *
from db.sqlHelper import *
from spiders.ProxyValidate import *


class SpidersManage(object):
    def __init__(self):
        self.downloader = HTML_Downloader()
        self.parser = HtmlParser()
        self.sqlHelper = sqlHelper()
        self.pValidate = ProxyValidate()

        self.downloaderFlag = True
        self.validateFlag = True

    def startDownloader(self):
        while self.downloaderFlag:
            url_lists = []
            uStart_lists = []
            uEnd_lists = []
            # 解析方式
            type_lists = []
            # 解析规则
            rules_lists = []

            for item in parserList:
                url_lists.append(item["url"])
                uStart_lists.append(item["url_start"])
                uEnd_lists.append(item["url_end"])
                type_lists.append(item["type"])
                rules_lists.append(item["rules"])

            for i in range(len(url_lists)):
                for j in range(uStart_lists[i], uEnd_lists[i]):
                    url = url_lists[i] + str(j)
                    html = self.downloader.download(url)
                    if type_lists[i] == 'xpath':
                        proxies = self.parser.xPathParser(html, rules_lists[i])
                        try:
                            self.sqlHelper.insert(config.VTABLE_NAME, proxies)
                        except:
                            pass
                        # print proxies

            self.sqlHelper.truncate()

    def startValidate(self):
        while self.validateFlag:

            select_sql = ""
            sql = ""
            type = ""
            data = ""
            states = 1
            l = len(list(self.sqlHelper.select("select *from proxies")))
            if l < config.MAX:
                select_sql = "select type,proxy from " + config.VTABLE_NAME + " order by _id desc limit 0,5;"
                type = "i"
                states = 1
            else:
                type = "d"
                select_sql = "select type,proxy from " + config.TABLE_NAME
                states = 2
            data = self.sqlHelper.select(select_sql)
            s = self.pValidate.validate(list(data),states)
            self.sqlHelper.executeSQL(config.TABLE_NAME, type, s)
            k = []
            for i in data:
                k.append(i[1])
            try:
                self.sqlHelper.delete("delete from verification where proxy=%s ",k)
            except:
                pass