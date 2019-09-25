from multiprocessing import Process,active_children,cpu_count,current_process,get_all_start_methods,get_context,get_start_method,queues,Queue

# print("返回主进程中所有的子进程",active_children())
# print("返回CPU的核心数",cpu_count())
# print("返回当前进程",current_process())
# print("获得进程全部开启方法",get_all_start_methods())
# print("返回默认的上下文",get_context())
# print("返回默认的进程开启方法",get_start_method())

"""

"""
# 创建进程
# （1）构造函数
# import time,random
#
# def fun():
#     time.sleep(random.randint(1,3))
#     print("710")
#
# if __name__  == "__main__":
#     for i in range(10):
#         p = Process(target=fun)
#         p.start()

# (2)继承类创建
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess,self).__init__()
#     def run(self):
#         fun()
#队列
# q = queues.Queue()
# 接收正整数，用来表示 队列的长度，如果是 -1 0 代表无限长
"""
q.put() 插入内容
q.get() 获取内容
q.full() 是否已满
q.empty() 是否为空
q.task_done() 表示前面排队的任务已经被完成
q.join() 阻塞
"""
# if __name__ == "__main__":
#     q = Queue(2)
#
#     q.put(1)
#     print("qsize",q.qsize())
#     print("full",q.full())
#     print("empty",q.empty())
#     q.put(2)
#     print("qsize",q.qsize())
#     print("full",q.full())
#     print("empty",q.empty())
# #     # q.put(3)
# #     # print("qsize", q.qsize())
# #     # print("full", q.full())
# #     # print("empty", q.empty())


#自己实现full，empty，qsize
# from threading import Lock
# class Myqueue:
#     def __init__(self,mysize=0):
#         self.__data = []
#         self.__mysize = mysize
#         self.__isfull = False
#         self.__isempty = True
#         self.__lock = Lock()
#         self.__lock.acquire()
#     def qsize(self):
#         return len(self.__data)
#     def full(self):
#         if self.__mysize == 0 or self.__mysize == -1:
#             return False
#         elif len(self.__data)==self.__mysize:
#             return True
#         else:
#             return False
#     def empty(self):
#         if len(self.__data) ==0:
#             return True
#         else:
#             return False
#     def get(self):
#         if self.qsize()<=0:
#             self.__lock.acquire()
#         else:
#             if self.__lock.locked():
#                 self.__lock.release()
#         return self.__data.pop(0)
#     def put(self,data):
#         if self.qsize()>= self.__mysize:
#             self.__lock.acquire()
#         else:
#             self.__data.append(data)
#
# q = Myqueue(3)
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.full())
# print(q.qsize())
# print(q.empty())
# print("get",q.get())
# # q.put(4)


# from multiprocessing import Pipe
# # Pipe() 管道
# conn1,conn2 = Pipe(True) # 双工
#
# def fun1(con):
#     con.send("fun1：hello")
#     print(con.recv())
# def fun2(con):
#     print(con.recv())
#     con.send("fun2: hi")
#
# if __name__ =="__main__":
#     p1= Process(target=fun1,args=(conn1,))
#     p1.start()
#     p2 = Process(target=fun2,args=(conn2,))
#     p2.start()

import os
a= os.path.exists('day1')
os.mkdir('daf')
print(a)