# Makefile for i2c stuff
# Based on the Makefile for the overo-arduino-i2c test program

ifeq ($(strip $(OETMP)),)
	OETMP = $(HOME)/overo-oe/tmp
endif


TOOLDIR = $(OETMP)/sysroots/`uname -m`-linux/usr/armv7a/bin
STAGEDIR = ${OETMP}/sysroots/armv7a-angstrom-linux-gnueabi/usr

CC = ${TOOLDIR}/arm-angstrom-linux-gnueabi-gcc
CFLAGS = -Wall

LIBDIR = $(STAGEDIR)/lib
INCDIR = $(STAGEDIR)/include

TARGET = i2c_imu_read

$(TARGET) :
	$(CC) $(CFLAGS) -I $(INCDIR) -I . -L $(LIBDIR) sensors.c overo-i2c.c -o $(TARGET)

test:
	gcc sensors.c overo-i2c.c -o test

razr:
	$(CC) $(CFLAGS) -I $(INCDIR) -I . -L $(LIBDIR) Razor_AHRS.c dcm.c math.c output.c sensors.c overo-i2c.c -o razr

install:
	scp $(TARGET) root@192.168.23.3:/home/root

clean :
	rm -f $(TARGET)
