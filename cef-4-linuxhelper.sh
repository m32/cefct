g++ -Wall -Werror -fPIC -shared -o linuxhelper.so \
linuxhelper.cpp \
-I bin \
-lX11 `pkg-config --libs --cflags gtk+-3.0`
