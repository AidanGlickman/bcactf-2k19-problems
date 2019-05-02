# For the Night is Dark 1 Writeup

## Necessary Tools
* Image processing skills, I will be doing this writeup with Python and [PIL](https://pythonware.com/products/pil/)
* I guess you could also do it by hand in photoshop or something but that seems slow

## Procedure
1. The first thing we can notice is that the "stars" are each single pixels of varying red brightnesses. We are told in the hint that this puzzle has one star per row, and that the order is top to bottom.
2. Seeing this, we can determine that we probably want to extract the values of those "stars," and see what they might mean. That can be done with some code like this:

```python
from PIL import Image
picture = Image.open("starmap.bmp")
pixels = picture.load()

width, height = picture.size

for i in range(height):
    for j in range(width):
        red = pixels[j,i][0]
        if red != 0:
            print(red)
```

3. This gets us a string of numbers, all of which look like they are in the ascii range! So, if we just modify our code to have the print statement give us the character representations, that might get us somewhere.

```python
print(chr(red), end="")
```

4. Interesting, now we get a url. If we navigate to the URL, we get the flag, and our next challenge!

## Flag
`bcactf{gu1d3d_8y_574r5_QmVnaW5uaW5ncw}`

> write-up by: [**@aidanglickman**](https://aidanglickman.com)
