#!/usr/bin/env python  
#encoding: utf-8
import threading 
import data.realData as rd
'''
ccc=open('F:/day/2015-03-31/000014.ss','rb')
buf=ccc.read()
print(len(buf))
a=struct.unpack('fffffffffffffffff8s',buf[0:76])
#print(struct.unpack('fff8s',buf[20:40]))
#print(struct.unpack('fff8s',buf[40:60]))
print(a)
'''
jxsc=0.0  
if __name__=='__main__':
    
    #print()
    #thread.start_new_thread(rd.realDate_start())
    threading.Thread.start(rd.realDate_start())
