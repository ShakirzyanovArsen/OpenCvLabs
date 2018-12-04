#!/usr/bin/python3
import cv2
import sys
from os import path
import numpy as np

if sys.argv.__len__() < 3:
    print('Missing input and output file names')
    exit(1)
fileInPath = sys.argv[1]
fileOutPath = sys.argv[2]

if not path.exists(fileInPath) or not path.isfile(fileInPath):
    print('Invalid input file name')
    exit(1)
outDir = path.dirname(fileOutPath)
if not path.exists(outDir):
    print('Output file directory does\'t exists')
    exit(1)
image = cv2.imread(fileInPath, 0)
image = cv2.medianBlur(image, 3)
image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite(fileOutPath, image)
