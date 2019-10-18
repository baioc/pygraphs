APP_NAME=libpygraphs

CC = g++ -std=c++17
CFLAGS = -Wall
TEST_CFLAGS = -fsanitize=leak
BUILD_CFLAGS = -fpic -DNDEBUG=1 -O2

SC = swig
SFLAGS = -python -c++

SRC = graph.hpp
INT = libpygraphs.i
GEN = libpygraphs_wrap.cxx
OBJ = libpygraphs_wrap.o
LIBS = -I/usr/include/python3.7m
TST = main.cpp

default:
	make build

build: $(INT) $(SRC)
	$(SC) $(SFLAGS) $(INT)
	$(CC) $(CFLAGS) $(BUILD_CFLAGS) $(LIBS) -c $(GEN)
	$(CC) -shared -o _$(APP_NAME).so $(OBJ)

test: $(TST) $(SRC)
	$(CC) $(CFLAGS) $(TEST_CFLAGS) -o test_$(APP_NAME).out $(TST)

all:
	make test
	make build

clean:
	- rm test_$(APP_NAME).out
	- rm $(APP_NAME).py
	- rm $(APP_NAME)_wrap.cxx
	- rm *.o
	- rm _$(APP_NAME).so
