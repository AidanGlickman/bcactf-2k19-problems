# Secret Code Writeup

## Necessary Tools

* Knowledge of a scripting language, for this writeup I will use Python.

## Procedure

1. This one is pretty straight forward. We are told exactly what to do, so let's just script it!  
2. The first step is obviously to open up the file, and since it would be nice to do some indice stuff (to split the first line from the others nicely) I decided to read it in to an array.

```python
with open("flag.txt", "r") as text:
    lines = text.read().splitlines()
```

3. Next, we can just set up some of our important variables, namely a string to hold our flag and our list of keys.
	* Because we are counting from 1 instead of 0, I wrote a little map function to turn all of our numbers at the top of the file in to integers and then decrement them to make our lives easier.

```python
flag = ""
keys = list(map(lambda num: int(num)-1, lines[0].split()))
```

4. Now, we get to the important part of searching for our numbers. 
	1. For this, we want to loop through every line except the first one with the numbers, check if the length is divisible by 3, and if there is no `&`.
	2. If this is true, we can `pop` the top number on the list and find that character in the line and add it to the flag.

```python
for line in lines[1::]:
    if len(line) % 3 == 0 and "&" not in line:
        flag += line[keys.pop(0)]
```

5. Finally, print out the flag!

```python
print(flag)
```

## Flag
`bcactf{f0110w_tH3_r00lz_<3_l0ve_m3_pls}`

> write-up by: [**@aidanglickman**](https://aidanglickman.com)
