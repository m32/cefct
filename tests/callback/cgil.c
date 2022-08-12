/*
http://caswenson.com/2009_06_13_bypassing_the_python_gil_with_ctypes.html
*/

#ifdef _WIN32
#define _EXPORT __declspec(dllexport)
#else
#define _EXPORT __attribute__((visibility("default")))
#endif

_EXPORT
int test(int from, int to)
{
  int i;
  int s = 0;

  for (i = from; i < to; i++)
    if (i % 3 == 0)
      s += i;

  return s;
}
