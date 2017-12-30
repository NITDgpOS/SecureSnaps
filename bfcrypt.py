from PIL import Image 
import PIL
import getpass
from Crypto.Cipher import Blowfish
import numpy as np


def pad_string(str):
    new_str = str
    pad_chars = 8 - (len(str) % 8)

    if pad_chars != 0:
        for x in range(pad_chars):
            new_str += " "
        
    return new_str

def encrypt(imagename,password):
    img = Image.open( imagename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    H, W = len(data), len(data[0])
    print(H)
    print(W)
    pixelstring= ""
    for t in data:
        for p in t:
            for i in p:
                pixelstring= pixelstring + str(100+i)
    pixelstring= pixelstring+','+str(H)+','+str(W)
    
    crypt_obj = Blowfish.new(password, Blowfish.MODE_ECB)
    ciphertext = crypt_obj.encrypt(pad_string(pixelstring))

    cipher= open(imagename+'.crypt', 'w')
    cipher.write(ciphertext)
    
def decrypt(ciphername,password):  
    cipher= open(ciphername, 'r')
    ciphertext= cipher.read()

    crypt_obj = Blowfish.new(password, Blowfish.MODE_ECB)
    pixelstring= crypt_obj.decrypt(ciphertext)

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

    img = Image.fromarray(data, 'RGB')
    x= ciphername.split('.')
    img.save(x[0]+'_dec.'+x[-2])
    img.show()

def encode(filename):
    pwd = getpass.getpass("Enter password: ")
    try:
        encrypt(filename, pwd)
        print('Encrypted successfully')
    except:
        print("Could not encrypt.")

def decode(filename):
    pwd = getpass.getpass("Enter password: ")
    decrypt(filename+".crypt", pwd)
    
    # try:
    #     decrypt(filename+".crypt", pwd)
    #     print('Decrypted successfully')
    # except:
    #     print("Incorrect password.")
