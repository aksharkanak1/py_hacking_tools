#!/usr/bin/python

from scapy.utils import *
from scapy.all import *
from scapy.utils import rdpcap
import sys
import struct
import socket
import require_fn
import time

print "<cmd> <file> <interface> <host> "

router=[]
fd = open(sys.argv[1],'r')
flushPkts=False
while True :
      rd = fd.read(4)
      if (len(rd) < 4) and len(rd) > 0:
            rd = require_fn.addPad(rd,4-len(rd))
            flushPkts =True
      elif len(rd) == 0 :
            flushPkts =True
      if len(rd) == 4:
            ip = socket.inet_ntoa(rd)
            router.append(ip)
      if len(router) == 10 or flushPkts :
            op=IPOption('\x07')
            op.routers = router
            pkt = Ether()/IP(dst=sys.argv[3],options=op)/TCP(dport=80)
            del pkt[IP].chksum
            del pkt[TCP].chksum
            pkt.show2()
            sendp(pkt, iface=sys.argv[2])
            router=[]
            time.sleep(0.5)
      if flushPkts == True:
            print "flushPkts = 1"
            fd.close()
            break

