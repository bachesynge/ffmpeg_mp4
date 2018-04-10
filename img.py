#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image

def blend_two_images(names):
    img1 = Image.open( "/Users/mengyue/code/gif/img/"+names+".png")
    img1 = img1.convert('RGBA')
    '''
    img2 = Image.open("/Users/mengyue/code/img/111.jpg")
    img2 = img2.convert('RGBA')
    r,g,b,a = img2.split()

    img1.paste(img2, (34, 437), mask=a)

    img1.show()
    img1.save( "/Users/mengyue/code/img/1/"+names+".png")
    return
    '''
    img3 = Image.open( "/Users/mengyue/code/img/p2.png")
    img3 = img3.convert('RGBA')
    r,g,b,y = img3.split()

    img1.paste(img3, (200, 430), mask=y)
    #img1.show()
    img1.save( "/Users/mengyue/code/img/1/"+names+".png")
    return

#blend_two_images('t0')


t = 0
for i in range(0,111):
    names = 't'+str(i)
    print (names)
    blend_two_images(names)
