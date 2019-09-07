import os
import glob
from scipy.misc import imresize
import cv2

"""
s

"""
""" 
denim 000001 - 000398
leather 000399 - 000466
pencil 000467 - 000981
long 000982 - 001293
mini 001294 - 002222
aline 002223 - 003751
pleated 003752 - 003986



"""

fpath2 = "./input/"
outpath = "./output/"
start = 1000


for filename in os.listdir(fpath2):
	#if filename.find('png') == -1 :
	#os.rename(fpath + filename, fpath + str(start).zfill(6) + "_0.png")

	os.rename(fpath2 + filename, fpath2 + str(start).zfill(5) + ".png")
	
	
	
	
	start += 1


