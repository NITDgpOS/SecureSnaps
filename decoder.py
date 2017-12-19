from PIL import Image
from keygen import *
from utils import *
import argparse
import getpass


def decode(image_path,degree,pwd):
    try:
    	im = Image.open(image_path, "r")
    except FileNotFoundError:
    	print ('Image path is incorrect. Try again.')
    	exit(0)

    im = Image.open(image_path, "r")
    arr = im.load()  # pixel data stored in this 2D array
    (W, H) = im.size
    print(W, H)


    KEY = generate_tuples(H, W,pwd)

    for i in range(4):
        # ith Wave
        first = cascade(KEY[3 - i][0:2], degree, W, H)
        second = cascade(KEY[3 - i][2:], degree, W, H)
        automate_swap_dec(first, second, degree + 1, im, arr)

    color(arr,KEY[0][0:3],W,H)

    tokenized= image_path.split('.')
    saved_path= tokenized[0]+'_dec.'+tokenized[1]
    # im.show() #To display the image im
	im.save(saved_path)
    return (im,arr,saved_path)

def efficiency_calc(image_path,im,arr,saved_path):
    (W,H) = im.size
    im2 = Image.open(saved_path, "r")

    # To calculate efficiency of the algorithm
    arr2 = im2.load()
    efficiency(arr2, arr, W, H)
    im.show()


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='absolute/relative path to the image file')
    args = parser.parse_args()

    image_path = args.path

    if(image_path is None):
        print ('Please provide the path to image file. Try again.')
        exit(0)
    degree = int(input("Enter degree: "))
    pwd = getpass.getpass("Enter password: ")
    (im,arr,saved_path)=decode(image_path,degree,pwd)
    efficiency_calc(image_path,im,arr,saved_path)
