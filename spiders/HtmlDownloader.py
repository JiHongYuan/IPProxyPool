# -*- coding: utf-8 -*-

import requests
import time
from requests import Response, ConnectionError

import config
import webRules

class HTML_Downloader(object):
    def __init__(self):
        pass

    def download(self,url):

        html = None
        try:
            response = requests.get(url,headers=webRules.get_header(),timeout=config.TIMEOUT)
            print 'Downloading<%s>%s'%(response.status_code,url)
            html = response.text
            time.sleep(6)
        except Exception as e:
            print e.message
            if hasattr(e,'Response.raise_for_status'):
                print '<%s>URL:%s\nError:%s'%(e.Response.raise_for_status,url,e)
            # 重试次数
            num_retries = 2

            if num_retries > 0:
                # 代理
                pass



        return html