#!/usr/bin/env python  
#encoding: utf-8
import tushare as ts
import time
import os
import pandas as pa
import data.cltp as cp
import struct

#判断时间是否发生变化
oldv=['00:00:00' for i in range(610000)]
#保存输出字符
outlen=['' for i in range(610000)]

#快速判断该股票是否破过均线
sfpx=[False for i in range(610000)]

filepath=r'c:/day/'
rq=''

jxsc=time.time();

is_stop=False

def getFloat(str_ft):
    ret=0.0
    try:
        ret=float(str_ft)
    except Exception,ex:
        ret=0.0
    
    return ret

#获取某个时刻实施的股票交易数据
def getRealData_sk(): 
    klist=cp.get_gplb()
    tempnum=0
    templist=[]
    partdf=[]
    alldf=[]
    for k in klist:
        tempnum=tempnum+1
        templist.append(k)
        if tempnum==200:
            try:
                df = ts.get_realtime_quotes(templist)
                partdf.append(df)
                tempnum=0
                templist=[]
            except Exception:
                print(u'数据读取超时，结束线程')
                realDate_stop()
                '''
                df = ts.get_realtime_quotes(templist)
                partdf.append(df)
                tempnum=0
                templist=[]
                '''
    
    #把最后的数据加入
    try:
        partdf.append(ts.get_realtime_quotes(templist))
        alldf=pa.concat(partdf)
    except Exception:
        print(u'最后数据读取超时，结束线程')
        realDate_stop()
        
        
    return alldf

def xrwj(wfilepath,wlin,s_code):
    
    #先判断文件是否存在，如果文件存在则直接添加到末尾，不存在则新建
    if os.path.exists(wfilepath):
        binfile=open(wfilepath,'ab')
    else:
        binfile=open(wfilepath,'wb')
        
    binfile.write(wlin)
    binfile.close
    print(s_code+u'数据已写入')    

#列表计算，如果内存中时间与读取的时间不一致，则认为这是新数据。
#则把字符串写入到内存中，如果字符串长度超过5000则写入到文件中
def jssj(s_open,s_pre_close,s_price,s_high,s_low,s_v,s_a,b1_v,b1_p,b2_v,b2_p,b3_v,b3_p,b4_v,b4_p,b5_v,b5_p,b6_v,b6_p,b7_v,b7_p,b8_v,b8_p,b9_v,b9_p,b10_v,b10_p,rq,s_sj,s_code):
    k_p=int(s_code)
    
    #如果数组中的时间不一致，则写入新内容
    if oldv[k_p]!=s_sj:
        oldv[k_p]=s_sj
        outlen[k_p]=outlen[k_p]+struct.pack('fffffffffffffffffffffffffff8s',float(s_open),float(s_pre_close),float(s_price),float(s_high),float(s_low),float(s_v),float(s_a),float(b1_v),float(b1_p),float(b2_v),float(b2_p),float(b3_v),float(b3_p),float(b4_v),float(b4_p),float(b5_v),float(b5_p)
                                            ,float(b6_v),float(b6_p),float(b7_v),float(b7_p),float(b8_v),float(b8_p),float(b9_v),float(b9_p),float(b10_v),float(b10_p),str(s_sj))
        
        #长度为500时，写入文件。其他情况都保存在内存中
        if len(outlen[k_p])>1000:
            xrwj(filepath+rq+'/'+s_code+'.ss',outlen[k_p],s_code)
            
            '''global jxsc
            #计算均线
            jx.rDatejx(s_code, outlen[k_p])
            tempTime=time.time()-jxsc
            #print('-----------------'+str(tempTime))
            
            #每隔10分钟输出一次均线结果
            if tempTime>10:
                jx.outRes()
                
                jxsc=time.time()
            '''    
            outlen[k_p]=''
            
    ###x下面方法为测试使用        
    '''else:
        oldv[k_p]=s_sj
        outlen[k_p]=outlen[k_p]+struct.pack('fffffffffffffffff8s',float(s_open),float(s_pre_close),float(s_price),float(s_high),float(s_low),float(s_v),float(s_a),float(b1_v),float(b1_p),float(b2_v),float(b2_p),float(b3_v),float(b3_p),float(b4_v),float(b4_p),float(b5_v),float(b5_p),str(s_sj))
        
        #长度为500时，写入文件。其他情况都保存在内存中
        if len(outlen[k_p])>760:
            xrwj(filepath+rq+'/'+s_code+'.ss',outlen[k_p],s_code)
            outlen[k_p]=''
    '''
    

#停止程序，并将数据取出
def realDate_stop():
    count=0
    allcode='000000'
    dirname=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    for out1 in outlen:
        if len(str(count))<6:
            c_temp=6-len(str(count))
            gp_code=allcode[0:c_temp]+str(count)
        else:
            gp_code=str(count)
        if len(out1)>10:
            xrwj(filepath+dirname+'/'+gp_code+'.ss',out1,gp_code)
            outlen[count]=''
            
        count=count+1
    #退出
    print(u'线程已停止')
    
    print(u'暂停5秒')
    time.sleep(5)
    realDate_main()
    #exit(1)
    #thread.exit_thread()


