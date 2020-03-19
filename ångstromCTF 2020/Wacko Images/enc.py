from numpy import *
from PIL import Image

##flag = Image.open(r"flag.png")
##img = array(flag)
##
##key = [41, 37, 23]
##
##a, b, c = img.shape
##
##for x in range (0, a):
##    for y in range (0, b):
##        pixel = img[x, y]
##        for i in range(0,3):
##            pixel[i] = pixel[i] * key[i] % 251
##        img[x][y] = pixel
##
##enc = Image.fromarray(img)
##enc.save('enc.png')


# Decrypt
enc = Image.open(r"enc.png")
img = array(enc)

key = [41, 37, 23]
a, b, c = img.shape # 200, 500, 4

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        #print(pixel)
        for i in range(0,3):
            #pixel[i] = pixel[i] * key[i] % 251
            for n in range(1, 255):
                if ((n * key[i]) % 251 == pixel[i]):
                    pixel[i] = n
                    break
        img[x][y] = pixel
        #print(pixel)

flag = Image.fromarray(img)
flag.save('enc_flag.png')
