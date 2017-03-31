from PIL import Image
import math
from keygen import *

image_path= 'Temp/castle.jpeg'
im = Image.open(image_path, "r")
arr = im.load() #pixel data stored in this 2D array
putpixel = im.im.putpixel
KEY= generate_tuples()
(W,H) = im.size

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
	print('Swap Successful')

#Send tuples here to automate
swap(1,1,1,2,im)
swap(1,3,5,6,im)

# im.show() #To display the image im	
im.save("Enc/"+image_path[5:-5]+"_en"+".jpeg")
im2 = Image.open(image_path, "r")

#To calculate efficiency of the algorithm
arr2= im2.load()
efficiency(arr2, arr)
