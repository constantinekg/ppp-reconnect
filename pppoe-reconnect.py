#!/usr/bin/env python3.4
# Constantine (http://infdots.blogspot.com)
import os
import sys
import time
from datetime import datetime

def testchan(h):
	host = h
	res = os.system("ping -c 1 " + host)
	if res == 0:
		print (host, ' is up. Current time is: ', str(datetime.now()))
		#os.system("cvlc " + 'sc.mpeg ' + '--play-and-exit') # Uncomment this line and comment line behind if you want to listen mpeg file then system sound beeper
		os.system("beep " + '-l 350 -f 392 -D 100 -n -l 350 -f 392 -D 100 -n -l 350 -f 392 -D 100 -n -l 250 -f 311.1 -D 100 -n -l 25 -f 466.2 -D 100 -n -l 350 -f 392 -D 100 -n -l 250 -f 311.1 -D 100 -n -l 25 -f 466.2 -D 100 -n -l 700 -f 392 -D 100 -n -l 350 -f 587.32 -D 100 -n -l 350 -f 587.32 -D 100 -n -l 350 -f 587.32 -D 100 -n -l 250 -f 622.26 -D 100 -n -l 25 -f 466.2 -D 100 -n -l 350 -f 369.99 -D 100 -n -l 250 -f 311.1 -D 100 -n -l 25 -f 466.2 -D 100 -n -l 700 -f 392 -D 100 -n -l 350 -f 784 -D 100 -n -l 250 -f 392 -D 100 -n -l 25 -f 392 -D 100 -n -l 350 -f 784 -D 100 -n -l 250 -f 739.98 -D 100 -n -l 25 -f 698.46 -D 100 -n -l 25 -f 659.26 -D 100 -n -l 25 -f 622.26 -D 100 -n -l 50 -f 659.26 -D 400 -n -l 25 -f 415.3 -D 200 -n -l 350 -f 554.36 -D 100 -n -l 250 -f 523.25 -D 100 -n -l 25 -f 493.88 -D 100 -n -l 25 -f 466.16 -D 100 -n -l 25 -f 440 -D 100 -n -l 50 -f 466.16 -D 400 -n -l 25 -f 311.13 -D 200 -n -l 350 -f 369.99 -D 100 -n -l 250 -f 311.13 -D 100 -n -l 25 -f 392 -D 100 -n -l 350 -f 466.16 -D 100 -n -l 250 -f 392 -D 100 -n -l 25 -f 466.16 -D 100 -n -l 700 -f 587.32 -D 100 -n -l 350 -f 784 -D 100 -n -l 250 -f 392 -D 100 -n -l 25 -f 392 -D 100 -n -l 350 -f 784 -D 100 -n -l 250 -f 739.98 -D 100 -n -l 25 -f 698.46 -D 100 -n -l 25 -f 659.26 -D 100 -n -l 25 -f 622.26 -D 100 -n -l 50 -f 659.26 -D 400 -n -l 25 -f 415.3 -D 200 -n -l 350 -f 554.36 -D 100 -n -l 250 -f 523.25 -D 100 -n -l 25 -f 493.88 -D 100 -n -l 25 -f 466.16 -D 100 -n -l 25 -f 440 -D 100 -n -l 50 -f 466.16 -D 400 -n -l 25 -f 311.13 -D 200 -n -l 350 -f 392 -D 100 -n -l 250 -f 311.13 -D 100 -n -l 25 -f 466.16 -D 100 -n -l 300 -f 392.00 -D 150 -n -l 250 -f 311.13 -D 100 -n -l 25 -f 466.16 -D 100 -n -l 700 -f 392') # Starwars system beeper sound
		sys.exit()
	else:
		print (host, ' is down')
		return True

def helper():
	print ('Programm parameters: \n -d - Destionation (hostname or ip address) \n -t - Time for checking (in seconds) \n -h - Help')

if __name__ == '__main__':
	
    if len (sys.argv) == 1:
        helper()
    elif (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
            helper()
            sys.exit(1)
    else:
        if len (sys.argv) < 5:
            print ("Error. Too few parameters.")
            sys.exit (1)

        if len (sys.argv) > 5:
            print ("Error. Too many parameters.")
            sys.exit (1)

        host_name = sys.argv[1]
        host_value = sys.argv[2]
        time_name = sys.argv[3]
        time_value = sys.argv[4]

        if (host_name == "--dest" or host_name == "-d" and time_name == "--time" or time_name == "-t"):
            print ("Host is: {}".format (host_value))
            print ("Time is: {}".format (time_value))
            print ("Beginning of checking...")
            while True:
                try:
                    while True:
                        testchan(host_value)
                        time.sleep(float(time_value))
                except:
                    sys.exit(1)
        
        else:
            print ("Error. Unknown parameter")
            helper()
            sys.exit (1)
