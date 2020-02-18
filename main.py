#! /usr/bin/env/ python
# -*- coding: utf-8 -*-
# Time: 2020-02-18 10:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: main.py

#watch dog for steamid
#use this to run on a server
import schedule,time
from check_stats import check
import sys
from server_redis import save_to_redis

url = "" #url为必填项，你也可以将url改为name=xxx，系统会自动抓取名称匹配的第一个结果
def run():
    status = ""
    r = check(url=url)
    if r:
        status = "online"
    elif not r:
        status = "offline"
    else:
        return False
    save_to_redis(status=status)


schedule.every(5).minutes.do(run)
"""
默认每5分钟刷新一次数据
check函数返回值表示当前用户的状态True为在线，False为离线，error即爬取失败
参考schedule可以设置不同的时间频率
比如every(5).minutes,every(5).seconds,every(5).days
你也许会使用到redis缓存来更新数据，参考server-redis
"""

if __name__ == '__main__':
    #schedule
    # try:
    #     input = sys.argv[1]
    #     status = check(name=input)
    #     if status:
    #         print("在线")
    #     elif not status:
    #         print("离线")
    #     else:
    #         print("检查输出的用户或地址")
    # except:
    #     print("请输入参数")
    while True:
        schedule.run_pending()
        time.sleep(10)