# Cookie Clicker Writeup

## Necessary Tools
* A web browser should be the only thing you need to use to solve this problem.
* Optionally, an extension like [this](http://www.editthiscookie.com/) can be used to make the problem even easier.

## Procedure
#### The Short Way
 1. With [EditThisCookie](http://www.editthiscookie.com/) installed on your browser, open up the page, and get started by clicking the cookie once.
 1. Open EditThisCookie, and set the `cookies` field to a ridiculous number (e.g. **1235193458612934857102938471923847**).
 1. Open the shop and buy the flag, revealing it in plaintext.
#### The Long Way
 1. Analyze the source code (`cookie-clicker.js`), revealing that this Cookie Clicker game stores the number of cookies clicked in an HTTP cookie.
 1. Set the `cookies` cookie to a large value (e.g. **1235193458612934857102938471923847**). A way to do this is as follows:
   * Open your browser's development tools, then type this in the JS console:
     ```javascript
     document.cookie = "cookies=102384701923847091283640912384609123485701923857"
     ```
 1. Navigate to [the flag](http://localhost:5001/flag), revealing the flag in plain text.
 1. Profit! :tada:

> write-up by: [**@edwfeng**](https://github.com/edwfeng) and [**@aidanglickman**](https://github.com/aidanglickman)
