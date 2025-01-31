python3 cefcapiparse.py bin
python3 cefcapiparseinternal.py bin
cl -Ibin -Fecefsizes.exe cefsizes.c
cefsizes
python3 cefapp
