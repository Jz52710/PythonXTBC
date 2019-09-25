import multiprocessing
import threading
import os
import time
import random
import sys

def copy_file(queue, file_name, source_folder_name, dest_folder_name):
    # print('正在复制：%s' % file_name)
    if os.path.isdir(source_folder_name + '/' + file_name):#判断是否为目录
        queue.put(file_name)#插入内容
        return
    if not os.path.exists(dest_folder_name):#如果路径存在，返回True，否则Flase
        os.mkdir(dest_folder_name)#创建目录
    data_file = open(source_folder_name + '/' + file_name, 'rb')#旧文件
    cp_file = open(dest_folder_name + '/' + file_name, 'wb')#新文件
    while True:
        content = data_file.read(4096)#读取旧文件中的内容
        if len(content) == 0:
            break
        cp_file.write(content)#把旧文件里面的东西写到新文件中
    data_file.close()
    cp_file.close()
    # print('%s文件复制完成！' % file_name)
    queue.put(file_name)

def main():
    source_folder_name = input("请输入文件夹:")
    dest_folder_name = source_folder_name + "附件"#新文件夹名字
    file_names = os.listdir(source_folder_name)#返回指定目录下所有的文件和目录名的一个列表，但是并没有列出来什么是目录，什么是文件
    # 创建一个队里
    queue = multiprocessing.Manager().Queue(128)#队列
    # 创建进程池
    p = multiprocessing.Pool(1)#线程池
    for file_name in file_names:
        # print('put file_name %s' % file_name)
        p.apply_async(copy_file, args=(queue, file_name, source_folder_name, dest_folder_name))#返回结果对象的方法的一种变体
    p.close()
    # p.join()
    all_file_nums = len(file_names)
    while True:
        file_name = queue.get()#获取内容
        if file_name in file_names:
            file_names.remove(file_name)
        copy_rate = (all_file_nums - len(file_names)) * 100 / all_file_nums
        print("\r%.2f=========>(%s) (%0.2f/%0.2f)" % (copy_rate, file_name, len(file_names), all_file_nums) + " " * 50,
              end="")
        # \r 默认表示将输出的内容返回到第一个指针，这样的话，后面的内容会覆盖前面的内容
        # sys.stdout.flush()
        # if len(file_names) < 5:
        #    print("remaining: %s" % file_names)
        if copy_rate >= 100:
            break
    print('拷贝文件完成!')

if __name__ == "__main__":
    main()