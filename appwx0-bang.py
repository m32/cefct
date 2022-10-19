#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import cefapp
import wx
import ctypes
from cefct import libcef
import ctypes as ct
from cefct import libcef
from cefappcommon import Client

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkX11

libX11 = ctypes.CDLL("libX11.so.6")

def main():
    input('main')

def appmain():
    args = [
        '/devel/bin/python3/bin/python3',
    ]
    c = cefapp.App()
    result = cefapp.AppStartup(c, args)
    print('call.main')
    main()
    print('/call.main')
    #cefapp.AppCleanup(result)
    print('exit', c)

if __name__ == '__main__':
    appmain()
