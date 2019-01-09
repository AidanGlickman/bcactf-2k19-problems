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
If we feel like it, we can even chain these together.
```python
>>> hex(int('0o144', 8))
'0x64'
>>> bin(int(oct(int('0x64', 16)), 8))
'0b1100100'
```

The command `tr` (translate, available in UNIX-like systems) maps certain characters to other characters.
For example, `$ tr 'abc' 'xyz'` replaces any instances of `a` with `x`, any instanfces of `b` with `y`, and any instances of `c` with `z`.
We can also define ranges of values.
For eaxmple, `$ tr '[a-c]' 'xyz'` will do the same thing as before.
To end input, end the file with `Ctrl-D`.

We can also use redirection/pipes to apply this translation on the contents of a file.
If we had a file `hello.txt` with some data, we can read the contents of that file and send it to `tr` with `$ tr 'abc' 'xyz' < hello.txt`, or `$ cat hello.txt | tr 'abc' 'xyz'`.


## Flag
`bcactf{galftcacb}`

> write-up by: **@eruuc**, **@edwfeng**
