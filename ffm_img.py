#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


t = 0
c = 22
for i in range(1,90):
    t = str(i* 66)
    times = t.zfill(3)
    box = (0, 0, 112, 77)

    if int(t) < 1000:
        times = t.zfill(3)
        ffmpegs = 'ffmpeg -y -i /Users/mengyue/Desktop/3.19/c1.mp4  -f image2 -ss 0.'+str(times)+' -t 0.001  -r 1 /Users/mengyue/code/gif/img/t'+str(c)+'.png'
    else:
        a = t[0:1]
        b = t[1:4]
        ffmpegs = 'ffmpeg -y -i /Users/mengyue/Desktop/3.19/c1.mp4  -f image2 -ss '+a+'.'+b+' -t 0.001  -r 1 /Users/mengyue/code/gif/img/t'+str(c)+'.png'
    c +=1
    os.system(ffmpegs)
