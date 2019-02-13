# Corrupted PSD Writeup

## Necessary Tools
* An image viewer capable of viewing PSD files
* A text editor

## Procedure
Opening the [PSD file format specification](https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/#50577409_pgfId-1055726) and scrolling to the **File Header Section** reveals that all Photoshop files must begin with `8BPS` in order to be properly read. Opening `flag.psd` in a text editor shows that these bytes have been altered to `OOPS`. As such, the procedure is as follows:

1. Open `flag.psd` in a text editor.
2. Replace `OOPS` with `8BPS`.
3. Save `flag.psd` and open it in an image viewer, revealing the flag.

## Flag
`bcactf{corrupt3d_ph0705sh0p?_n0_pr0b5_1af4efb890}`

> write-up by: [**@anli5005**](https://anli5005.rocks)
