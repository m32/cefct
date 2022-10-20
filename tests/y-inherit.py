#!/usr/bin/env vpython3
from ctypes import Structure

class One(object):
    def __init__(self):
        print('One')
        super().__init__()
        print('/One')

class Two(object):
    def __init__(self):
        print('Two')
        super().__init__()
        print('/Two')

class Three(One, Two):
    pass

print('Three')
cls = Three()

print('One, Structure')
class X(One, Structure):
    pass

cls = X()
