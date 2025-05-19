CC=gcc
CFLAGS=-Wall -Wextra -I./include
SRC=app.c src/*.c
BIN=bin/todolist

all: prepare $(BIN)

prepare:
	mkdir -p bin

$(BIN): $(SRC)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -rf bin/