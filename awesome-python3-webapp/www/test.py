#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午6:50
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : XXXXXX@gmail.com
# @Site    :

import orm,asyncio,functools
from models import User, Blog, Comment


# async def test(loop):
#     await orm.create_pool(loop,user='www-data', password='www-data', db='awesome')
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#     await u.save()
#
# async def find(loop):
#     await orm.create_pool(loop,user='www-data',password= "www-data",db='awesome')
#     rs = await User.findAll()
#     print('查找测试： %s' % rs)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([find(loop)]))
def log(func):
    # @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)
        return func()
    return wrapper

@log
def now():
    print('2018-08-23')

now()

# n = now()
# print(n.__name__)
# print(now.__name__)
# n()
