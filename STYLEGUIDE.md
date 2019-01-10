## BCA CTF Problem Styleguide

* [Naming Conventions](#naming-conventions)
* [File Structure](#file-structure)
* [The Problem File](#the-problem-file)
* [The Flag](#the-flag)
* [The Writeup](#the-writeup)

### Naming Conventions

* Folders and files should be named in all lowercase, with words seperated by dashes
* Markdown files and other wiki-like or informational files should be named in all capitals with words stringing in to eachother with no seperations.

### File Structure

The folder for your problem should simply be the name of your problem, with the conventions outlined above. The folder structure should be as follows:

```
.
+-- README.md
+-- required-files
|	+-- [put-required-files-here]
+-- source-code
|	+-- [put-source-code-here-if-applicable]
+-- solution
|	+-- README.md
|	+-- tools
|	|	+-- [put-solver-files-here-if-applicable]

```

* Style for `README.md` is detailed [below](#the-problem-file).
* The directory `required-files` should contain all files that should be uploaded along with the problem, for example an image for a steganography problem.
* The directory `source-code` should contain source code for a problem that should **not** be uploaded along with the problem. This includes source files for web problems, uncompiled code for binary reverse problems, and so on.
	* If you need to include a compiled binary (for example if you are doing a binary reversal problem) please include it as a regular binary (for example a c program compiled with gcc) with no file extension and not something platform specific like a windows exe.
* The directory `solution` should contain a writeup and a `tools` folder with applicable tools, for example a script that may be useful for solving the problem.
	* Style for `solution/README.md` is detailed [below](#the-writeup).

> **NOTE:** When you are first submitting your problem, you do not have to have a writeup included. If you do not include a writeup and your problem is accepted, either you or one of the admins should add one later.

### The Problem File

`README.md` is the main file of your problem. It should be formatted as follows:

```markdown
# Problem Title

## Problem Statement
This is where you should put the message you want to appear with your problem.

## Hints (Optional)
* This is a hint to help if you are stuck
* This is another hint to help

## Flag
`bcactf{flag}`

> made by: [**@author**](https://github.com/author)

```

You do not need to include anything about the required files other than describe what they are in the problem statement if you want. Anything in the `required-files` folder will be uploaded with the problem as an attachment.

### The Flag

* Flags should generally be in the format `bcactf{flag}`. 
* I recommend putting flags in 1337speak so that they can't be guessed as easily, but that kind of stuff is really up to you. 
* Very rarely should the flag not be wrapped in `bcactf{}`, but sometimes this may be necessary, for example if the flag is hashed and can only be retrieved with a rainbow table. In this case please specify in the problem statement that the flag will not be wrapped in `bcactf{}` so that people don't get confused.

### The Writeup

`solution/README.md` should be an easy to follow step-by-step guide to solving the problem. It should detail the tools used to solve the problem, and the procedure.

The writeup should be as follows:

```markdown

# Problem Title Writeup

## Necessary Tools
* [This program/tool](link to tool) is useful for solving this problem
* [This program/tool](link to tool) is also useful for solving this problem

## Procedure
1. First you should realize that X
1. Second you should do Y. I did it using [TOOL]
1. Third you should do Z, revealing that the flag is `bcactf{flag}`

## Flag
`bcactf{flag}`

> write-up by: [**@author**](https://github.com/author)

```

>**NOTE**: The reason I use `1.` for every item of the list is so that you can go back and add intermediate steps later. Markdown viewers will take care of actually putting the correct numbers in.

Some useful things to include:

* Images of what your screen should look like at different points so that people can easily follow along.
* Commentary describing your thought process at different points while solving the problem.
* Links to websites that you used if applicable.
