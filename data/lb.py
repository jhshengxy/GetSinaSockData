#!/usr/bin/env python  
#encoding: utf-8
'''用于计算股票的量比，获取5天之前股票的平均成交量'''

import os;
import struct;
import progressbar as psb
import data.cons as cons

basedir=r'F:\day' #保存数据的根目录
cjllist=[0 for i in range(610000)]
jscs=[0 for i in range(610000)]
#处理文件夹中的文件
def getFile(d_dir):
    daylist=os.listdir(d_dir)
    
    progress = psb.ProgressBar().start()
    allcount=len(daylist)
    
    templist=[0 for i in range(610000)]
    i=0.0
    for k in daylist:
        
        
        #print(k[0:6])
        gpdm=int(k[0:6])
        
        #读取文件
        fh = open(d_dir+'\\'+k, 'rb')
        buf=fh.read()
        fh.close()
        #获取长度
        buf_len=len(buf)
        
        #获得手数,取最后一个数据节点
        b_str=buf[buf_len-116:buf_len]
        a=struct.unpack('fffffffffffffffffffffffffff8s',b_str)
        cjllist[gpdm]=cjllist[gpdm]+int(a[5])
        
        templist[gpdm]=int(a[5])
        #如果手数等于0，则说明该股票未交易
        if int(a[5])!=0:
            jscs[gpdm]=jscs[gpdm]+1
        #print(str(gpdm)+'---'+str(int(a[5])))
        #print(a)
        
        
        #根性进度条
        progress.update((i/allcount)*100.0)
        i=i+1;
        
    progress.finish()
    
    outlist=[]
    for dm in cons.GPDMLB:
        dm_sz=int(dm)
        
        outlist.append(dm);
        outlist.append(templist[dm_sz])
    
    ifile=open(d_dir+'\\sum.txt','w')#写入的文件
    st=','.join(str(i) for i in outlist)
    ifile.write(st)
    
    
    
#获取文件夹
def getdir():
    filelist=os.listdir(basedir)
    
    fp=len(filelist)
    kt=1
    while 1:
        nowfile=basedir+'\\'+filelist[fp-kt]
        sumfile=basedir+'\\'+filelist[fp-kt]+'\\sum.txt'
        #如果文件存在，直接从文件获取
        if os.path.exists(sumfile):
            print(111)
        else:
            getFile(nowfile)
        
        kt=kt+1
        print(nowfile)
        
        #取前五天的数据
        if kt>6:
            break;
        

    
if __name__=='__main__':
    getdir()