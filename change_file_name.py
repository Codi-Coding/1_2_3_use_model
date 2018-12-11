import os
import glob
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

fpath2 = "toProcess/"
fpath2 = "original/"
start = 1000


for filename in os.listdir(fpath2):
	#if filename.find('png') == -1 :
	#os.rename(fpath + filename, fpath + str(start).zfill(6) + "_0.png")

	os.rename(fpath2 + filename, fpath2 + "_1" + str(start).zfill(5) + "_1.png")
	
	start += 1


