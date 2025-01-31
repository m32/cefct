#!/usr/bin/env vpython3
import cefapp
from cefct import libcef

def main():
    c = cefapp.App()
    cls = cefapp.AppSetup(c)
    cls.Execute()

    print('loop', flush=True)
    from appgtk1a import gtkmain
    gtkmain()

    cls.Cleanup()
    print('*'*20, 'done')
if __name__ == '__main__':
    main()
