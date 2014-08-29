Data_Acquistion
===============

Python Scripts for Data Acquistion
#! /usr/bin/python
 
from time import time
import sys
 
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import *
from Phidgets.Devices.TemperatureSensor import *
 
# Define an error catching function so we can call it on "try...except" blocks
def LocalErrorCatcher(event):
    print("Phidget Exception: " + str(e.code) + " - " + str(e.details) + ", Exiting...")
    exit(1)
 
# Obtain an initial time from which to generate timestamps
start = time()
 
# Clear and open the data file for writing
outfile = open("temperature_data_py.csv", "w")
 
# Create a listener function for changes in thermocouple temperature
def TemperatureDataHandler(e):
    global start
    global outfile
 
    now = time() - start
 
    # Get the board temperature
    ambientTemp = e.device.getAmbientTemperature()
 
    # Write the data to the text file
    outfile.write(str(now) + "," + str(e.temperature) + "," + str(ambientTemp) + "\n")
 
    # Print a dot to indicate one more point recorded
    sys.stdout.write(".")
    sys.stdout.flush()
 
# Write a header to the text file first thing
outfile.write("Time,Thermocouple-Temperature,Ambient-Board-Temperature\n")
 
# Create the Phidget software object, hook in the event function, and open the object
device = TemperatureSensor()
device.setOnTemperatureChangeHandler(TemperatureDataHandler)
device.openPhidget()
device.waitForAttach(10000)
 
# Set the thermocouple type and trigger (0 = record all data)
try:
    device.setThermocoupleType(0, ThermocoupleType.PHIDGET_TEMPERATURE_SENSOR_K_TYPE)
except PhidgetException as e: LocalErrorCatcher(e)
device.setTemperatureChangeTrigger(0, 0)
 
print("Press Enter to end anytime...");
character = str(raw_input())
 
device.closePhidget()
exit(0)
