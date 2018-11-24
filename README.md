# Linux macchanger APP v1.0.0

*************************************************
              LINUX MACCHANGER V 1.0.0

                AUTHOR AIME MALAIKA
*************************************************

Usage: changemymac.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        new MAC address
  -r RAND, --random=RAND
                        Generate random mac address MAC address use 0 as
                        argument

Sample
1. see help 

python changemymac.py --help

2.modify to a precise mac address

python changemymac.py -i eth0 -m 00:11:22:33:33:78

3.modify to a random mac address

python changemymac.py -i eth0 -r 0


