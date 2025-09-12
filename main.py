#Python Project for Encoding and decoding a message/text/secret in a Image Using LSB method
from PIL import Image
txt=input("Enter your txt: ")
bin = ''.join(format(ord(char), '08b') for char in txt)
print(bin)