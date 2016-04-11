#!/usr/bin/env python  
#encoding: utf-8

#分价表信息

import pandas as pa
import numpy as np
import struct
import time
import os
def tjfjb(wjpath):
    #读取单个文件信息
    ccc=open(wjpath,'rb')
    buf=ccc.read()
    alldata=[]
    xj=[]           #股票价格
    cjl=[]          #成交量
    sj=[]
    s=0
    stime=time.time()
    bulen=len(buf)
    while (s+116)<=bulen:
        a=struct.unpack('fffffffffffffffffffffffffff8s',buf[s:s+116])
        #print(struct.unpack('fff8s',buf[20:40]))
        #print(struct.unpack('fff8s',buf[40:60]))
        s=s+116
        alldata.append(a)
    
    
    alen=len(alldata)
    st=1
    while st<alen:
        xj.append(round(alldata[st][2],2))
        sj.append(alldata[st][27])
        bt=st-1
        if bt>1:
            cjl.append(alldata[st][5]-alldata[bt][5])  
        else:
            cjl.append(0)
        
        #print(str(xj[st-1])+'--'+str(cjl[st-1])+'--'+str(alldata[st][5])+'--'+str(alldata[st-1][5])+'--'+sj[st-1])
        st=st+1
    data={'xj':xj,'cjl':cjl}
    myframe=pa.DataFrame(data)
    
    myframeGrouped=myframe.groupby('xj')
    #print(myframeGrouped.sum())
    
    endtime=time.time()
    
    #print(endtime-stime)



def tjfjb2(wjpath):
    
    ccc=open(wjpath,'rb')
    buf=ccc.read()
    alldata=[]
    xj=[]           #股票价格
    cjl=[]          #成交量
    sj=[]
    jghash=[0 for i in range(40000)]
    lowprice=999999.0
    highprice=0.1
    
    s=0
    stime=time.time()
    bulen=len(buf)
    while (s+116)<=bulen:
        a=struct.unpack('fffffffffffffffffffffffffff8s',buf[s:s+116])
        #print(struct.unpack('fff8s',buf[20:40]))
        #print(struct.unpack('fff8s',buf[40:60]))
        s=s+116
        alldata.append(a)
    
    
    alen=len(alldata)
    st=1
    while st<alen:
        gpprice=int(alldata[st][2]*100) #所有的股价都是精确到小数点后两位，所以乘以100就可以转换为整数
        #print(int(gpprice))
        if gpprice==0:
            st=st+1
            continue
        if gpprice<lowprice:
            lowprice=gpprice
        
        if gpprice>highprice:
            highprice=gpprice
        jghash[gpprice]=jghash[gpprice]+alldata[st][5]
        
        st=st+1
        
    s=lowprice
    while s<=highprice+1:
        t=s/100.0
        #print(str(t)+'---'+str(jghash[s]))
        s=s+1
               
if __name__=='__main__':   
    a=os.listdir('f:\\day\\2015-04-02')
    stime=time.time()
    #tjfjb2('f:\\day\\2015-04-03\\000045.ss')
    for af in a:
        #tjfjb2('f:\\day\\2015-04-03\\'+af)
        tjfjb('f:\\day\\2015-04-02\\'+af)

    etime=time.time()
    print('方法1:'+str(etime-stime))
    
    stime=time.time()
    for af in a:
        tjfjb2('f:\\day\\2015-04-02\\'+af)
        #tjfjb('f:\\day\\2015-04-03\\'+af)        
        
    etime=time.time()
    print('方法2:'+str(etime-stime))
    