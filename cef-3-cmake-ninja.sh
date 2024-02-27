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
fi
if [ ! -d bin ]; then
ln -s cef/build/tests/cefclient/Release/ bin
fi
