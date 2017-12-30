import os
from PIL import Image 
import PIL
import math
import hashlib
import binascii
import getpass
import hashlib
from blowfish import *
import numpy as np

def encrypt(imagename,password):
    img = Image.open( imagename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    print(data)
    H, W = len(data), len(data[0])
    print(H)
    print(W)
    pixelstring= ""
    for t in data:
        for p in t:
            for i in p:
                pixelstring= pixelstring + str(100+i)
    pixelstring= pixelstring+','+str(H)+','+str(W)

    pixelstring= enc_text(pixelstring, password)

    cipher= open(imagename.split('.')[0], 'w')
    cipher.write(pixelstring)
    # return pixelstring
    
def decrypt(ciphername,password):  
    cipher= open(ciphername, 'r')
    ciphertext= cipher.read()
    
    pixelstring= dec_text(ciphertext, password)
    x= pixelstring.split(',')
    H,W= int(x[-2]),int(x[-1])
    pixelstring= x[0]
    pixelstring= [int(pixelstring[i:i+3])-100 for i in range(0, len(pixelstring), 3)]

    data = np.zeros((H, W, 3), dtype=np.uint8)
    c= 0
    for i in range(H):
        for j in range(W):
            data[i,j]= pixelstring[c], pixelstring[c+1], pixelstring[c+2]
            c=c+3

    print(data)

def encode(filename):
    pwd = getpass.getpass("Enter password: ")
    print(encrypt(filename, pwd))
    # try:
    #     encrypt(filename, pwd)
    #     print('Encrypted successfully')
    # except:
    #     print("Could not encrypt.")

def decode(filename):
    pwd = getpass.getpass("Enter password: ")
    decrypt(filename.split('.')[0], pwd)
    # try:
    #     decrypt(filename+".crypt", pwd)
    #     print('Decrypted successfully')
    # except:
    #     print("Incorrect password.")
