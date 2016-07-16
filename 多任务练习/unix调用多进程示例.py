#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""调用unix类系统fork()函数示例"""
import os

print 'process.(%s) start...' %os.getpid()
pid= os.fork()
if pid= 0:
    print'I am child process (%s) and my parent is %s'%(os.getpid(),os.getppid())
else:
    print'I (%s) just created a child process(%s).'%(os.getpid(),pid)
