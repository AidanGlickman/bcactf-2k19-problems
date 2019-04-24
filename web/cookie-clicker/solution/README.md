# Cookie Clicker Writeup

## Necessary Tools
* A web browser should be the only thing you need to use to solve this problem.
* Optionally, an extension like [this](http://www.editthiscookie.com/) can be used to make the problem even easier.

## Procedure
 1. Set the `cookies` cookie to a large value (e.g. **1235193458612934857102938471923847**).
   * **Probably not shorter way:** Install [EditThisCookie](http://www.editthiscookie.com/) and set the `cookies` cookie to a ridiculous number.
   * **Long way:** Open your browser's development tools, then type this in the JS console:
     ```javascript
     document.cookie = "cookies=102384701923847091283640912384609123485701923857"
     ```
 2. Navigate to [the flag](http://localhost:5001/flag), revealing the flag in plain text.
 3. Profit! :tada:

> write-up by: [**@anli5005**](https://anli.dev) and [**@aidanglickman**](https://aidanglickman.com)
