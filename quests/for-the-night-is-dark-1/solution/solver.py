#!/usr/bin/env python3

from PIL import Image
picture = Image.open("starmap.bmp")
pixels = picture.load()

width, height = picture.size

for i in range(height):
    for j in range(width):
        red = pixels[j,i][0]
        if red != 0:
            print(chr(red), end="")
print()