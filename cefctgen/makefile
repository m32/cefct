VPYTHON := /devel/bin/python3/bin/python
#VPYTHON = python
PYCONFIG=/usr/bin/python3-config

python_version_full := $(wordlist 2,4,$(subst ., ,$(shell $(VPYTHON) --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})
python_version = ${python_version_major}.${python_version_minor}

PYTHON_LIBRARY = $(shell $(PYCONFIG) --configdir)/libpython${python_version}.so

CFLAGS += $(shell $(PYCONFIG) --cflags)
CFLAGS += -I /devel/00-build/cffi/glucef/cef_binary_91.1.21+g9dd45fe+chromium-91.0.4472.114_linux64

LDFLAGS += -lpython${python_version} $(shell $(PYCONFIG) --ldflags)

CFLAGS += \
    -DVIRTUAL_PYTHON_PATH=L\"$(VPYTHON)\" \
    -DPYTHON_LIBRARY=\"$(PYTHON_LIBRARY)\" \
    -I .

all : zpython

zpython : zpython.o
	g++ -fPIC -o $@ $^ $(LDFLAGS)

zpython.o : zpython.cpp
	g++ -fPIC -o $@ -c $(CFLAGS) $^

clean:
	rm -f zpython zpython.o
