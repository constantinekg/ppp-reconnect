#!/usr/bin/env python3.4
# Constantine (http://infdots.blogspot.com)
# PPP-oe reconnection
# Add this script into crontab (every 10 minutes): */10 * * * * /path/to/script -d 8.8.8.8 -t 10 > /var/log/pppoe-reconnect.log
import os
import sys
import time
from datetime import datetime

def testchan(h):
	host = h
	res = os.system("ping -c 1 " + host)
	if res == 0:
		print (host, ' is up. Current time is: ', str(datetime.now()))
		sys.exit()
	else:
		print (host, ' is down, trying to reconnect...')
		os.system("poff -a")
		os.system("pon dsl-provider")
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
