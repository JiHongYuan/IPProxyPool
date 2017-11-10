# -*- coding:utf-8 -*-
import threading
import requests
import time

import webRules
import config


class ProxyValidate(object):
    # proxy {
    #   "http":"http://192.168.1.1"
    #   "https":"http://192.168.1.1"
    # }
    def __init__(self):
        self.text_url = ""
        self.response = []
        self.states = 1
    def process_queue(self,proxies):
        try:
            proxy = proxies.pop()
        except IndexError:
            pass

        if proxy[0] == "http":
            self.text_url = config.URL_HTTP_TEXT
        elif proxy[0] == "https":
            self.text_url = config.URL_HTTPS_TEXT

        try:
            print proxy
            response = requests.get(self.text_url, proxies={proxy[0]:proxy[1]}, headers=webRules.get_header(),
                                    timeout=3)

            print response.text
            if self.states == 1:
                self.response.append(proxy)

        except Exception as e:
            #print e
            #print proxy
            if self.states == 2:
                self.response.append(proxy)



    def validate(self, proxies=[],states=1):
        self.states = states
        self.response = []
        threads = []
        while proxies:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)

            while len(threads) < config.MAX_THREADS and proxies:
                thread = threading.Thread(target=self.process_queue(proxies))
                thread.setDaemon(True)
                thread.start()
                threads.append(thread)

            time.sleep(config.SLEEP_TIME)

        return self.response
