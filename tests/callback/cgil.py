#!/usr/bin/env vpython3
import os
import ctypes as ct
import threading
import time

dll = ct.CDLL("./cgil."+("dll" if os.name == "nt" else "so"))

test = dll.test
test.argtypes = [ct.c_int, ct.c_int]

def t(n):
    ret = test(0, 1000000000)
    print('t(%d)=%d'%(n, ret))

def main():
    N = 6
    start_time = time.time()
    for i in range(N):
        t(i)
    end_time = time.time()
    print("Sequential run time: %.2f seconds" % (end_time - start_time))

    start_time = time.time()
    tt = []
    for i in range(N):
        tt.append(threading.Thread(target=t, args=(i,)))
    for t1 in tt:
        t1.start()
    for t1 in tt:
        t1.join()
    end_time = time.time()
    print("Parallel run time: %.2f seconds" % (end_time - start_time))

if __name__ == '__main__':
    main()
