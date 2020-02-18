# -*- coding: utf-8 -*-
# Time: 2020-02-18 10:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: server_redis.py

#connect to redis
#使用redis保存一分钟内的缓存信息
import redis

host = "127.0.0.1"
port = 6379
pool = redis.ConnectionPool(host=host, port=port)
redis = redis.Redis(connection_pool=pool)

#如果你有密码，请使用
# password = ""
# pool = redis.ConnectionPool(host=host, port=port)
# redis = redis.Redis(connection_pool=pool,password=password)

def save_to_redis(status,px=None):
    redis.set(name="steam_status",value=status,px=px)

def test_redis():
    print(redis.get(name="steam_status").decode("utf-8"))


