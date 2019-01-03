## How to Run
To run this problem, you'll need to download and install an up-to-date version of [Node.js](https://nodejs.org).

To install dependencies (required before you run the problem), use these commands:
```shell
$ cd path/to/cookie-clicker
$ cd source-code
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

## Files Included
* `index.js` - Node.js code that runs the HTTP server
* `package.json` - File used by NPM to download and install dependencies
* `config.json` - Contains configuration options used to run the problem *(see **Configuration**)*
* `static` - Folder containing the cookie clicker game itself
* `templates/shop.hbs` - Template used to generate the shop page
