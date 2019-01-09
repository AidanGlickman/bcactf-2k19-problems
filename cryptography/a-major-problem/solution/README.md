# A Major Problem Writeup

## Necessary Tools
* [This Wikipedia page](https://en.wikipedia.org/wiki/Mnemonic_major_system) is useful for solving this problem.
* [This tool](https://www.browserling.com/tools/ascii-to-text) is also useful for solving this problem

## Procedure

This problem is a fairly simple cryptography problem, in the vein of stuff like Book Report from ctflearn.

It uses the Mnemonic Major System, which pairs each digit (0-9) to a sound or set of letters. For instance, '0' corresponds to an 'S', 'Z', or a soft 'C' (like "sizzle", "zoo", and "cipher", respectively). Some letters, notably all of the vowels, H, and Y) are left unassigned. This allows the encoding of numbers into words by finding the consonant sound of each digit and connecting them with unassigned letters.  

As an example, say we want to encode the number "123":
'1' = 'T or D'
'2' = 'N'
'3' = 'M'
So, we can use the word "*d*e*n*i*m*" to encode this number, as E and I are meaningless.

In this specific problem, the user is given a string of Mnemonic major system-encoded words. The words translate to a set of numbers, the ASCII character codes for the flag. The planned thought process for this problem is ideally something like this:

1. Research the words "Major" and "Mnemonic", finding resources about the Mnemonic Major System.
1. Translate the words either manually or with a tool.
1. Feed the numbers into an ASCII->Text converter, thus revealing the flag as `bcactf{g3t_g0t}`

## Flag
`bcactf{g3t_g0t}`

> write-up by: [**@natjef**](https://github.com/natjef)
