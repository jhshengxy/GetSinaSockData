#!/usr/bin/env python  
#encoding: utf-8
import signal
import struct
'''
            0：open，今日开盘价
            1：pre_close，昨日收盘价
            2：price，当前价格
            3：high，今日最高价
            4：low，今日最低价
            5：volumn，成交量 maybe you need do volumn/100
            6：amount，成交金额（元 CNY）
            7：b1_v，委买一（笔数 bid volume）
            8：b1_p，委买一（价格 bid price）
            9：b2_v，“买二”
            10：b2_p，“买二”
            11：b3_v，“买三”
            12：b3_p，“买三”
            13：b4_v，“买四”
            14：b4_p，“买四”
            15：b5_v，“买五”
            16：b5_p，“买五”
            
            17：b1_v，委卖一（笔数 bid volume）
            18：b1_p，委卖一（价格 bid price）
            19：b2_v，“卖二”
            20：b2_p，“卖二”
            21：b3_v，“卖三”
            22：b3_p，“卖三”
            23：b4_v，“卖四”
            24：b4_p，“卖四”
            25：b5_v，“卖五”
            26：b5_p，“卖五”
            
            27:时间
'''
ccc=open('F:/day/2015-04-24/000045.ss','rb')
buf=ccc.read()
print(len(buf))
s=0

while (s+116)<=len(buf):
    a=struct.unpack('fffffffffffffffffffffffffff8s',buf[s:s+116])
    #print(struct.unpack('fff8s',buf[20:40]))
    #print(struct.unpack('fff8s',buf[40:60]))
    s=s+116
    print(a)
    
    #if s>100000:
    #    break
    #17
    '''print(str(round(a[0],2))+','+str(round(a[1],2))+','+str(round(a[2],2))+','+str(round(a[3],2))+','+str(round(a[4],2))+
          ','+str(round(a[5],2))+','+str(round(a[6],2))+','+str(round(a[7],2))+','+str(round(a[8],2))+','+str(round(a[9],2))+
          ','+str(round(a[10],2))+','+str(round(a[11],2))+','+str(round(a[12],2))+','+str(round(a[13],2))+','+str(round(a[14],2))+
          ','+str(round(a[15],2))+','+str(round(a[16],2))+','+str(a[17]))
          
    '''