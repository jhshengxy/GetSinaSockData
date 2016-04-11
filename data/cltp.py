#!/usr/bin/env python  
#encoding: utf-8
'''
处理停牌股票数据
2015年3月30日 14:41:05
by shengxy
'''
import os
import cons as cn
import tushare as ts


def reDate():
    print(u'初始化交易股票列表')
    reta=[]
    tpgp=[]
    try:
        fh=open(r'zcgp.txt')
        buf=fh.read()
        reta=buf.split(',')
        cn.JYGP=reta
        return 
    except Exception,ex:
        print(u'获取实时数据')
    
    gplist=cn.GPDMLB
    progress = psb.ProgressBar().start()
    totle=len(gplist)
    i=0.0
    tpcount=0
    for dm in gplist:
        #print(i/(totle-1.0)*100.0)
        progress.update((i/totle)*100.0)
        try:
            ts.get_realtime_quotes(dm)
            reta.append(dm)
        except Exception,ex:
            tpgp.append(dm)
            tpcount=tpcount+1
            
        i=i+1
    progress.finish()
    ifile=open(r'zcgp.txt','w')#写入的文件
    st=','.join(str(i) for i in reta)
    ifile.write(st)
    print(u'停牌股票处理完毕，共有：'+str(tpcount)+u'只股票停牌,'+str(len(reta))+u'只股票正常交易')
    
    cn.JYGP=reta
    cn.TPGP=tpgp
    
        
#获得正常交易的股票代码列表
def get_gplb():
    
    if len(cn.JYGP)<10:
        print(u'从文件获取到交易股票信息')
        reDate();
        return cn.JYGP
    else:
        #print(u'从内存获取到交易股票信息')
        return cn.JYGP
