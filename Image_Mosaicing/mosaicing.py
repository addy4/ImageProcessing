# This code produces image mosaics
# The tiles are plain colored images . Their paths are shown below.
# The target image = grid of tiles * color matching with source image

import os
import numpy as np 
import cv2 

def read_file():
	s = cv2.imread('/Users/PremBhatia1/Desktop/picaz/children.jpeg')
	s = cv2.cvtColor(s,cv2.COLOR_BGR2LAB)
	t = cv2.imread('/Users/PremBhatia1/Desktop/picaz/sky.jpg')
	t = cv2.cvtColor(t,cv2.COLOR_BGR2LAB)
	return s, t

def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2))
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

def color_transfer(im1,im2):
		print("Converting picture"+"...")
		s, t = im1,im2 
		s_mean, s_std = get_mean_and_std(s)
		t_mean, t_std = get_mean_and_std(t)

		height, width, channel = s.shape
		for i in range(0,height):
			for j in range(0,width):
				for k in range(0,channel):
					x = s[i,j,k]
					x = ((x-s_mean[k])*(t_std[k]/s_std[k]))+t_mean[k]
				#	x = (x-s_mean[k])*((t_std[k]*0.7)/(s_std[k]*0.3))+t_mean[k]  
					# round or +0.5
					x = round(x)
					# boundary check
					x = 0 if x<0 else x
					x = 255 if x>255 else x
					s[i,j,k] = x

		s = cv2.cvtColor(s,cv2.COLOR_LAB2BGR)
		return s

def getpics():
    im1 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/blue.png')
    im1 = cv2.resize(im1,(25,25)) 
    im2 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/green.png')
    im2 = cv2.resize(im2,(25,25))
    im3 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/lightblue.png')
    im3 = cv2.resize(im3,(25,25))
    im4 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/lightpur.jpeg')
    im4 = cv2.resize(im4,(25,25))
    im5 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/maroon.png')
    im5 = cv2.resize(im5,(25,25)) 
    im6 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/mustard.png') 
    im6 = cv2.resize(im6,(25,25))
    im7 = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/skin.png')
    im7 = cv2.resize(im7,(25,25)) 
    return im1,im2,im3,im4,im5,im6,im7 

def grid():
    img1,img2,img3,img4,img5,img6,img7 = getpics()
    horiz1 = cv2.hconcat([img1,img2,img3,img4,img5,img6,img7,img1,img2,img3,img4,img5,img6,img7,img1,img2,img3,img4,img5,img6,img7,img1,img2,img3,img4,img5,img6,img7,img1,img2,img3,img4,img5,img6,img1,img2,img3,img4,img5,img6,img7]) 
    horiz2 = cv2.hconcat([img3,img4,img5,img6,img7,img1,img2,img3,img4,img1,img2,img3,img4,img5,img6,img7,img1,img2,img7,img3,img4,img5,img1,img6,img7,img2,img3,img4,img5,img6,img7,img1,img2,img3,img5,img6,img7,img1,img2,img4,img6])
    horiz3 = cv2.hconcat([img2,img3,img4,img1,img2,img6,img4,img5,img1,img5,img1,img2,img3,img4,img7,img1,img2,img3,img2,img4,img7,img6,img4,img5,img1,img6,img7,img1,img2,img3,img4,img5,img6,img7,img1,img2,img3,img5,img7,img4,img5])
    horiz4 = cv2.hconcat([img4,img1,img1,img2,img3,img4,img5,img7,img6,img4,img7,img1,img5,img1,img2,img6,img7,img1,img6,img5,img3,img4,img6,img7,img2,img5,img6,img7,img1,img2,img3,img4,img5,img6,img7,img5,img4,img2,img1,img3,img7]) 
    verti1 = cv2.vconcat([horiz1,horiz2,horiz3,horiz4]) 
    verti1 = cv2.vconcat([verti1,verti1]) 
    verti1 = cv2.vconcat([verti1,verti1]) 
    verti1 = cv2.vconcat([verti1,verti1]) 
    #verti1 = cv2.vconcat([verti1,verti1]) 
    verti1 = cv2.vconcat([horiz1,horiz2,horiz3,horiz4,verti1,horiz1,horiz2,horiz3,horiz4,horiz1,horiz2,horiz3,horiz4,horiz1,horiz2,horiz3,horiz4])
    final = verti1
    return final
    # 48 rows
    # 40 cols 
def matching():
    #grider = grid() 
    #cv2.imwrite('/Users/PremBhatia1/Desktop/picaz/newnow/gird.jpg',grider) 
    print("skip this")

matching() 
print("Done")
src = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/gird.jpg')
duplicated = src 
tar = cv2.imread('/Users/PremBhatia1/Desktop/picaz/newnow/painted.jpeg') 
tar = cv2.resize(tar, (1025,1200)) 
row = 0 
col = 0 
iter = 0
crawl = 0 
#row = 9999
#col = 9999
while(row < 48): 
    while(col < 40):
        print("in here") 
        ex_src = src[iter:iter + 25, crawl: crawl + 25] 
        ex_tar = tar[iter:iter + 25, crawl: crawl + 25]
        ex_src = cv2.cvtColor(ex_src,cv2.COLOR_BGR2LAB)
        ex_tar = cv2.cvtColor(ex_tar,cv2.COLOR_BGR2LAB) 
        imf = color_transfer(ex_src, ex_tar) 
        duplicated[iter:iter + 25, crawl: crawl + 25] = imf 
        crawl = crawl + 25
     #   cv2.imwrite('/Users/PremBhatia1/Desktop/picaz/random/z.jpeg',ex_src)
        col = col + 1
    iter = iter + 25 
    row = row + 1
    col = 0 
    crawl = 0

print("here")
cv2.imwrite('/Users/PremBhatia1/Desktop/picaz/newnow/resulting_b_for_repo.jpg',duplicated)

#im1 = cv2.imread('/Users/PremBhatia1/Desktop/seminar/pics for presentation/source.png')
#im2 = cv2.imread('/Users/PremBhatia1/Desktop/seminar/pics for presentation/target.png')
#im3 = cv2.imread('/Users/PremBhatia1/Desktop/seminar/pics for presentation/result.png')
#im1 = cv2.resize(im1, (500,500))
#im2 = cv2.resize(im2, (500,500))
#im3 = cv2.resize(im3, (500,500))
#cv2.imwrite('/Users/PremBhatia1/Desktop/picaz/newnow/hist1_for_repo.jpg',im1)
#cv2.imwrite('/Users/PremBhatia1/Desktop/picaz/newnow/hist2_for_repo.jpg',im2)
#cv2.imwrite('/Users/PremBhatia1/Desktop/picaz/newnow/hist3_for_repo.jpg',im3)

