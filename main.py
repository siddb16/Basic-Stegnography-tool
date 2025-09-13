#Python Project for Encoding and decoding a message/text/secret in a Image Using LSB method
from PIL import Image
import numpy as np

def txt_to_bin():
    txt=input("Enter your txt: ")
    bin = ''.join(format(ord(char), '08b') for char in txt)
    print(bin)
    return bin

# verifying the user defined function
# bin=txt_to_bin()
# print(bin)

def img_encode():
    # path=input("Enter the path of image to encodde:")
    img=Image.open("cute.png")
    # img.show()
    img_array=np.array(img)
    print(img_array)
    img_array[:,:,0]=(img_array[:,:,0] & 0xFE) | 1
    print(img_array)

img_encode()