# Cookie Clicker Writeup

## Necessary Tools
* A web browser should be the only thing you need to use to solve this problem.

## Procedure
1. Analyze the source code (`cookie-clicker.js`), revealing that this Cookie Clicker game stores the number of cookies clicked in an HTTP cookie.
2. Set the `cookies` cookie to a large value (e.g. **1235193458612934857102938471923847**). A way to do this is as follows:
  * Open your browser's development tools, then type this in the JS console:
    ```javascript
    document.cookie = "cookies=102384701923847091283640912384609123485701923857"
    ```
3. Navigate to [the flag](http://localhost:5001/flag).
4. Profit! :tada:
