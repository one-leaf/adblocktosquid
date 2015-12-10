# adblocktosquid
adblock rules to squid url_regex  rules

本程序将ADBLockPlus的规则转为SQUID的规则

数据来源：   https://easylist.adblockplus.org/en/

下载的地址： https://easylist-downloads.adblockplus.org/easylist.txt

           https://easylist-downloads.adblockplus.org/easylistchina.txt

SQUID 设置：

   acl adblock url_regex "/etc/squid/adblock.acl"

   http_access deny adblock
   
运行：

   sudo python adblock2squid.py > /etc/squid/adblock.acl
