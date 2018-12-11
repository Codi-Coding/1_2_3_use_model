import cv2
import numpy as np
import os

PROCESS_DIR = "toProcess/"
SEGMENT_DIR = "segment/"
OUTPUT_DIR = "output/"

flist = open("list.txt",'r').read().splitlines()
print(flist)

for imgname in flist:
	print(imgname)
	img1 = cv2.imread(PROCESS_DIR + imgname)
	#img3 = cv2.imread('_3.jpg')
	segmentimg = cv2.imread(SEGMENT_DIR + imgname[:-4] + "_vis.png")
	print(segmentimg)
	white_back = cv2.imread('back_white.png')

	img1 = cv2.resize(img1,(480,642), interpolation=cv2.INTER_AREA)
	segmentimg = cv2.resize(segmentimg,(480,642), interpolation=cv2.INTER_AREA)

	# 삽입할 이미지의 row, col, channel정보
	print(img1.shape)
	# 삽입할 이미지의 row, col, channel정보
	print(segmentimg.shape)


	#segmentimg = cv2.resize(segmentimg,(192,256))

	### segnment 바지 분리 및 resize / threshold 50~70 사이 값임 바지는


	seg_gray = cv2.cvtColor(segmentimg, cv2.COLOR_BGR2GRAY)
	seg_ret, seg_mask = cv2.threshold(seg_gray,126,255,cv2.THRESH_BINARY)

	mask_inv =cv2.bitwise_not(seg_mask)
	img_fg = cv2.bitwise_and(seg_gray,seg_gray,mask=mask_inv)

	seg_ret, seg_mask = cv2.threshold(img_fg,125,255,cv2.THRESH_BINARY)
	#re_seg = cv2.resize(seg_mask,(192,256), interpolation=cv2.INTER_AREA)

	mask_inv =cv2.bitwise_not(seg_mask)
	cv2.imshow('inv',mask_inv)
	###하얀색에 검은색 상품

	print(seg_mask.shape)


	#########



	img = cv2.bitwise_and(img1,img1,mask=seg_mask) #마스크는 1채널 값이여야함
	cv2.imshow('img1',img)
	####이거###

	img3gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret2, mask2 = cv2.threshold(img3gray,0,255,cv2.THRESH_BINARY)



	mask_inv2 =cv2.bitwise_not(mask2)




	img_bg = cv2.bitwise_and(white_back,white_back,mask=mask_inv)
	cv2.imshow('img_bg',img_bg)
	#백그라운드가 좀더 큼(검은색 남아있음)
	'''
	img_fg = cv2.bitwise_and(img,img,mask=seg_mask)
	cv2.imshow('img_fg',img1)
	'''
	print("###")
	print(white_back.shape)
	print(img.shape)
	dst = cv2.add(img_bg,img)
	cv2.imshow('1',dst)


	cv2.imshow('org2',dst)

	cv2.imwrite('preprocess.jpg', dst)

	save = str(OUTPUT_DIR) + str(imgname[:-6]) + "_1.jpg"
	cv2.imwrite(save, dst)

	#cv2.imshow('final',mask_inv2)

	#cv2.imwrite('final.jpg', mask_inv2)

	cv2.waitKey(0) # 키입력까지 대기
	cv2.destroyAllWindows()	
	

'''

######################2


mask_img = cv2.imread('mask.png')
cv2.imshow('two',mask_img)


img1 = cv2.imread('_1.png')
img3 = cv2.imread('_3.jpg')
segmentimg = cv2.imread('_5.png')

# 삽입할 이미지의 row, col, channel정보
print(img1.shape)
# 삽입할 이미지의 row, col, channel정보
print(img3.shape)


segmentimg = cv2.resize(segmentimg,(256,192))

### segnment 바지 분리 및 resize / threshold 50~70 사이 값임 바지는


seg_gray = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("segpos",seg_gray)
seg_ret, seg_mask = cv2.threshold(seg_gray,255,255,cv2.THRESH_BINARY)

mask_inv =cv2.bitwise_not(seg_mask)
img_fg = cv2.bitwise_and(seg_gray,seg_gray,mask=mask_inv)

seg_ret, seg_mask = cv2.threshold(img_fg,100,255,cv2.THRESH_BINARY)
re_seg = cv2.resize(seg_mask,(192,256), interpolation=cv2.INTER_AREA)

mask_inv =cv2.bitwise_not(re_seg)
cv2.imshow("pos",mask_inv)




print(re_seg.shape)
print(type(img1))

img = cv2.bitwise_and(img1,img1,mask=re_seg) #마스크는 1채널 값이여야함


img3gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret2, mask2 = cv2.threshold(img3gray,0,255,cv2.THRESH_BINARY)



mask_inv2 =cv2.bitwise_not(mask2)

img_bg = cv2.bitwise_and(dst,dst,mask=mask_inv)
cv2.imshow("bg",img_bg)

#백그라운드가 좀더 큼(검은색 남아있음)

img_fg = cv2.bitwise_and(img,img,mask=re_seg)
cv2.imshow("fg",img_fg)

dst2 = cv2.add(img_bg,img_fg)
print("final")
print(dst.shape)


cv2.imshow('final',dst2)

cv2.imwrite('final.jpg', dst2)

cv2.waitKey(0) # 키입력까지 대기
cv2.destroyAllWindows()

'''