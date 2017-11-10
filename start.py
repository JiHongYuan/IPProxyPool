# coding:utf-8
import multiprocessing
from SpidersManage import *
from ProxyService.ProxyService import startService

manage = SpidersManage()

s1 = multiprocessing.Process(target=manage.startDownloader)
s2 = multiprocessing.Process(target=manage.startValidate)
s3 = multiprocessing.Process(target=startService)

s2.start()
s3.start()
