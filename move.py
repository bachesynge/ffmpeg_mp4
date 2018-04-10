#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import re,datetime
from func import print_gif_path

path = '/Users/mengyue/Desktop/2.28/3/'
catch = 'nocatch/'
file_name='/Users/mengyue/Desktop/2.28/0301-1.txt'
mp4_name = '/Users/mengyue/Desktop/2.28/20180301_1.mp4'
file=open(file_name,'r')
begintimes = '1519887699658'
beginnum = ''


#切割首页mp4
ossystems = 'ffmpeg -y  -ss 0.000 -t 0.400 -i '+mp4_name+' -c:v libx264 -r 30 -s 360*640 -vprofile baseline -crf 22  -an  '+path+'0.mp4'
ossystem_h5 = 'ffmpeg -y  -ss 0.000 -t 0.400 -i '+mp4_name+' -c:v libx264 -r 30 -s 360*640 -vprofile baseline -crf 22  -an  '+path+'h50.mp4'
ossystem_wow = 'ffmpeg -y  -ss 0.000 -t 0.400 -i '+mp4_name+' -c:v libx264 -r 30 -s 720*1280 -vprofile baseline -crf 18 -an  '+path+'wow0.mp4'
os.system(ossystems)
os.system(ossystem_wow)
os.system(ossystem_h5)

def cut_m_mp4(mp4_url, btime, mp4_endname, s, t):

    #ts1 = mp4_endname+'1.ts'
    #ts2 = mp4_endname+'2.ts'
    #btime2 = btime+2.9
    ossystem_ts1  = 'ffmpeg -y  -ss '+str(btime)+' -t 0.400 -i '+mp4_url+' -c:v libx264 -r 30 -s "'+str(s)+'*'+str(t)+'"  -vprofile baseline -crf 22  -an '+mp4_endname
    #ossystem_ts1  = 'ffmpeg -y  -ss '+str(btime)+' -t 0.400 -i '+mp4_url+' -c:v libx264 -r 30 -s "'+str(s)+'*'+str(t)+'"  -vprofile baseline -crf 22  -an '+ts1
    #ossystem_ts2  = 'ffmpeg -y  -ss '+str(btime2)+' -t 0.001 -i '+mp4_url+' -c:v libx264 -r 30 -s "'+str(int(s*1.5))+'*'+str(int(t*1.5))+'"  -vprofile baseline -crf 22  -an '+ts2
    print (ossystem_ts1)
    #print (ossystem_ts2)
    os.system(ossystem_ts1)
    #os.system(ossystem_ts2)
    
    #time.sleep(1) 
    #oss = 'ffmpeg -y -i "concat:'+ts1+'|'+ts2+'" -c copy  '+mp4_endname
    #print (oss)
    #os.system(oss)

def cut_c_mp4(mp4_url, btime, mp4_endname, s):
    ossystem_mp4 = 'ffmpeg -y  -ss '+str(btime)+' -t 5.000 -i '+mp4_url+' -c:v libx264 -r 30 -s '+s+' -vprofile baseline -crf 22  -an '+mp4_endname
    print (ossystem_mp4)
    os.system(ossystem_mp4)

a = '1'
for (num,line) in enumerate(file):
    info = line.split('|')
    if(len(info)==4):
        #日志符合规则 进行剪切处理
        #开始截取时间
        btime = (float(info[0]) - float(begintimes))/1000
        x = info[1].split('.')
        y = info[2].split('.')
        urls = print_gif_path(int(x[0]),int(x[1]),int(y[0]),int(y[1]))
        cut_m_mp4(mp4_name, btime, path+str(urls)+'.mp4', 360, 640)
        cut_m_mp4(mp4_name, btime, path+'h5'+str(urls)+'.mp4', 360, 640)
        cut_m_mp4(mp4_name, btime, path+'wow'+str(urls)+'.mp4', 720, 1280)
    elif(len(info)==3):
        btime = (float(info[0]) - float(begintimes))/1000
        urls = info[1].replace('.','_')
        if float(info[1]) != float(a):
            a = info[1]
            cut_c_mp4(mp4_name, btime, path+catch+str(urls)+'.mp4', '360*640')
            cut_c_mp4(mp4_name, btime, path+catch+'h5'+str(urls)+'.mp4', '360*640')
            cut_c_mp4(mp4_name, btime, path+catch+'wow'+str(urls)+'.mp4', '720*1280')

