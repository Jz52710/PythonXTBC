# 创建进程
"""
1.构造函数
t = Thread(target=fun)
target 线程执行功能
args fun 的参数
kwargs fun 的参数
groups 线程扩展时使用 一般默认为None

t 线程对象属性
t.start()   运行
t.join(blocking,timeout)    阻塞
t.name()    线程名字
t.ident()   线程id
t.daemon    是否为守护进程 默认False。    守护进程：主进程不会等待守护进程运行结束
t.is_alive()    判断线程是否存活

2.通过继承类的方式
class MyTread(Thread):
    def __init__(self)；
        super(MyThread,self).__init__()
    def run(self):
        #   线程被start()时执行的功能
        pass
t = MyTread()
"""
#锁
"""
l = Lock()
l.acquire() 上锁
l.release() 释放锁
死锁：两个都在阻塞等待对方释放锁
Rlock   递归锁、重复锁
Rlock和Lock区别
同一个线程内，Rlock可以重复上锁，Lock释放锁后才能上锁
Lock    锁上的状态时可以释放锁，释放状态的锁释放时会报错。
Rlock   是一个局部锁，在一个线程中上锁后，其他线程无法释放。Lock全局锁
"""