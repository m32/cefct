#!/bin/bash
vpython3 cefcapiparse.py bin
vpython3 cefcapiparseinternal.py bin
gcc -I bin -o cefsizes cefsizes.c
./cefsizes
vpython3 cefapp
