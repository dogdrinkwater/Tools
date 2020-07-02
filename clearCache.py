# -*- coding:utf-8 -*-
from rediscluster import RedisCluster
import sys


class clearRedis:
    redis_nodes = [{'host': '172.16.251.202', 'port': 7000},
                   {'host': '172.16.251.202', 'port': 7001},
                   {'host': '172.16.251.202', 'port': 7002},
                   {'host': '172.16.251.202', 'port': 7003},
                   {'host': '172.16.251.202', 'port': 7004},
                   ]
    @staticmethod
    def clear_with_key(keystr):


        try:
            redisconn = RedisCluster(startup_nodes=clearRedis.redis_nodes)
            list_keys = redisconn.keys(keystr)
            for key in list_keys:
                redisconn.delete(key)
                print('缓存已清除！')

        except:
            print("Connect Error!")
            sys.exit(1)

    def clear_userGroup(userId):
        key = "UIC:USER_GROUP:*:%s*" % userId
        clearRedis.clear_with_key(key)

    def clear_user(userId):
        key = 'UIC:USER:UIC_USER_BY_ID:%s' % userId
        clearRedis.clear_with_key(key)
