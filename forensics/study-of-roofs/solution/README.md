#  Writeup

## Necessary Tools
* [Foremost is a great forensics tool.](http://foremost.sourceforge.net/)

## Procedure
1. There are a few clues in this problem that all point to the same procedure for solving. 
	* If you took the first hint, you will see something about Greek. Roof in Greek is "stegi", which is a pretty telling hint. (Therefore the study of roofs would be stegiography, which is pretty close to steganography)
	* Even if you don't make the roof connection, there is a Stegosaurus on the roof.
1. All of those words connect to "steg" in some way, which is eluding to [Steganography](https://en.wikipedia.org/wiki/Steganography).
1. My steganography tool of choice is [Foremost](http://foremost.sourceforge.net/), but other tools like [Binwalk](https://github.com/ReFirmLabs/binwalk) would work for this problem as well.
1. Open your terminal of choice
1. Assuming you have Foremost installed, navigate to where the downloaded image is. (If it's in your downloads, `cd Downloads`)
1. Run `foremost -i dem_shingles.jpg` to have foremost take the image as an input file.
1. Foremost will generate a folder called `output` in whatever directory you are in. Open up the directory and in the `jpg` subdirectory, you will see an image. Open this image up and you see `bcactf{r4i53_7h3_r00f_liz4rd}`.

## Flag
`bcactf{r4i53_7h3_r00f_liz4rd}`

> write-up by: [**@aidanglickman**](https://aidanglickman.com)
