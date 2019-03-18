# The Flag is... Writeup

## Nessecary Tools
* Literally any text editor (eg. [Notepad++](https://notepad-plus-plus.org/))
* Ascii85 Decoder

## Procedure
1. Open the file in your text editor of choice.
1. Note that there are a few "objects", organized in a hierarchical manner. Each stores some information.
   * The one beginning `1 0 obj` appears to be the root of the object tree. 
   * The one beginning `4 0 obj` appears to set the font.
   * The one beginning `5 0 obj` appears to have something encoded. Let's try looking at this.
1. Note that right above the jumbled mess in `5 0 obj`, there is  `/Filter /ASCII85Decode`. This suggests that the text is encoded in [Ascii85](https://en.wikipedia.org/wiki/Ascii85). Run this through a decoder, and play around with it if it throws an error.

One thing to note is that there are two instances of `5 0 obj`. One is in the first section, the other is after the first `%%EOF`. This is known as an incremental update, and uses the latest version of any objects. This behavior allows us to hide information within a PDF, while not showing the user. 

## Flag
`bcactf{d0n7_4g3t_4b0u7_1nCr3Men74l_uPd473s}`

> write-up by: [**@edwfeng**](https://github.com/edwfeng)