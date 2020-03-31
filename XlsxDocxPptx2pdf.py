#!/usr/bin/python3
# coding: utf-8
# Author: Shieber
# Date: 2019.10.12
# transfer pptx to pdf
# -a option means transfer all files in the current directory to pdf.

import sys
import time
from os.path import  basename 
from subprocess import call

def pptx2pdf():
    argv = sys.argv
    if len(argv) < 2:
        script = basename(argv[0])
        print('Usage: %s name.pptx or %s -a'%(script,script))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.pptx 1>/dev/null 2>&1'
        call(order,shell=True)

    if argv[1].endswith('.pptx'):
        order = 'libreoffice --invisible --convert-to pdf %s 1>/dev/null 2>&1'%argv[1]
        call(order,shell=True)
    else:
        print('Error, file type does not match!')

def docx2pdf():
    argv = sys.argv
    if len(argv) < 2:
        script = basename(argv[0])
        print('Usage: %s name.docx or %s -a'%(script,script))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.docx 1>/dev/null 2>&1'
        call(order,shell=True)

    if argv[1].endswith('.docx'):
        order = 'libreoffice --invisible --convert-to pdf %s 1>/dev/null 2>&1'%argv[1]
        call(order,shell=True)
    else:
        print('Error, file type does not match!')

def xlsx2pdf():
    argv = sys.argv
    if len(argv) < 2:
        script = basename(argv[0])
        print('Usage: %s name.docx or %s -a'%(script,script))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.xlsx 1>/dev/null 2>&1'
        call(order,shell=True)

    if argv[1].endswith('.xlsx'):
        order = 'libreoffice --invisible --convert-to pdf %s 1>/dev/null 2>&1'%argv[1]
        call(order,shell=True)
    else:
        print('Error, file type does not match!')

if __name__ == '__main__':
    start = time.time()
    pptx2pdf()
    #docx2pdf()
    #xlsx2pdf()
    end = time.time()
    print('耗时：%.2f(s)'%(end-start))
