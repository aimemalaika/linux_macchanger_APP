#!/usr/bin/en python

import subprocess
import optparse
import random

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="interface to change its MAC address")
parser.add_option("-m","--mac",dest="new_mac",help="new MAC address")
parser.add_option("-r","--random",dest="rand", help="Generate random mac address MAC address use 0 as argument")
(options,argument) = parser.parse_args()
print("*************************************************")
print("              LINUX MACCHANGER V 1.0.0           ")
print("                                                 ")
print("                AUTHOR AIME MALAIKA              ")
print("*************************************************")
int_face = options.interface
if options.new_mac:
    mac_val = options.new_mac
else:
    v1 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v2 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v3 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v4 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v5 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v6 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v7 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v8 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v9 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v10 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v11 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    v12 = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
    mac_val = v2+v1+":" +v4+v3+ ":" +v6+v5+ ":" +v7+v8+ ":" +v10+v9+":"+v11+v12
print("[+] Changing MAC address for interface "+int_face)
subprocess.call(["ifconfig",int_face,"down"])
subprocess.call(["ifconfig",int_face,"hw","ether",mac_val])
subprocess.call(["ifconfig",int_face,"up"])
print("[+] To "+mac_val)
print("[#] END TERMINATED")

