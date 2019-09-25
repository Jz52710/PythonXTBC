from threading import Thread,active_count,current_thread,enumerate,main_thread,stack_size,Lock,RLock,Condition
import time,random
# print(active_count())#返回当前活动线程的数量
# print(current_thread())#返回当前的线程
# print(enumerate())#返回当前活动的线程
# print(main_thread())#返回主线程对象
# print(stack_size()) #返回创建线程时使用的栈的大小，如果指定size参数，则用来指定后续创建的线程使用的栈的大小，size必须为0（表示使用系统默认值）或大于32k的正整数。


# def task(num):
#     # time.sleep(random.randint(0,5))
#     time.sleep(3)
#     print(num)
# # start = time.time()
# arr = []
# for i in range(5):
#     t = Thread(target=task,args=(i,))
#     t.start()
#     arr.append(t)
#
# for i in arr:
#     i.join()

# end = time.time()
# print("总共用时%s"%(end-start))

# class Mytest(Thread):
#     def __init__(self):
#         super().__init__(self)
#         # self.name = ''
#     def run(self):
#         time.sleep(3)
#         print(self.name)
# t1 = Mytest()
# t1.run()

"""
Thread对象常用方法：
start() 运行线程
join(time)阻塞主进程time阻塞时间
name 线程的名字
ident 线程的标识
is_alice() 判断线程是否存活
daemon 是否为守护线程(守护线程：主线程不会等守护线程运行结束)
"""
# def task():
#     time.sleep(2)
#     print("task")
# t1 = Thread(target=task)
# t1.daemon = False
# # t1.daemon = True
# t1.start()
"""
gtoup 默认为None为扩展Thread保留
target 线程启动执行函数
args 是元组 是线程执行函数的参数
kwargs 是线程执行函数的参数
"""

# hg = []
#
# l1 = Condition()
# class Xm(Thread):
#     def __init__(self):
#         super(Xm,self).__init__()
#     def run(self):
#         l1.acquire()
#         while True:
#             time.sleep(2)
#             hg.append(1)
#             print("小明放了1个鱼丸，锅内有%s个"%(len(hg)))
#             if len(hg)>=5:
#                 l1.notify()
#                 l1.wait()
#
#
# class Xh(Thread):
#     def __init__(self):
#         super(Xh,self).__init__()
#     def run(self):
#         l1.acquire()
#         while True:
#             time.sleep(1)
#             hg.pop()
#             print("小红吃了1个鱼丸，锅内有%s个"%(len(hg)))
#             if len(hg)==0:
#                 l1.notify()
#                 l1.wait()
#
# p = Xm()
# p.start()
#
# p = Xh()
# p.start()

# from threading import RLock
#
# r = RLock()
# l = Lock()
# def test1():
#     r.acquire()
#     print('123')
#     r.release()
# def test2():
#     r.acquire()
#     print('test2')
#     r.release()
# t = Thread(target=test1)
# t.start()
# t2 = Thread(target=test2)
# t2.start()
#死锁
# l1 = Lock()
# l2 = Lock()
#
# def fun1():
#     l1.acquire()
#     print("fun1 run")
#     time.sleep(1)
#     l2.acquire()
#     print("fun1 end")
#     l1.release()
#     l2.acquire()
# def fun2():
#     l2.acquire()
#     print("fun2 run")
#     l1.acquire()
#     print("fun2 end")
#     l2.release()
#     l1.release()
#
# t1 = Thread(target=fun1)
# t1.start()
#
# t2 = Thread(target=fun2)
# t2.start()

#锁的上下文使用方法
# arr = []
# l = Lock()
# def fun():
#     time.sleep(1)
#     with l:#上锁，自动解锁
#         arr.append(random.randint(0,10))
#         print(arr)
#
# for i in range(5):
#     t = Thread(target=fun)
#     t.start()

"""
条件锁
"""
# from threading import Condition
# import time
# con = Condition()
#
# arr = []
#
# class XM(Thread):
#     def __init__(self):
#         super(XM,self).__init__()
#     def run(self):
#         with con:
#             while True:
#                 time.sleep(2)
#                 arr.append(1)
#                 length = len(arr)
#                 print("小明添加了1个鱼丸,锅内还有%s个鱼丸"%length)
#                 if length>=5:
#                     con.notify()
#                     con.wait()
#
# class XH(Thread):
#     def __init__(self):
#         super(XH,self).__init__()
#     def run(self):
#         with con:
#             while True:
#                 time.sleep(1)
#                 arr.pop()
#                 length = len(arr)
#                 print("小红吃了1个鱼丸,锅内还有%s个鱼丸" % length)
#                 if length<=0:
#                     con.notify()
#                     con.wait()
# xm = XM()
# xm.start()
#
# xh = XH()
# xh.start()
"""
爬取豆瓣电影top250
"""
import requests
import lxml.etree as etree
urls = ["https://movie.douban.com/top250?start=%s"%i for i in range(0,226,25)]

class Mytest(Thread):
    def __init__(self):
        super(Mytest,self).__init__()
    def run(self):
        while len(urls)>0:
            url = urls.pop()
            res = requests.get(url).text
            html = etree.HTML(res)
            titles = html.xpath("//div[@class='hd']/a/span[1]/text()")
            print(self.name,titles)

for i in range(2):
    mytest = Mytest()
    mytest.start()
print(len(urls))
print(urls)

#信号量
# from threading import Semaphore
# import time
# b = Semaphore(value=3)
# #技术面试，每次3人
# class Ms(Thread):
#     def __init__(self):
#         super(Ms,self).__init__()
#     def run(self):
#         with b:
#             print('%s开始面试，倒计时3秒'%self.name)
#             time.sleep(3)
#             print('%s面试结束，有请下一位'%self.name)
# for i in range(20):
#     m = Ms()
#     m.start()
# 时间
# from threading import Thread,Timer
# def hello():
#     print("123")
#
# t = Timer(10,hello)
# t.start()
# 栅栏
from threading import Barrier
class add:
    def __init__(self):
        pass
