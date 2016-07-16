#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time
import Queue

SHARE_Q= Queue.Queue()
_WORKER_THREAD_NUM= 3

class MyThread(threading.Thread):
    #线程初始化函数
    def __init__(self,func):
        super(MyThread,self).__init__()
        self.func= func

    #重写基类run方法
    def run(self):
        self.func()

#运行逻辑，如抓取
def do_something(item):
    print item

#工作逻辑，因为Queue中包含了wait,notify和锁，所以不必在读取任务时加锁解锁
def worker():
    global SHARE_Q
    while True:
        if not SHARE_Q.empty():
            item= SHARE_Q.get()
            do_something(item)
            time.sleep(1)
            SHARE_Q.task_done()

def main():
    global SHARE_Q
    threads=[]
    for task in xrange(5):
        SHARE_Q.put(task)
    for i in xrange (_WORKER_THREAD_NUM):
        thread=MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    SHARE_Q.join()

if __name__== '__main__':
    main()
