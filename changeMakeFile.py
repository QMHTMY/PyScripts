#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 将当前目录中的某格式名改为另外一种。如 aa.html变成aa.txt
# 以当前目录中的某格式名新建同名新格式文件。 如由aa.c新建aa.txt

import re
import os
import click
import shutil

@click.command()
@click.option('--suffixS', default='html', help='suffix of source file')
@click.option('--suffixD', default='txt', help='suffix of destination file')
def changeName(suffixS, suffixD):
    filePattn = re.compile(r'(.*)\.'+suffixS)

    for fl in os.listdir('.'):
        matched = filePattn.search(fl)
        if matched:
            newName = matched.group(1) + '.' + suffixD
            shutil.move(fl, newName)

@click.command()
@click.option('--suffixS', default='html', help='suffix of source file')
@click.option('--suffixD', default='txt', help='suffix of destination file')
def makeNewFile(suffixS, suffixD):
    filePattn = re.compile(r'(.*)\.'+suffixS)

    for fl in os.listdir('.'):
        matched = filePattn.search(fl)
        if matched:
            newName = matched.group(1) + '.' + suffixD
            with open(newName,'w') as fobj: 
                pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 changeMakeFile.py --hlep")
        sys.exit(1)

    #changeName()
    #makeNewFile()
