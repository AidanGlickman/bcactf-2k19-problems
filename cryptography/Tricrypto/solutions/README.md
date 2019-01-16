# Tricrypto Writeup

## Necessary Tools
* [This ROT13 encoder/decoder](https://www.dcode.fr/rot-13-cipher) is useful for solving this problem.
* [This Hex, Decimal, Binary, and Octal Converter](https://www.rapidtables.com/convert/number/hex-dec-bin-converter.html) can be used to convert the numbers.

## Procedure
1. When you look at the subscripts, it says E, S, and R. "E" stands for Base 8 (**E**ight), "S" stands for Base 16 (**S**ixteen), and "R" stands for ROT13.
2. Using this information, you take the number that is given to you and convert it to Base 8.
3. Take the number from step 2 and convert it to Base 16.
4. Take the number from step 3 and decode it using the ROT13 decoder, and it reveals "galftcacb".
5. Wrap "galftcacb" and it should be "bcactf{galftcacb}".

Alternatively, you can use python to convert bases.
```python
>>> a = 100
>>> bin(a) # Converts an integer to binary
'0b1100100'
>>> oct(a) # Converts an integer to octal
'0o144'
>>> hex(a) # Converts an integer to hexadecimal
'0x64'
```
We can also convert back to base 10.
```python
>>> int('0b1100100', 2)
100
>>> int('0o144', 8)
100
>>> int('0x64', 16)
100
```

## Flag
`bcactf{galftcacb}`

> write-up by: **@eruuc**, **@edwfeng**
