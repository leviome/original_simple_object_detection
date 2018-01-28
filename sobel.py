import numpy as np
import Image
import math
def get_na(na):
	a,b = np.shape(na)
	na_new = np.zeros((a, b))
	for i in range(1,a-1):
		for j in range(1,b-1):
			na_new[i][j] = sobel(na[i-1][j-1],na[i-1][j],na[i-1][j+1],na[i][j-1],na[i][j],na[i][j+1],na[i+1][j-1],na[i+1][j],na[i+1][j+1])
	return na_new
			


def sobel(a0,a1,a2,a3,a4,a5,a6,a7,a8):
	sx = a0+2*a1+a2-(a6+2*a7+a8)
	sy = a0+2*a3+a6-(a2+2*a5+a8)
	return math.sqrt(pow(sx,2)+pow(sy,2))

def thin_pic(img):
	na = np.array(img)
	a,b,c= np.shape(na)
	no = np.zeros((a,b))
	for i in range(a):
		for j in range(b):
			no[i][j] = na[i][j][0]
	no_pic = Image.fromarray(no)
	return no_pic

THRES = 200
def binary(na):
	a,b = np.shape(na)
	#na_new = np.zeros((a, b))
	for i in range(a):
		for j in range(b):
			if na[i][j] >=THRES:
				na[i][j] = 255
			else:
				na[i][j] = 0
	return na

def main(img):
	img1 = thin_pic(img)
	na = np.array(img1)
	na1 = get_na(na)
	na2 = binary(na1)
	return na2
	#img_new = Image.fromarray(na2)
	#img_new.show()
#main()

if __name__ =='__main__':
	path = input('input pic : ')
	img = Image.open(path)
	na = main(img)
	img1 = Image.fromarray(na)
	img1.show()
