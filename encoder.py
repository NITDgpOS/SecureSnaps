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
extension=image_path.split('.')[-1]
	
try:
	im = Image.open(image_path, "r")
except FileNotFoundError:
	print ('Image path is incorrect. Try again.')
	exit(0)

im = Image.open(image_path, "r")
arr = im.load()  # pixel data stored in this 2D array
(W, H) = im.size
degree = int(input())
print(W, H)

KEY = generate_tuples(H, W)

for i in range(4):
    # ith Wave
    first = cascade(KEY[i][0:2], degree, W, H)
    second = cascade(KEY[i][2:], degree, W, H)
    automate_swap(first, second, degree + 1, im, arr)

# im.show() #To display the image im
im.save("Enc/" + image_path.split("/")[-1] + "_en.png")
im2 = Image.open(image_path, "r")

# To calculate efficiency of the algorithm
arr2 = im2.load()
efficiency(arr2, arr, W, H)
im.show()
