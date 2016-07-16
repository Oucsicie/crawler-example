#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time,sys,Queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(Basemanager):
    pass

#从主机进程获取Queue，不需要回调函数，只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器主机进程:
server_addr= '127.0.0.1'
print('Connect to server %s...'% server_addr)
#端口，验证码与主进程保持一致:
m= QueueManager(addresss= (server_addr,5000),authkey='abc')
#链接主进程:
m.connect()
#获取Queue对象:
task= m.get_task_queue()
result= m.get_result_queue()
#从task队列获取Queue执行任务，结果输入result队列:
for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d*%d...'%(n,n))
        r='%d*%d=%d'%(n,n,n*n)
        time.sleep(1)
        resutlt.put(r)
    except Queue.Empty:
        print('task queue is empty.')
#处理结果:
print('worker exit.')
