#Python Project for Encoding and decoding a message/text/secret in a Image Using LSB method
from PIL import Image
txt=input("Enter your txt: ")
binary=bin(txt)
print(binary)
