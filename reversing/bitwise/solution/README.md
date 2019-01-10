# Bitwise Operations

## Procedure

We don't actually need to know too much about bitwise operations to reverse this problem.
All we need to know is that they take in an integer and give out an integer.

From this, we can see the general flow of the code:

1.  We prompt the user for a string
2.  We loop through each character in the string
    -   We convert each letter into its ASCII value using [ord(char)](https://docs.python.org/3/library/functions.html#ord)
    -   The converted int gets put through the following snippet: `((i ^ 100) | i ^ (i << 10)) ^ 134 + ((i >> 20) | i) ^ (i ** 5 + i)`
    -   We add the integer output to a list (of integers)
3.  Finally, we compare it to the expected output
    -   If it doesn't match, the program returns `Wrong`
    -   If it **does** match, the program returns `Success`

Knowing this, we can take the expected output and calculation snippet,
and build a program to find the correct input.

Here is the general flow we want in a solution:

1.  We loop through all of the items in the expected output
    -   We loop through a list made with `range(126)`, because 125 is the [ASCII code](http://man7.org/linux/man-pages/man7/ascii.7.html) for `}` and arrays are 0-indexed like any sane language
    -   We run each int through the original operation
    -   We check if the returned int is the same as the expected output
    -   If it is, we add the ASCII character to an output string with [chr(i)](https://docs.python.org/3/library/functions.html#chr)
2.  After we run through the list, we print the final output

We can then test the brute-forced output with the original program.

> write-up by: [**@edwfeng**]((https://github.com/edwfeng)