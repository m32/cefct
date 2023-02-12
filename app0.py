#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import cefapp
import time
import ctypes as ct
from cefct import libcef
from cefappcommon import Client

def appmain():
    args = [
        '/devel/bin/python3/bin/python3',
        '/devel/00mirror-cvs/00-m32/cefct/app0.py',
    ]
    c = cefapp.App()
    print('AppStartup')
    cls = cefapp.AppSetup(c, args)
    cls.Execute()
    time.sleep(3)
    print('AppCleanup')
    cls.Cleanup()
    print('exit', c)

if __name__ == '__main__':
    appmain()
