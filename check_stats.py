#! /usr/bin/env/ python
# -*- coding: utf-8 -*-
# Time: 2020-02-18 10:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: check_stats.py

#check status of your steam friends
from get_steam_id import search
from query_all import query_status
import requests,random
from http_conf import *


def check(name=None,url=None):
    try:
        user_agent = choose_agent()
        headers = {"User-Agent":user_agent}
        if url and name:
            res = requests.get(url,headers).text
            r =query_status(res)
            return r
        elif url and not name:
            res = requests.get(url,headers).text
            r = query_status(res)
            return r
        elif not url and name:
            result = search(name)[0]["address"]
            res = requests.get(result,headers).text
            r = query_status(res)
            return r
        else:
            print("使用方式：\n输入用户名<name={}>以匹配\n或输入准确地址<url={}>以爬取\n")
            return "input error"

    except Exception as e:
        print("err in check\n",e.args)


def choose_agent():
    a = random.choice(user_agent)
    return a
