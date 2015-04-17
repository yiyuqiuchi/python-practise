#!/usr/bin/env python
#description:ping module

import os

def To_view_help():
    print """
    a   ---- check hosts is alive or not.
    b   ---- check hosts' uptime.
    """
    item = raw_input("please enter an item: ")
    return item

def To_ping_host():
    default_ip = ['132.96.77.29', '132.96.77.130']
    for ip in default_ip:
        cmd = r'ping -c 3 %s' % ip
        os.system(cmd)
    return

def To_exit():
    exit()
    return

if __name__ == '__main__':
    h = To_view_help()
    if h == "a":
        p = To_ping_host()
        h = To_view_help()
    elif h == "q":
        #print "Error!"
        exit()
    else:
        print "Error! Please enter an item again :"
        h = To_view_help()

