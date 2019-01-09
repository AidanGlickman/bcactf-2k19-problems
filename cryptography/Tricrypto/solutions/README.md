# Tricrypto Writeup

## Necessary Tools
* This ROT13 encoder/decoder [http://rumkin.com/tools/cipher/rot13.php] is useful for solving this problem.
* This Hex, Decimal, Binary, and Octal Converter [https://www.rapidtables.com/convert/number/hex-dec-bin-converter.html] can be used to convert the numbers.

## Procedure
1. When you look at the subscripts, it says E, S, and R. "E" stands for Base 8, "S" stands for Base 16, and "R" stands for ROT13.
2. Using this information, you take the number that is given to you and convert it to Base 8.[TOOL]
3. Take the number from step 2 and convert it to Base 16. `bcactf{flag}`
4. Take the number from step 3 and decode it using the ROT13 decoder, and it reveals "galftcacb".
5. Wrap "galftcacb" and it should be "bcactf{galftcacb}".

## Flag
`bcactf{galftcacb}`

> write-up by: **@[eruuc]**
