import serial
 
# Duration in seconds, sample rate (fs) in Hz
duration = 420;
fs = 2.0;
 
# Calculate sample time and number of loops needed
T = 1/fs;
loops = int(duration/T)
 
# Setup serial port and open file to write
serial = serial.Serial(&quot;COM3&quot;, 9600, timeout=5)#choose COM and BAUD rate
f = open(&quot;Data1.raw&quot;, &quot;w&quot;)
 
# Loop as needed, writing datato file
for i in range(0,1):#loops once
    data = serial.read()
    f.write(data)
    print data),
# Be sure to close the file afterwards
f.close()

clear all;
close all;
clc
 
fid = fopen(&#039;Data1.raw&#039;);
raw_data = fread(fid, &#039;uint16&#039;);
fclose(fid);
 
x = double(raw_data)
 
plot(x);
