from PIL import Image
import math
from keygen import *
from utils import *

image_path= 'Temp/castle.jpeg'
im = Image.open(image_path, "r")
arr = im.load() #pixel data stored in this 2D array
putpixel = im.im.putpixel
(W,H) = im.size
degree = int(input())
print(W,H)

def efficiency(orig, enco):
	different = 0
	for i in range(W):
		for j in range(H):
			if orig[i,j]!=enco[i,j]:
				different = different+1
	print('Different pixels: '+ str(different))
	print('Total pixels: '+ str(W*H))
	print('Efficiency: '+ str(different*100.0/(W*H)) +" %")


def swap(ai,aj,bi,bj, image):
	# Code to swap pixel RGB values
	temp= arr[ai,aj]
	arr[ai,aj]= arr[bi,bj]
	arr[bi,bj]= temp

def cascade(xy, N):
	cas= []
	cas.append((xy[0]%W,xy[1]%H))
	i= 0
	for i in range(N):
		xy= (function(xy[0])%W,function(xy[1])%H)
		cas.append(xy)
	return cas

def automate_swap(alpha, beta, N, image):
	for i in range(N):
		swap(alpha[i][0],alpha[i][1],beta[i][0],beta[i][1], image)

KEY = generate_tuples(H,W)

for i in range(4):
	# ith Wave
	first= cascade(KEY[i][0:2],degree)
	second= cascade(KEY[i][2:],degree)
	automate_swap(first,second,degree+1,im)

# im.show() #To display the image im	
im.save("Enc/"+image_path[5:-5]+"_en"+".jpeg")
im2 = Image.open(image_path, "r")

#To calculate efficiency of the algorithm
arr2= im2.load()
efficiency(arr2, arr)
im.show()
