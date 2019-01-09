# Basic Password 1

## Procedure

This problem is easily solved with a brute force attack, as there are only so many combinations of four numbers.
The command line usage for the program is `$ ./<file name> <passcode>`.

We can just make a python script that iterates through all of the possible codes from 0 to 9999.
We will use [subprocess](https://docs.python.org/3/library/subprocess.html) to call the program, and then check the result.
Theoretically, we could get subprocess to catch the output string, which is either `Incorrect passcode.` or `Congrats! ...`.
However, subprocess can give us the [exit code](https://en.wikipedia.org/wiki/Exit_status) without much hassle, so let's just use that.

Most programs return an exit code 0 upon a successful run.
So we can just have a `for` loop, counting up sequentially, until we get an error code of 0.
This means that the main part of our program could look something like this:

```python
NULL = open(os.devnull, "w")
result = 1
i = -1

while result == 1:
    i += 1
    result = subprocess.call(["compiled", str(i)], stdout=NULL, stderr=subprocess.STDOUT)
```

`os.devnull` is used here to get rid of the human-readable output.
`result` tracks the exit code, and will cause the while loop to break after it gets an exit key that isn't 1 (in our case, the only other exit code is 0).
`i` tracks the passcode currently being tried.

> write-up by: [**@edwfeng**](https://github.com/edwfeng)