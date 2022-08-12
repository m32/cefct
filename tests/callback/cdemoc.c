/*
gcc -shared -fPIC -o cdemoc.so cdemoc.c
cl -Ox -MD -LD cdemoc.c

*/

#include <stdio.h>

typedef int *(*tcproc)(int *iarg);

#ifdef _WIN32
#define _EXPORT __declspec(dllexport)
#else
#define _EXPORT __attribute__((visibility("default")))
#endif
_EXPORT
int my_number = 1234;

_EXPORT
int cproc(tcproc cb){
    int a = 1;
    int *i = &a;
    printf("cproc before: i=%p &a=%p a=%d *i=%d\n", i, &a, a, *i);
    i = (*cb)(&a);
    printf("cproc  after: i=%p &a=%p a=%d *i=%d\n", i, &a, a, *i);
    return 5;
}
