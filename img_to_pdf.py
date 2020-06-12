#! /usr/bin/python3.7
# -*- coding: utf-8 -*-

# Author: Andrii Valchuk

import os
import stat
import time
from wand.image import Image as wimg
from progress.bar import IncrementalBar

def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

imgDir = input('Enter a directory of images: ')

filesList = os.listdir(imgDir)
fileList = []
for name in filesList:
    fullname = os.path.join(imgDir, name)
    if os.path.isfile(fullname) and not has_hidden_attribute(fullname):
        fileList.append(fullname)

fileName = input('Enter pdf file name: ')

print('Start conversion, pleas wait...')

bar = IncrementalBar('Convert', max = len(fileList))
img = wimg()

try:
    for file in fileList:
        img.read(filename=file)
        converted = img.convert('pdf')
        converted.save(filename=fileName)
        bar.next()
        time.sleep(.1)
except Exception as ex:
    print('\nCannot convert image to pdf: %s', ex)

bar.finish()

print("Finish\n")
