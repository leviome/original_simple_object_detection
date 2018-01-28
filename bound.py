import sobel
import numpy as np
import Image
LINE = 5
def bound(na,x0,y0,x1,y1):
	img_arr = na
	a,b,c = np.shape(img_arr)
	for i in range(b):
		for j in range(a):
			if (i>=x0 and i<=x0+LINE and j>=y0 and j<=y1) or (i>=x0 and i<=x1 and j>=y0-LINE and j<=y0)\
			 or (i>=x1-LINE and i<=x1 and j>=y0 and j<=y1) or(i>=x0 and i<=x1 and j>=y1-LINE and j<=y1):
				img_arr[j][i][0] = 255 
				img_arr[j][i][1] = 0
				img_arr[j][i][2] = 79
	img_after = Image.fromarray(img_arr)
	img_after.show()
	return img_after
def edge(img):
	na = sobel.main(img)
	a,b = np.shape(na)
	li = []
	lj = []
	for i in range(a):
		for j in range(b):
			if na[i][j] >= 200:
				li.append(i)
				lj.append(j)
	y0 = min(li)
	x0 = min(lj)
	y1 = max(li)
	x1 = max(lj)
	return x0,y0,x1,y1

def main():
	path = input('input picture : ')
	img = Image.open(path)
	x0,y0,x1,y1 = edge(img)
	na = np.array(img)
	bound(na,x0,y0,x1,y1)
	
main()
