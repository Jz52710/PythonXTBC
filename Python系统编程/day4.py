from multiprocessing import Manager
# from multiprocessing import Process,Array,Value
# import time
# """
# Array 数组
# Value 值
# """
# def fun1(arr,value):
#     arr[0] = 9
#     value.value = 4299
#
# def fun2(arr,value):
#     time.sleep(2)
#     print(list(arr))
#     print(value.value)
#
# if __name__ == "__main__":
#     arr = Array("i",[1,2,3,4,5])
#     value = Value("i",10)
#     print(list(arr))
#     print(value.value)
#     p1 = Process(target=fun1,args=(arr,value))
#     p1.start()
#     p2 = Process(target=fun2, args=(arr, value))
#     p2.start()

# from multiprocessing import Manager,Process
#
# def fun1(l,d):
#     l.append(7)
#     d["sex"]="女"
#
# def fun2(l,d):
#     arr = [5,2,7,1,0]
#     for i in arr:
#         l.append(i)
#     d["edg"] = "Clearlove"
# if __name__ == "__main__":
#     manage = Manager()#创建一个管理器对象
#     l = manage.list([1,2,3,4,5])#创建一个数据代理
#     d = manage.dict({"name":"小白","age":"20"})#创建 数据代理
#     p = Process(target=fun1,args=(l,d))
#     p.start()
#     p.join()
#     print(l,d)
#     p = Process(target=fun2,args=(l,d))
#     p.start()
#     p.join()
#     print(l,d)


from multiprocessing.pool import Pool
# def fun1():
#     pass
#
# if __name__ == "__main__":
#     pass

from multiprocessing import Pool
import time
def fun():
    time.sleep(1)
    return 123

def fun2(item):
    return item+1

if __name__ == "__main__":
    pool = Pool(100)  # 创建进程池 5代表进程池的进程数量
    res =pool.apply(fun)
    res = pool.apply_async(fun)
    res.wait()
    print(res.get())
    start = time.time()
    res1 = pool.map(fun2,range(100000))
    # res = map(fun2,range(100000))
    for i in res1:
        print(i)
    # print(res)
    end = time.time()
    print('运行总时间：%s'%(end-start))