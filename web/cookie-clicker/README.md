# Cookie Clicker
## Problem
My friend built a cookie clicker. How do I beat it?

## Hints
Here are some potential hints, in no particular order:
* Try looking at the source code. What does it reveal?
* What are cookies?

## Flag
The flag can be found in `config.json`. The default flag is:
```
bcaCTF{c00k13s_c71ck3d_34a2344d}
```

## Solution
Analysis of the source code (`cookie-clicker.js`) reveals that this Cookie Clicker game stores the number of cookies clicked in an HTTP cookie.

Therefore, a solution is as follows:
1. Set the `cookies` cookie to a large value (e.g. **1235193458612934857102938471923847**).
2. Navigate to [the flag](http://localhost:5001/flag).
3. Profit! :tada:

## How to Run
To run this problem, you'll need to download and install an up-to-date version of [Node.js](https://nodejs.org).

To install dependencies (required before you run the problem), use these commands:
```shell
$ cd path/to/cookie-clicker
$ npm install
```
NPM will download any dependencies that this problem requires and will install them in the `node_modules` directory. You only need to perform this step once.

To run this problem, run:
```shell
$ npm start
```

Once you're done, navigate to [localhost:5001](http://localhost:5001) to see the problem.

## Configuration
`config.json` contains a number of helpful config options, listed here:
* `port` - Controls which port the HTTP server will listen on (default: **5001**)
* `cookieThreshold` - How many cookies are needed to obtain the flag (default: 1e20)
* `flag` - The flag (default: `bcaCTF{c00k13s_c71ck3d_34a2344d}`)

## Required Files
* `index.js` - Node.js code that runs the HTTP server
* `package.json` - File used by NPM to download and install dependencies
* `config.json` - Contains configuration options used to run the problem *(see **Configuration**)*
* `static` - Folder containing the cookie clicker game itself
* `templates/shop.hbs` - Folder containing a template used to generate the shop page


> Problem submitted by [anli5005](https://github.com/anli5005)
