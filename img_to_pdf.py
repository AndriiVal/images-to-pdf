#! /usr/bin/python3.7
# -*- coding: utf-8 -*-

# Author: Andrii Valchuk

import os
import time

from wand.image import Image as wimg
from progress.bar import IncrementalBar

imgDir = input('Enter a directory of images: ')
fileName = input('Enter pdf file name: ')

filesList = os.listdir(imgDir)
fileList = []
for name in filesList:
    fullname = os.path.join(imgDir, name)
    if os.path.isfile(fullname) and (fullname.endswith('.jpg') or fullname.endswith('.png')):
        fileList.append(fullname)

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
