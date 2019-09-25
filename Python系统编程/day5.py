#协程
#yield实现
# import time
# arr = []
# def LJ(gen):
#     while True:
#         if len(arr)<=0:
#             for i in range(5):
#                 time.sleep(1)
#                 arr.append(1)
#                 print("雷军生产了一台小米MIX Alpha，总共生产了%s台"%len(arr))
#         elif len(arr) >= 5:
#             #调用生成器
#             for i in range(5):
#                 next(gen)
# def DMZ():
#     while True:
#         time.sleep(1)
#         arr.pop()
#         print("董明珠砸了一台小米MIX Alpha，剩下%s台"%len(arr))
#         yield
# LJ(gen=DMZ())

"""
额外补充
生成器中 send()  next()
"""
#greenlet实现协程
# import time
# from greenlet import greenlet
# arr = []
# def LJ():
#     while True:
#         for i in range(5):
#             time.sleep(1)
#             arr.append(1)
#             print("雷军生产了一台小米MIX Alpha，总共生产了%s台"%len(arr))
#         f2.switch()
# def DMZ():
#     while True:
#         for i in range(5):
#             time.sleep(1)
#             arr.pop()
#             print("董明珠砸了一台小米MIX Alpha，剩下%s台"%len(arr))
#         f1.switch()
#
#
# f1 = greenlet(LJ)
# f2 = greenlet(DMZ)
# f1.switch()

"""
gevent 方式实现协程
"""

# import gevent
# def fun1():
#     print("我")
#     gevent.sleep(1)
#     print("帅")
# def fun2():
#     print("好")
#     gevent.sleep(2)
#     print("呀")
#
# f1 = gevent.spawn(fun1)
# f2 = gevent.spawn(fun2)
# gevent.joinall([f1,f2])


#猴子补丁
# import gevent
# import requests
# import lxml.etree as etree
# from gevent import monkey
#
# monkey.patch_all()
#
# urls = ['https://movie.douban.com/top250?start=%s'% i for i in range(0,226,25)]
#
# def getCon(url):
#     con = requests.get(url)
#     htmlObj = etree.HTML(con.text)
#     title = htmlObj.xpath('//span[@class="title"][1]/text()')
#     print(title)
# spawns = [gevent.spawn(getCon,url=url) for url in urls]
#
# gevent.joinall(spawns)

"""
async 关键字 把函数转换成一个等待对象
"""
import asyncio
async def fun1():
    print("Hello")
    await asyncio.sleep(1)
    print("Word!")
asyncio.run(fun1())
