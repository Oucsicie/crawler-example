#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import random, time, Queue

MAX_SIZE = 5
SHARE_Q = []  #模拟共享队列
CONDITION = threading.Condition()

class Producer(threading.Thread) :

    def run(self) :
        products = range(5)
        global SHARE_Q
        while True :
            CONDITION.acquire()
            if len(SHARE_Q) == 5 :
                print "Queue is full.."
                CONDITION.wait()
                print "Consumer have comsumed something"
            product = random.choice(products)
            SHARE_Q.append(product)
            print "Producer : ", product
            CONDITION.notify()
            CONDITION.release()
            time.sleep(random.random())

class Consumer(threading.Thread) :

    def run(self) :
        global SHARE_Q
        while True:
            CONDITION.acquire()
            if not SHARE_Q :
                print "Queue is Empty..."
                CONDITION.wait()
                print "Producer have producted something"
            product = SHARE_Q.pop(0)
            print "Consumer :", product
            CONDITION.notify()
            CONDITION.release()
            time.sleep(random.random())

def main() :
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()

if __name__ == '__main__':
    main()

