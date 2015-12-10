#!/usr/bin/env python
# -*- coding: utf-8; -*-
# # (c) free software, GPLv3
# Connect: oneleaf@gmail.com
'''
本程序将ADBLockPlus的规则转为SQUID的规则
数据来源：   https://easylist.adblockplus.org/en/
下载的地址： https://easylist-downloads.adblockplus.org/easylist.txt
           https://easylist-downloads.adblockplus.org/easylistchina.txt
SQUID 设置：
   acl adblock url_regex "/etc/squid/adblock.acl"
   http_access deny adblock
   
运行：
   sudo python adblock2squid.py > /etc/squid/adblock.acl
'''

import urllib2, re, os

def addrules(url):
    html = urllib2.urlopen(url,timeout=60).readlines()
    for line in html:
        line=line.strip()
        if line=='': continue
        if line.find('$')>=0: continue
        if line.find('#')>=0: continue
        if line.find('@@')>=0: continue
        if line.find('[]')>=0: continue
        if line.startswith('!'): continue
        if line.startswith('['): continue
        line=line.replace('.','\.')
        line=line.replace('^','.')
        line=line.replace('|http','http')
        line=line.replace('||','')
        line=line.replace('*','.*')
        line=line.replace('?','\?')
        line=line.replace('|','')
        print line

if __name__ == '__main__':
    addrules("https://easylist-downloads.adblockplus.org/easylistchina.txt")
    addrules("https://easylist-downloads.adblockplus.org/easylist.txt")
