CC ?= cc
CFLAGS ?= -std=c89 -Wall -Wextra -Werror -pedantic
CPPFLAGS ?= -Iinclude

.PHONY: all check clean check-m0

all: build/test_backend

build:
	mkdir -p build

build/test_backend: tests/test_backend.c src/backend.c include/ataristudio/backend.h | build
	$(CC) $(CFLAGS) $(CPPFLAGS) -o $@ tests/test_backend.c src/backend.c

check: build/test_backend check-m0
	./build/test_backend

check-m0:
	python3 scripts/check_m0.py

clean:
	rm -rf build
