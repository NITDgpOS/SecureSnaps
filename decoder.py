from PIL import Image
import math
from keygen import *
from utils import *

image_path= 'Enc/colors_en.jpeg'
im = Image.open(image_path, "r")
arr = im.load() #pixel data stored in this 2D array
putpixel = im.im.putpixel
(W,H) = im.size
degree = int(input())
print(W,H)

KEY = generate_tuples(H,W)

for i in range(4):
	# ith Wave
	first= cascade(KEY[3-i][0:2],degree, W, H)
	second= cascade(KEY[3-i][2:],degree, W, H)
	automate_swap_dec(first,second,degree+1,im,arr)

# im.show() #To display the image im	
im.save("Dec/"+image_path[4:-8]+"_dec"+".jpeg")
im2 = Image.open(image_path, "r")

#To calculate efficiency of the algorithm
arr2= im2.load()
efficiency(arr2, arr, W, H)
im.show()
