Author: Constantine | myainetwork@gmail.com | http://infdots.blogspot.com
License: GNU/GPL v2

This script was maded for checking of pppoe connection and secondly for reconnection. This script was tested on Ubuntu 14.04.
For first you must create pppoe connection by running pppoeconf utility. After this you will have pppoe connection by 
'dsl-provider' name. After this please make clone from repository by running 'git clone https://github.com/constantinekg/ppp-reconnect' 
and put pppoe-reconnect.py into your favorite directory (as example into /etc). Put this into your crontab:
*/10 * * * * /etc/pppoe-reconnect -d 8.8.8.8 -t 10 > /var/log/pppoe-reconnect.log
This will make checks (10 times) every 10 minutes for google dns by running ping command. If google dns will unavailable script 
will make reconnection of pppoe.
