#!/bin/bash
if [ -d cef/build ]; then
pushd cef/build
cmake \
-G "Ninja" \
-DCMAKE_BUILD_TYPE=Release \
../source
popd
fi
