# File Headers Writeup

## Necessary Tools
* (HHD Hex Editor Neo) https://www.hhdsoftware.com/free-hex-editor is useful for editing the hex of the file.

## Procedure
1. First, you should realize that the file is unable to be recognized because the file header has been corrupted.
2. Second, you should edit the file with a hex editor (the one provided in tools is what I use) and change the first 16 hex digits so that it matches the PNG file header (89 50 4E 47 0D 0A 1A 0A)
3. Finally, you should open the image and the flag is displayed, revealing the flag to be 'bcactf{f1l3_h3ad3rs_r_c001}

## Flag
`bcactf{f1l3_h3ad3rs_r_c001}`

> write-up by: **@20nlevin**