#生成文件夹
def scwjj():
    dirname=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if os.path.exists(filepath+dirname)!=True:
        os.makedirs(filepath+dirname)
        kk=dirname
        print(u'生成文件夹')   
        
def realDate_start():

    scwjj()    
    global jxsc
    jxsc=time.time();
    #循环调用方法
    while 1:
        a=time.strftime('%H:%M:%S',time.localtime(time.time()))
        if (a>'09:14:48' and a<'11:31:00') or (a>'12:59:50' and a<'15:01:00'):
             realDate_main()
             
             if is_stop:
                 realDate_stop()
        else:
            time.sleep(10)
            print(a)
            print(u'未开市，暂停10秒') 
            scwjj()

                
def realDate_main():
    
    #初始化时，两个数组的datafr
    stime=time.time()
    newdf=getRealData_sk()
    df_len=len(newdf)
    count=0
    
    while 1:
        
        if count>=df_len:
            break;
        
        '''
                DataFrame 实时交易数据
              属性:0：name，股票名字
            1：open，今日开盘价
            2：pre_close，昨日收盘价
            3：price，当前价格
            4：high，今日最高价
            5：low，今日最低价
            6：bid，竞买价，即“买一”报价
            7：ask，竞卖价，即“卖一”报价
            8：volumn，成交量 maybe you need do volumn/100
            9：amount，成交金额（元 CNY）
            10：b1_v，委买一（笔数 bid volume）
            11：b1_p，委买一（价格 bid price）
            12：b2_v，“买二”
            13：b2_p，“买二”
            14：b3_v，“买三”
            15：b3_p，“买三”
            16：b4_v，“买四”
            17：b4_p，“买四”
            18：b5_v，“买五”
            19：b5_p，“买五”
            20：a1_v，委卖一（笔数 ask volume）
            21：a1_p，委卖一（价格 ask price）
            ...
            30：date，日期；
            31：time，时间；
            '''
        rq=newdf.iat[count,30]
        ofilename=newdf.iat[count,32]
        
        s_open=getFloat(newdf.iat[count,1])
        s_pre_close=getFloat(newdf.iat[count,2])
        s_price=getFloat(newdf.iat[count,3])
        s_high=getFloat(newdf.iat[count,4])
        s_low=getFloat(newdf.iat[count,5])
        s_v=getFloat(newdf.iat[count,8])
        s_a=getFloat(newdf.iat[count,9])
        
        b1_v=getFloat(newdf.iat[count,10])
        b1_p=getFloat(newdf.iat[count,11])
        b2_v=getFloat(newdf.iat[count,12])
        b2_p=getFloat(newdf.iat[count,13])  
        b3_v=getFloat(newdf.iat[count,14])
        b3_p=getFloat(newdf.iat[count,15])        
        b4_v=getFloat(newdf.iat[count,16])
        b4_p=getFloat(newdf.iat[count,17])
        b5_v=getFloat(newdf.iat[count,18])
        b5_p=getFloat(newdf.iat[count,19])
        
        b6_v=getFloat(newdf.iat[count,20])
        b6_p=getFloat(newdf.iat[count,21])
        b7_v=getFloat(newdf.iat[count,22])
        b7_p=getFloat(newdf.iat[count,23])
        b8_v=getFloat(newdf.iat[count,24])
        b8_p=getFloat(newdf.iat[count,25])
        b9_v=getFloat(newdf.iat[count,26])
        b9_p=getFloat(newdf.iat[count,27])
        b10_v=getFloat(newdf.iat[count,28])
        b10_p=getFloat(newdf.iat[count,29])
        
        
        jssj(s_open,s_pre_close,s_price,s_high,s_low,s_v,s_a,b1_v,b1_p,b2_v,b2_p,b3_v,b3_p,b4_v,b4_p,b5_v,b5_p,b6_v,b6_p,b7_v,b7_p,b8_v,b8_p,b9_v,b9_p,b10_v,b10_p,rq,newdf.iat[count,31],ofilename)
        
        #将内存中的数据输出到文件
        
        #bytes=struct.pack('fffffffffffffffff8s',float(s_open),float(s_pre_close),float(s_price),float(s_high),float(s_low),float(s_v),float(s_a),float(b1_v),float(b1_p),float(b2_v),float(b2_p),float(b3_v),float(b3_p),float(b4_v),float(b4_p),float(b5_v),float(b5_p),str(newdf.iat[count,31]))
        #xrwj(filepath+rq+'/'+ofilename+'.ss',bytes)
        #binfile=open(filepath+ofilename+'.ss','wb')
        #binfile.write(bytes)
        #binfile.close
         
        count=count+1
        #print(count)
        
        
         
    etime=time.time()
    hs=etime-stime
    print(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))+u'数据处理完毕，耗时'+str(hs))
    
