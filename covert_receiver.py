#!/usr/bin/python

from scapy.utils import *
from scapy.all import *
from scapy.utils import rdpcap
import sys
import random
import socket

print "<cmd> <filter> <interface> <verbose>"


def filterfn(p):
    if p.haslayer(TCP):
       if p[TCP].dport==80:
          return True
    return False 


fd=0;
try :
      fd = open('./covert_data/'+str(random.randint(0x01, 0xffffffff)),'w')
except:
      print "FAILED TO OPEN THE OUTPUT FILE"
      quit()


while True :
   # read one packet

   # print on the terminal
   pkt = sniff(lfilter=filterfn,count=1,iface=sys.argv[2])
   if sys.argv[3] == 'v':
      print pkt[0].show()
   else :
      print pkt[0].summary()
   try :
      ip = pkt[0][IP]
      # extract the data from the IP record route optiions
      ops = ip.options
      if len(ops) > 0 :
         for op in ops:
             if op.option == 7 :
               ips = op.routers
               for ip in ips :
                   data = socket.inet_aton(ip)
                   fd.write(data)
                   fd.flush()
      else :
        print "PACKET HAS NO OPTIONS"
   except:
      print "FAILED TO GET THE IP HEADER FROM PACKET"

