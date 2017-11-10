# -*- coding: utf-8 -*-
from lxml import etree

class HtmlParser(object):

    def __init__(self):
        pass
        # [0] http
        # [1] ip
        # [2] post
        # self.array = [
        #     [],
        #     [],
        #     [],
        # ]
        # # proxies 列表
        # self.proxies = []

    # xpath解析
    def xPathParser(self,response,parsers={}):
        array = [
            [],
            [],
            [],
        ]
        # proxies 列表
        proxies = []

        root = etree.HTML(response)
        try:
            for i in range(len(parsers)):
                # parsers[0] 为http
                if i is None and i:
                    # 默认添加https
                   array[0].append('https')
                  # proxys[0].append('http')
                # 每一列添加数据*
                for item in root.xpath(parsers[i]):
                    array[i].append(str(item.text.lower()))

        except Exception as e:
            print "HtmlParser:",e

        # 二维数组 列项 拼接
        for i in range(len(array[0])):
            s = [
                    array[0][i],
                    array[0][i] +
                    "://" + array[1][i] +
                    ":"   + array[2][i]]

            proxies.append(s)

        return proxies


    def reParser(self,response,parser):
        pass