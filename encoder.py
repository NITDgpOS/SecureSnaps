from PIL import Image
from keygen import *
from keygen_1 import *
from utils import *
import argparse
import getpass

def encode(image_path, pwd):
    extension=image_path.split('.')[-1]
    try:
        im = Image.open(image_path, "r")
    except FileNotFoundError:
        print ('Image path is incorrect. Try again.')
        exit(0)

    im = Image.open(image_path, "r")
    arr = im.load()  # pixel data stored in this 2D array
    (W, H) = im.size
    print(W, H)
    degree= int(0.36*W*H)

    KEY = generate_tuples(H, W, pwd)
    KEY1 = generate_tuples_1(H, W, pwd)

    for i in range(4):
        # ith Wave
        first = cascade(KEY[i][0:2], degree, W, H)
        second = cascade(KEY[i][2:], degree, W, H)
        automate_swap(first, second, degree + 1, im, arr)

    for i in range(4):
        # ith Wave
        first = cascade(KEY1[i][0:2], degree, W, H)
        second = cascade(KEY1[i][2:], degree, W, H)
        automate_swap(first, second, degree + 1, im, arr)

    color(arr,KEY[0][0:3],W,H)
    tokenized= image_path.split('.')
    saved_path= tokenized[0]+'_enc.'+tokenized[1]
    # im.show() #To display the image im
    im.save(saved_path)
    return (im,arr,saved_path)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='absolute/relative path to the image file')
    args = parser.parse_args()

    image_path = args.path

    if(image_path is None):
        print ('Please provide the path to image file. Try again.')
        exit(0)
    # degree = int(input("Enter degree: "))
    pwd = getpass.getpass("Enter password: ")
    (im,arr,saved_path)=encode(image_path, pwd)
    efficiency_calc(image_path,im,arr, saved_path)
