#!/usr/bin/env python3
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
        print(f'Usage: {script} name.pptx or {script} -a')
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.pptx 1>/dev/null 2>&1'
        call(order,shell=True)

    if argv[1].endswith('.pptx'):
        order = f'libreoffice --invisible --convert-to pdf {argv[1]} 1>/dev/null 2>&1'
        call(order,shell=True)
    else:
        print('Error, file type does not match!')

def docx2pdf():
    argv = sys.argv
    if len(argv) < 2:
        script = basename(argv[0])
        print(f'Usage: {script} name.docx or {script} -a')
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.docx 1>/dev/null 2>&1'
        call(order,shell=True)

    if argv[1].endswith('.docx'):
        order = f'libreoffice --invisible --convert-to pdf {argv[1]} 1>/dev/null 2>&1'
        call(order,shell=True)
    else:
        print('Error, file type does not match!')

def xlsx2pdf():
    argv = sys.argv
    if len(argv) < 2:
        script = basename(argv[0])
        print(f'Usage: {script} name.docx or {script} -a')
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.xlsx 1>/dev/null 2>&1'
        call(order,shell=True)

    if argv[1].endswith('.xlsx'):
        order = f'libreoffice --invisible --convert-to pdf {argv[1]} 1>/dev/null 2>&1'
        call(order,shell=True)
    else:
        print('Error, file type does not match!')

if __name__ == '__main__':
    start = time.time()
    pptx2pdf()
    #docx2pdf()
    #xlsx2pdf()
    end = time.time()
    print('耗时：{end - start:.2f}(s)')
