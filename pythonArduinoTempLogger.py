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
arduino = '/dev/ttyUSB0'
ser = serial.Serial('/dev/ttyUSB0', 9600)

# set date and time variable
localtime = time.asctime( time.localtime(time.time()) )

# read serial data from arduino and write to file
# the loop is designed to run twice to capture data from both arduinos transmitting
for x in range (0,2):
   fout = open ('arduinotemp.csv', 'a')
   fout.write(localtime + '\t ' + str(ser.readline()))
   time.sleep(1)
   fout.close()
(x)

