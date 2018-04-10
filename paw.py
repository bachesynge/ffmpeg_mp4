#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import re,datetime
from func import print_gif_path

path = '/Users/mengyue/code/gif/14/nocatch/'
file_name='/Users/mengyue/Desktop/18/8c.txt'
mp4_name = '/Users/mengyue/Desktop/18end-2.mp4'
file=open(file_name,'r')
begintimes = ''
beginnum = ''

def cut_mp4(mp4_url, btime, mp4_endname, s):
    ossystem_mp4 = 'ffmpeg -y  -ss '+str(btime)+' -t 4.000 -i '+mp4_url+' -c:v libx264 -r 30 -s '+s+' -vprofile baseline -crf 23  -an '+mp4_endname
    print (ossystem_mp4)
    os.system(ossystem_mp4)
i = 0
for (num,line) in enumerate(file):
    info = line.split('|')
    if(len(info)==3):
        # 视频初始时间点
        if begintimes =='':
            # 视频初始时间点
            begintimes = info[0]
        btime = btime = (float(info[0]) - float(begintimes))/1000
        urls = info[1].replace('.','_')
        print num
        if (i % 2) == 0:
            cut_mp4(mp4_name, btime, path+str(urls)+'.mp4', '360*640')
            cut_mp4(mp4_name, btime, path+'h5'+str(urls)+'.mp4', '360*640')
            cut_mp4(mp4_name, btime, path+'wow'+str(urls)+'.mp4', '720*1280')
        i += 1
