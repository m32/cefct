#!/bin/bash
if [ -d cef/build ]; then
    pushd cef/build
    ninja cefclient cefsimple
    pushd tests/cefclient/Release
    if [ ! -d include ]; then
        ln -s ../../../../source/include/
    fi
    popd
    popd
    if [ ! -d bin ]; then
        ln -s cef/build/tests/cefclient/Release/ bin
        #ln -s cef/build/tests/cefsimple/Release/ bin
    fi
fi
