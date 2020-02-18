# -*- coding: utf-8 -*-
# Time: 2020-02-18 10:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_steam_id.py

#get your friends id
import requests,random
from http_conf import *
from query_all import query_list_from_list

__steam_session__ = "https://steamcommunity.com/search/users/"
__steam_search__ = "https://steamcommunity.com/search/SearchCommunityAjax?text={}&filter=users&\
sessionid={}&steamid_user=false&page=1"

"""
因为用户名重复问题导致用户数量过多，只保留第一页数据，请尽量输入详细的用户名
"""
def search(word):
    try:
        one_useragent = choose_agent()
        headers = plu_headers
        headers["User-Agent"] = one_useragent
        url = __steam_session__
        session = requests.session()
        req1 = session.get(url,headers=headers)
        req2 = session.get(__steam_search__.format(word,req1.cookies["sessionid"]),headers=headers)

        userlist = query_list_from_list(req2.json())
        return userlist

    except Exception as e:
        print("err in search\n",e.args)

def choose_agent():
    a = random.choice(user_agent)
    return a
