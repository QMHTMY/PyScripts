#!/usr/bin/python3
# -*- coding: utf-8 -*-
# backup system files

import zipfile
import click
from os import walk
from os.path import abspath,basename,exists,join


@click.command()
@click.option('--folder', default='./', help='folder to backup')
@click.option('--storedir', default='/home/username/xxx/', help='folder for save')
def backupToZip(folder):
    folder = abspath(folder)
    number = 1
    while True:
        zipFilename = ''.join([basename(folder),'_',str(number),'.zip'])
        filename    = ''.join([storedir, zipFilename])
        if not exists(filename):
            break
        number += 1

    with zipfile.ZipFile(storedir,'w') as backupZip:
        for fd,subfd,fils in walk(folder):
            backupZip.write(fd)
            for fil in fils:
                if fil.startswith(basename(fd)+'_') and fil.endswith('.zip'):
                    continue
                backupZip.write(join(fd, fil))

if __name__ == "__main__":
    backupToZip()
