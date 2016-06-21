#!/usr/bin/env python

import threading

def worker(num):
    """Thread worker function"""
    print 'Worker : %s' %num
    return
thread = []
for i in range(5):
    t=threading.Thread(target=worker,args=(i,))
    thread.append(t)
    t.start()

