#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        Arduino Temperature & Humidity Data Logger
# Purpose:     log temperature readings throughout a given area
#
# Author:      shatteredhaven
#
# Created:     January 2013
#
#-------------------------------------------------------------------------------

import serial
import time

# read from the serial port. use COM# (ex. COM4) if running on Windows instead of Linux
#arduino = '/dev/ttyUSB0'
#ser = serial.Serial('/dev/ttyUSB0', 9600)

arduino = 'COM8'
ser = serial.Serial('COM8', 9600)

# pause after opening serial on arduino
time.sleep(10)

# set date and time variable
localtime = time.asctime( time.localtime(time.time()) )

# read serial data from arduino and write to file
ser.write('2')
fout = open ('arduinotemp.csv', 'a')
fout.write(localtime + '\t ' + str(ser.readline()))
fout.close()
time.sleep(20)
# pause 20 seconds then send message from arduino 2 and writes the response
ser.write('4')
fout = open ('arduinotemp.csv', 'a')
fout.write(localtime + '\t ' + str(ser.readline()))
fout.close()


