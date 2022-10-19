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
    ]
    c = cefapp.App()
    print('AppStartup')
    result = cefapp.AppStartup(c, args)
    time.sleep(3)
    print('AppCleanup')
    cefapp.AppCleanup(result)
    print('exit', c)

if __name__ == '__main__':
    appmain()
