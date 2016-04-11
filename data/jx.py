#!/usr/bin/env python  
#encoding: utf-8
'''计算均线'''
import data.cons as con
import os
import struct
import progressbar as psb
#import realData as data_rd
import time

basedir=r'F:\day' #保存数据的根目录


#输出结果
def outRes():
    outlist=[]
    for s_scode in con.GPDMLB:
        s_p=int(s_scode)
        '''if data_rd.sfpx[s_p]==False:
            outlist.append(s_scode)
    '''
    outlist.append(time.strftime('%H:%M:%S',time.localtime(time.time())))
    ifile=open(r'jx.txt','w')#写入的文件
    st=','.join(str(i) for i in outlist)
    ifile.write(st)    
    print(u'均线结果已输出'+time.strftime('%H:%M:%S',time.localtime(time.time())))

#xj：现价
#cjje：成交金额（当前时刻）
#cjss：成交手数（当前时刻）
#返回结果：如果计算出来的结果在均线范围内（价格不低于均线的-0.5%)，返回True，否则返回False

def jsxx(xj,cjje,cjss):
    #print(str(xj)+'---'+str(cjje)+'---'+str(cjss))
    if cjss==0:
        return True;
    
    jx=cjje/(cjss*1.0)
    cj=(xj-jx)/jx
    #print(u'均线'+str(round(jx,2))+u'现价'+str(xj)+u'差价'+str(cj))
    
    if cj>=-0.0025:
        return True;
    else:
        return False;
    


'''def rDatejx(scode,outstr):
    c_p=int(scode)
    if data_rd.sfpx[c_p]==False:
         a=struct.unpack('fffffffffffffffffffffffffff8s',outstr[len(outstr)-116:len(outstr)])
         #print(scode+'---'+str(a[3])+'QQQQQ'+str(a[4])+'BBBBB'+str(a[5]))
         if jsxx( round(a[2],2),round(a[6],2),round(a[5],2))==False  and a[5]>0 and a[3]!=a[4]:
            data_rd.sfpx[c_p]=True;
'''        
def wjjs(wjpath):
    #print(wjpath)
    ccc=open(wjpath,'rb')
    buf=ccc.read()
    s=0
    buf_len=len(buf)
    #是否破线标志
    sfpx=True;
    while (s+116)<=buf_len:
        a=struct.unpack('fffffffffffffffffffffffffff8s',buf[s:s+116])
        if jsxx( round(a[2],2),round(a[6],2),round(a[5],2))==False:
            sfpx=False
            break;
        
        s=s+116
        
        #if s>100000:
        #    break
    #成交手数大于0
    #排除一字涨停或者跌停的股票    
    if sfpx==True and a[5]>0 and a[3]!=a[4] :
        #print(a)
        print(u'未破线'+wjpath)
    
if __name__=='__main__':
    a=os.listdir('f:\\day\\2015-04-20')
    #wjjs('f:\\day\\2015-04-15\\601800.ss')
    progress = psb.ProgressBar().start()
    a_len=len(a)
    i=0.0
    for af in a:
        wjjs('f:\\day\\2015-04-20\\'+af)
        progress.update((i/a_len)*100.0)
        i=i+1;
    
    progress.finish()

