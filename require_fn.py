#!/usr/bin/python
import struct



def addPad(data,size):
    if size < 8 :
        for i in range (1, size+1) :
           data = data + struct.pack("B",0x00)
    else:
        mod = size / 8
        for i in range(1,mod+1) :
           data =  data +struct.pack("Q",0x00)
        mod = size % 8
        for i in range(1,mod+1):
           data = data + struct.pack("B",0x00)
    return data
