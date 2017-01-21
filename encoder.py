from PIL import Image
import math

image_path= 'Temp/castle.jpeg'
im = Image.open(image_path, "r")
arr = im.load() #pixel data stored in this 2D array

im.save("Enc/"+image_path[5:-5]+"_en"+".jpeg")
