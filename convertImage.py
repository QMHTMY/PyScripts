#!/usr/bin/python
# -*- coding: utf-8 -*-
# 将当前目录的某图片格式图片改为另外一种并存储到文件格式命名的目录中。
# 如*.png 存储到PNG/目录，*.jpg 存储到JPG/目录

import os
import re
import sys
import click 
from PIL import Image

@click.command()
@click.option('--Itype', help="input image type (png,jpg,jpeg)")
@click.option('--Otype', help="output image type (png,jpg,jpeg)")
def changeType(Itype, Otype):
    '''改变图片的格式从Itype到Otype'''
    filePattn = re.compile(r'(.*)\.'+Itype)
    for Im in os.listdir('.'):
        matched = filePattn.search(Im)
        if matched:
            newName  = matched.group(1) + '.' + Otype
            imageObj = Image.open(matched.group(0))  
            imageObj.save(newName)
            imageObj.close()

@click.command()
@click.option('--Itype', help="image type (png,jpg,jpeg)")
def makeDir(Itype):
    '''创建以文件格式为名的目录'''
    Itypes = ['jpeg','jpg','png','gif','bmp']
    if Itype in Itypes:
        dirname = Itype.upper() 
        dirname += '/'
        if not os.path.exists(dirname):
            os.makedirs(dirname)
    else:
        print("Wrong picture type")
        sys.exit(-1)

    return dirname

if __name__ == "__main__":
    changeType()
