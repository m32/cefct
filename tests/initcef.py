#!/usr/bin/env vpython3
top = "../bin"

import sys
import os

sys.path.insert(1, '..')
# os.chdir(top)

import ctypes
from cefct import libcefdef

libcefdef.LoadLibrary(top + "/libcef.so")
