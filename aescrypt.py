from PIL import Image 
import PIL
from Crypto.Cipher import AES
import hashlib
import binascii
import getpass

def encrypt(imagename,password):
    plaintext = list()
    plaintextstr = ""
    im = Image.open(imagename)  
    pix = im.load()
    
    width = im.size[0]
    height = im.size[1]
    
    for y in range(0,height):
        for x in range(0,width):
            plaintext.append(pix[x,y])
            
    for i in range(0,len(plaintext)):
        for j in range(0,3):
            plaintextstr = plaintextstr + "%d" %(int(plaintext[i][j])+100)
    relength = len(plaintext)
    
    plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"
    
    while (len(plaintextstr) % 16 != 0):
        plaintextstr = plaintextstr + "n"

    obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(plaintextstr)
    
    cipher_name = imagename + ".crypt"
    g = open(cipher_name, 'w')
    g.write(ciphertext)
    
    def construct_enc_image():
        asciicipher = binascii.hexlify(ciphertext)
        
    def replace_all(text, dic):
        for i, j in dic.iteritems():
            text = text.replace(i, j)
        return text

        reps = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
        asciiciphertxt = replace_all(asciicipher, reps)

        step = 3
        encimageone=[asciiciphertxt[i:i+step] for i in range(0, len(asciiciphertxt), step)]
        if int(encimageone[len(encimageone)-1]) < 100:
            encimageone[len(encimageone)-1] += "1"
        if len(encimageone) % 3 != 0:
            while (len(encimageone) % 3 != 0):
                encimageone.append("101")

        encimagetwo=[(int(encimageone[int(i)]),int(encimageone[int(i+1)]),int(encimageone[int(i+2)])) for i in range(0, len(encimageone), step)]    

        while (int(relength) != len(encimagetwo)):
            encimagetwo.pop()

        encim = Image.new("RGB", (int(width),int(height)))
        encim.putdata(encimagetwo)
   
        enc_success(cipher_name)
        
    construct_enc_image()
    
def decrypt(ciphername,password):  
    cipher = open(ciphername,'r')
    ciphertext = cipher.read()
    
    obj2 = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    decrypted = obj2.decrypt(ciphertext)
    decrypted = decrypted.replace("n","") 
   
    newwidth = decrypted.split("w")[1]
    newheight = decrypted.split("h")[1]
    
    heightr = "h" + str(newheight) + "h"
    widthr = "w" + str(newwidth) + "w"
    decrypted = decrypted.replace(heightr,"")
    decrypted = decrypted.replace(widthr,"")

    step = 3
    finaltextone=[decrypted[i:i+step] for i in range(0, len(decrypted), step)]
    finaltexttwo=[(int(finaltextone[int(i)])-100,int(finaltextone[int(i+1)])-100,int(finaltextone[int(i+2)])-100) for i in range(0, len(finaltextone), step)]    

    newim = Image.new("RGB", (int(newwidth), int(newheight)))
    newim.putdata(finaltexttwo)
    newim.show()

def encode(filename):
    pwd = getpass.getpass("Enter password: ")
    pwd= hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    pwd=pwd[0:32]
    try:
        encrypt(filename, pwd)
        print('Encrypted successfully')
    except:
        print("Could not encrypt.")

def decode(filename):
    pwd = getpass.getpass("Enter password: ")
    pwd= hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    pwd=pwd[0:32]
    try:
        decrypt(filename+".crypt", pwd)
        print('Decrypted successfully')
    except:
        print("Incorrect password.")
