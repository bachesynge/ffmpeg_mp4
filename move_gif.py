#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re,datetime
from func import print_gif_path

path = '/Users/mengyue/code/gif/2/'
file_name='/Users/mengyue/Downloads/move/1e.txt'
mp4_name = '/Users/mengyue/Downloads/move/move_1.mp4'
file=open(file_name,'r')
begintimes = ''
beginnum = ''
ossystems = 'ffmpeg -y  -ss 0.000 -t 0.001 -i '+mp4_name+' -c:v libx264 -r 29.97 -s 360*640 -vprofile baseline -crf 23  -an  '+path+'0.mp4'
ossystem_h5 = 'ffmpeg -y  -ss 0.000 -t 0.001 -i '+mp4_name+' -c:v libx264 -r 29.97 -s 360*640 -vprofile baseline -crf 23  -an  '+path+'h50.mp4'
ossystem_wow = 'ffmpeg -y  -ss 0.000 -t 0.001 -i '+mp4_name+' -c:v libx264 -r 29.97 -s 720*1280 -vprofile baseline -crf 18 -an  '+path+'wow0.mp4'
os.system(ossystems)
os.system(ossystem_wow)
os.system(ossystem_h5)
for (num,line) in enumerate(file):
    info = line.split('|')
    if(len(info)==4):
        if begintimes =='':
            # 视频初始时间点
            begintimes = info[0]
        #print (begintimes)
        #print ('--------------------------')
        #print info[0]
        #日志符合规则 进行剪切处理
        #开始截取时间
        btime = (float(info[0]) - float(begintimes))/1000
        cuttime = (float(info[3]) - float(info[0]))/1000
        #print(info[1],'---',info[2])
        x = info[1].split('.')
        y = info[2].split('.')
        urls = print_gif_path(int(x[0]),int(x[1]),int(y[0]),int(y[1]))
        #ossystem = '/usr/local/ffmpeg/bin/ffmpeg -y  -ss '+str(btime)+' -t '+str(cuttime)+ ' -i 2222.mp4 -f  gif '+path+str(urls)
        #ossystem = '/usr/local/ffmpeg/bin/ffmpeg -y  -ss '+str(btime)+' -t '+str(cuttime)+ ' -i 2222.mp4 -f  gif -r 15 -s 184*340 '+path+str(urls)
        #ossystem = '/usr/local/ffmpeg/bin/ffmpeg -y  -ss '+str(btime)+' -t '+str(cuttime)+ ' -i '+mp4_name+' -f  gif -s 294*512 '+path+str(urls)
        ###ossystem = '/usr/local/ffmpeg/bin/ffmpeg -y  -ss '+str(btime)+' -t '+str(cuttime)+ ' -i '+mp4_name+' -f  gif   '+path+str(urls)
        #ossystem = '/usr/local/ffmpeg/bin/ffmpeg -y  -ss '+str(btime)+' -t '+str(cuttime)+ ' -i '+mp4_name+' -f  gif  -r 10 -s 184*320 '+path+str(urls)
        ###ossystem2 = 'gif2webp '+path+str(urls)+' -o '+path+str(urls)+'.webp -q 20 -lossy -m 6'

        ossystem_mp4 = 'ffmpeg -y  -ss '+str(btime)+' -t 0.400 -i '+mp4_name+' -c:v libx264 -r 29.97 -s 360*640 -vprofile baseline -crf 23  -an '+path+str(urls)+'.mp4'
        ossystem_h5mp4 = 'ffmpeg -y  -ss '+str(btime)+' -t 0.400  -i '+mp4_name+' -c:v libx264 -r 29.97 -s 360*640 -vprofile baseline -crf 23 -an  '+path+'h5'+str(urls)+'.mp4'
        ossystem_wowmp4 = 'ffmpeg -y  -ss '+str(btime)+' -t 0.400  -i '+mp4_name+'  -c:v libx264 -r 29.97 -s 720*1280 -vprofile baseline -crf 18 -an '+path+'wow'+str(urls)+'.mp4'
        #ossystemmp4 = '/usr/local/ffmpeg/bin/ffmpeg -y  -ss '+str(btime)+' -t '+str(cuttime)+ ' -i '+mp4_name+'  -c copy  -f  mpegts   '+path+str(urls)+'.mp4'
        ###os.system(ossystem2)
        ###os.system(ossystem)

        os.system(ossystem_mp4)
        os.system(ossystem_h5mp4)
        os.system(ossystem_wowmp4)

        print (ossystem_h5mp4)
        print (ossystem_wowmp4)
        print (ossystem_mp4)
        #print('/usr/local/ffmpeg/bin/ffmpeg  -ss',btime,' -t ',cuttime, ' 111.mp4  git ', info[2], '.gif')
