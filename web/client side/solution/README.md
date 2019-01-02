# Client Side MD5

## Procedure

This is a pretty basic problem. When we open the webpage, we can see that we need a password.
We can also notice that the page uses [client side](https://en.wikipedia.org/wiki/Client-side) [MD5](https://en.wikipedia.org/wiki/MD5).

MD5 is a [hashing algorithm](https://en.wikipedia.org/wiki/Hash_function) that is pretty widely used.
It takes the input and spits out a 128 character string.

When we take a look at the source code for the form, we have:
```html
<input type="submit" class="btn btn-lg btn-success btn-block" value="Log In" onclick="verify(); return False;">
```

When we take a closer look, at the javascript function `verify();`, we see:

```html
<script type="text/javascript">
    function verify() {
        checkpass = document.getElementById("password").value;
        if (md5(checkpass) == "c0b135c5e83da476bcb5eb9878bfbb23") {
            alert("Correct!");
        }
        else {
            alert("Incorrect password");
        }
    }
</script>
```

We could try to make a brute forcing algorithm.
But why would we do something so computationally expensive when we could just use someone else's work?

If we look online, we can find rainbow tables, where other people have compiled lists of hashes upon hashes.
