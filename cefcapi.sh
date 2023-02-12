#!/bin/bash
vpython3 cefcapiparse.py bin
vpython3 cefcapiparseinternal.py bin
gcc -Ibin -o cefsizes cefsizes.c
./cefsizes
