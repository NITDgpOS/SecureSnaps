from PIL import Image
from keygen import *
from utils import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--path', help='absolute/relative path to the image file')
args = parser.parse_args()

image_path = args.path
if(image_path is None):
    print ('Please provide the path to image file. Try again.')
    exit(0)

try:
	im = Image.open(image_path, "r")
except FileNotFoundError:
	print ('Image path is incorrect. Try again.')
	exit(0)

im = Image.open(image_path, "r")
arr = im.load()  # pixel data stored in this 2D array
(W, H) = im.size
print(W, H)
degree = int(input())

KEY = generate_tuples(H, W)

for i in range(4):
    # ith Wave
    first = cascade(KEY[3 - i][0:2], degree, W, H)
    second = cascade(KEY[3 - i][2:], degree, W, H)
    automate_swap_dec(first, second, degree + 1, im, arr)

color(arr,KEY[0][0:3],W,H)
# im.show() #To display the image im
if "jpeg"in image_path or "jpg" in image_path:
	im.save("Dec/" + image_path.split("/")[-1] + "_dec.jpeg",format='JPEG',subsampling=0,quality=100)
else:
	im.save("Dec/" + image_path.split("/")[-1] + "_dec.png")
im2 = Image.open('Temp/painting.png', "r")

# To calculate efficiency of the algorithm
arr2 = im2.load()
efficiency(arr2, arr, W, H)
im.show()
