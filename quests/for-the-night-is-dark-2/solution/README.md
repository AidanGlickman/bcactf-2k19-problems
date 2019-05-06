# For the Night is Dark 2 Writeup

## Necessary Tools
* This one is going to take some digging around in something like Chrome Developer Tools
* A good MD5 rainbow-table, as far as web-based solutions go [this one](http://www.md5decrypt.org/) is pretty solid.

## Procedure
1. We are given a link to a page with just a text input box and a submit button, so it would seem we need to guess the password to move on.
2. If we go in to Inspect Element, go over to the sources tab, navigate to `javascripts`, and click on `stage2.js`, we can see the code making this problem tick.
3. It seems we just need to find a code whose MD5 hash results in `3758002ab24653af8d550c0c50473098` and we will be redirected to a new webpage
4. If we put the hash in to our rainbow-table, we get `darknight`, so let's enter that in to our form!
5. Now we are redirected, and given the flag and our next challenge!

## Flag
`bcactf{7h37ru7h15411w3h4v3_dGhlIGxpZ2h0IGluIG91ciBleWVz}`

> made by: [**@aidanglickman**](https://aidanglickman.com)