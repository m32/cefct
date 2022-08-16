#!/bin/bash
cef=../cef_binary_104.4.18+g2587cf2+chromium-104.0.5112.81_linux64
vpython3 cefglue_interop_gen.py --cpp-header-dir include --cefglue-dir gen/ --no-backup --cef-dir $cef
gcc -o cefsizes -I $cef cefsizes.c
./cefsizes
rm cefsizes cefsizes.c
