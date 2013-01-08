Arduino RF Temperature & Humidity Data Logger
==============
multiple arduinos transmitting temperature & humidity data via RF 

**Overview** 
This project uses multiple arduinos outfitted with the OpenSourceRF wireless shields to transmit temperature and humidity and uses a python script to log the data in a CSV file. 

This set up would also likely work with standard RF transmitters/receivers and the wire arduino library. 

**tutorial & photos**

**Software Used**
- pySerial - allows python to read from the serial port
- DHT-sensor-library - DHT sensor library from adafruit
- arduino IDE

**Files**
- arduinotemp.csv - csv file the python script logs data to
- arduinotemp.sh - shell script that executes the python script (if cron job will not execute python directly)
- arduinotempcron.txt - cron job example
- ArduinoTempLogger.ino - arduino sketch for arduino(s)
- OpenSourceRFDHT11TempLogging.fzz - fritzing schematic
- pythonArduinoTempLogger.py - python script

**Materials Used**
- two (2) OpenSource RF arduino shields (http://www.opensourcerf.com/)
- two (2) Arduino Unos
- two (2) DHT11 temperature sensors 
- two (2) 10K Ohm resistors
- two (2) breadboard (preferably mini-breadboard)
- one (1) Wireless RF USB Dongle (http://www.opensourcerf.com/)
- misc wires

**Issues/Notes**
- occasionally there is an issue where the data being read is cut off/formatted improperly. Still trying to correct.
- Windows 7 machine immediately recognized the USB device but I have had some issues with a Raspberry Pi. For whatever reason the Pi wouldn't immediately recognize the device and I had to toggle the network on/off switch before I was able to SSH into the device