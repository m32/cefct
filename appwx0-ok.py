#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import cefapp
import wx
import ctypes as ct
from cefct import libcef
from cefappcommon import Client

libX11 = ct.CDLL("libX11.so.6")

def main():
    input('main')
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GdkX11

def appmain():
    args = [
        '/devel/bin/python3/bin/python3',
    ]
    c = cefapp.App()
    cls = cefapp.AppSetup(c, args)
    cls.Execute()
    print('call.main')
    main()
    print('/call.main')
    cls.Cleanup()
    print('exit', c)

if __name__ == '__main__':
    appmain()
