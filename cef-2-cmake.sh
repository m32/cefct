#!/bin/bash
if [ ! -d cef/build ]; then
    fname=cef_binary_132.3.1+g144febe+chromium-132.0.6834.83_linux64
    if [ ! -f "$fname.tar.bz2" ]; then
        fname=cef_binary_132.3.1+g144febe+chromium-132.0.6834.83_linux64_client
        if [ ! -f "$fname.tar.bz2" ]; then
            echo "no directory cef build and not tarball found"
        else
            tar jxf $fname.tar.bz2
            ln -s $fname/Release/ bin
        fi
    else
        mkdir -p cef/build
        cd cef
        tar jxf ../$fname.tar.bz2
        ln -s $fname/ source
        cd ..
    fi
fi
if [ -d cef/build ]; then
    pushd cef/build
    cmake \
        -G "Ninja" \
        -DCMAKE_BUILD_TYPE=Release \
        ../source
    popd
fi
