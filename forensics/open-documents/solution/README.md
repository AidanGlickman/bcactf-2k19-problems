# Open Documents Writeup

## Nessecary Tools
* A `.zip` archive opener
* A file editor
* A Base64 decoder

## Procedure
Note that `.docx` files are just [zipped XML files](https://en.wikipedia.org/wiki/Office_Open_XML), as per [ISO/IEC 29500-1:2008](https://www.iso.org/standard/51463.html).
Unlike the older `.doc` files, these are literally just a bunch of [XML](https://en.wikipedia.org/wiki/XML) files, allowing you to unzip it and view the source.

1. Unzip the file `open.docx`.
1. Take a look through the contents. You should find the file `secrets.xml`. What could possibly be in this?
   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   PHNlY3JldCBmbGFnPSJiY2FjdGZ7ME94TWxfMXNfNG00ejFOZ30iIC8+
   ```
3. This string appears to be encoded in some way, so try decrypting it. You should find that this is a Base64 string, so put it through your favorite Base64 decoder to gt the flag.

## Flag
`bcactf{0OxMl_1s_4m4z1Ng}`

> write-up by: [**@edwfeng**](https://github.com/edwfeng)