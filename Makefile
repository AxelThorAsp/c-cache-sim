#
# Note: requires a 64-bit x86-64 system
#
CC = gcc
CFLAGS = -g -Wall -Werror -std=c99 -m64

csim: csim.c
	$(CC) $(CFLAGS) -o csim csim.c 

