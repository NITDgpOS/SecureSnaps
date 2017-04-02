from PIL import Image
import math
from keygen import *
from utils import *

image_path= 'Temp/painting.png'
im = Image.open(image_path, "r")
arr = im.load() #pixel data stored in this 2D array
(W,H) = im.size
degree = int(input())
print(W,H)

KEY = generate_tuples(H,W)

for i in range(4):
	# ith Wave
	first= cascade(KEY[i][0:2],degree, W, H)
	second= cascade(KEY[i][2:],degree, W, H)
	automate_swap(first,second,degree+1,im,arr)

# im.show() #To display the image im	
im.save("Enc/"+image_path[5:-4]+"_en"+".png")
im2 = Image.open(image_path, "r")

#To calculate efficiency of the algorithm
arr2= im2.load()
efficiency(arr2, arr, W, H)
im.show()
