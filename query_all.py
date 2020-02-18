# -*- coding: utf-8 -*-
# Time: 2020-02-18 10:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: query_all.py

#爬虫部分
from pyquery import PyQuery as pq
import json
import html

__pattern1__ = ".search_row .searchPersonaInfo .searchPersonaName"
__pattern2__ = ".responsive_status_info .profile_in_game_header"

def query_list_from_list(req):
    try:
        if(req):
            doc = pq(html.unescape(req["html"]))
            list = doc(__pattern1__).items()
            userlist = []
            for i in list:
                scheme = "用户名：{} 主页：{}\n"
                js = {'username': i.text(),'address': i.attr("href")}
                userlist.append(js)
                print(scheme.format(i.text(),i.attr("href")))
            print("注意：请务必输入准确的用户地址，否则会自动爬取第一个结果\n")
            return userlist

    except Exception as e:
        print("err in query\n",e.args)

def query_status(res):
    try:
        if(res):
            doc = pq(res)
            stats = doc(__pattern2__).text()
            if stats == "Currently Offline" or stats == "当前离线":
                return False
            elif stats == "Currently Online" or stats == "当前在线":
                return True
            else:
                return "error"
        else:
            print("没有响应的页面")
    except Exception as e:
        print("err in query\n",e.args)