# A Manner of Thpeaking Writeup

## Necessary Tools
* It's pretty easy to script this, so for this writeup I will use python.
* An understanding of [LISP](https://en.wikipedia.org/wiki/Lisp_(programming_language)), specifically [CAR and CDR](https://en.wikipedia.org/wiki/CAR_and_CDR).

## Procedure
1. The problem statement is written with a lisp, which is a clue that we are going to do something with LISP.
	* We can also notice this by looking at the `inthtructhins.txt` or `printableth.txt` and seeing what they look like.
1. We can see that in `inthtructhins.txt` we dont just have `car` and `cdr`, but rather several [compositions](https://en.wikipedia.org/wiki/CAR_and_CDR#Compositions) of the two.
1. `printableth.txt` contains a LISP-like structure, but it isn't in a form that can just be parsed in to a LISP linked list.
	* One option here would be to clean this up and pass it to a real LISP language (assuming there is one that can handle compositions that long), but here I'm going to just script it quickly in Python.
1. When we take this in to python, we can start by cleaning up the `printableth` string, and turning it in to an array. This could be scripted but it's honestly faster to do by hand.
	* When this is done, we end up with an array something like this:

	``` python
	PRINTABLELIST = [" !\"#$%&'()*+,-./", "0123456789", ":;<=>?@", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "[\\]^_`", "abcdefghijklmnopqrstuvwxyz", "{|}~"]
	```

	* Here I pretty much just got rid of the escapes that were not necessary for python strings, and converted the LISP-like list structure to a python multi-dimensional list.
1. Next, I made the `inthtructhins` in to a list as well, so that I could easily traverse them.
1. To determine the indices of each letter, I stripped down each instruction, reversed the list (because compositions go from right to left), and split on the 'a' character in the middle to get my two numbers. From there, I could get the indices by simply looking at the length of the two list (to determine how many times I need to `cdr`), and just print the characters from there to reveal the flag!


## Flag
`bcactf{L157_8453d_pR0gR4Mm1nG_15_4w3S0Me!}`

> write-up by: [**@aidanglickman**](https://github.com/aidanglickman)
