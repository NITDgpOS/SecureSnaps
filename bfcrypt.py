import os
from PIL import Image 
import PIL
import math
import hashlib
import binascii
import getpass
import hashlib
from blowfish import *

def encrypt(imagename,password):
    
    
def decrypt(ciphername,password):  
    

def encode(filename):
    pwd = getpass.getpass("Enter password: ")
    encrypt(filename, pwd)
    # try:
    #     encrypt(filename, pwd)
    #     print('Encrypted successfully')
    # except:
    #     print("Could not encrypt.")

def decode(filename):
    pwd = getpass.getpass("Enter password: ")
    decrypt(filename+".crypt", pwd)
    # try:
    #     decrypt(filename+".crypt", pwd)
    #     print('Decrypted successfully')
    # except:
    #     print("Incorrect password.")
