#!/usr/bin/env python3

from PIL import Image
import random
#picture = Image.open("base.bmp")
hiddentext = "http://rhllor.xyz/7h3fir31n0urh3ar75_d2VsY29tZSB0byBzdGVwIG9uZQ"
num = len(hiddentext)
picture = Image.new("RGB", (num,num), (0,0,0))
pixels = picture.load()
newPath = "out.bmp"
vals = []
for i in hiddentext:
    vals.append(ord(i))

for i,val in enumerate(vals):
    # pixels[0,i] = (val, pixels[0,i][1], pixels[0,i][2])
    pixels[random.randint(0,num-1),i] = (val, 0, 0)



picture.save(newPath)