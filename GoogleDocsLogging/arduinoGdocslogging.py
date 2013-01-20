#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        Arduino Temperature & Humidity Data Logger
# Purpose:     log temperature readings throughout a given area
#
# Author:      shatteredhaven
#              modified from Adafruit Raspberry Pi DHT11 logging example
#
# Created:     January 2013
#
#-------------------------------------------------------------------------------

import serial
import time
import subprocess
import re
import sys
import datetime
import gspread

# -------------------------------------------------------------------------------
# Google Account Details
# -------------------------------------------------------------------------------

# Account details for google docs
email       = 'emailaddress@domain.com'
password    = 'password'
# -------------------------------------------------------------------------------

# read from the serial port. use COM# (ex. COM4) if running on Windows instead of Linux
arduino = '/dev/ttyUSB0'
ser = serial.Serial('/dev/ttyUSB0', 9600)

# pause after opening serial on arduino
time.sleep(10)
print 'sleep'

# Login with your Google account
try:
  print 'logging in'
  gc = gspread.login(email, password)
except:
  print "Unable to log in.  Check your email address/password"
  sys.exit()

# Open a worksheet from your spreadsheet. Replace spreadsheet name with the name of the document on your google drive.
try:
  print 'opening spreadsheet'
  sh = gc.open('spreadsheet name')
# write to sheet 1
  worksheet = sh.get_worksheet(0)
# write to sheet 2
  worksheet2 = sh.get_worksheet(1)

except:
  print "Unable to open the spreadsheet.  Check your filename: %s" % spreadsheet
  sys.exit()
  
# read serial data from the first arduino and write to file
print 'write to arduino'
ser.write('2')
try:
  print 'write to file'
  values = [datetime.datetime.now(), str(ser.readline(8)), str(ser.readline(10)), str(ser.readline(4)), str(ser.readline(4)), str(ser.readline(15)), str(ser.readline(5)), str(ser.readline())]
  worksheet.append_row(values)
except:
  print "Unable to append data.  Check your connection?"
  sys.exit()
  time.sleep(20)

# pause 20 seconds then send message from the second arduino and writes the response
ser.write('4')
try:
  print 'write to file'
  values = [datetime.datetime.now(), str(ser.readline(8)), str(ser.readline(10)), str(ser.readline(4)), str(ser.readline(4)), str(ser.readline(15)), str(ser.readline(5)), str(ser.readline())]
  worksheet2.append_row(values)
except:
  print "Unable to append data.  Check your connection?"
  sys.exit()
