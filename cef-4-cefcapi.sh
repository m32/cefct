#!/bin/bash
python3 cefcapiparse.py bin
python3 cefcapiparseinternal.py bin
gcc -I bin -o cefsizes cefsizes.c
./cefsizes
python3 cefapp
