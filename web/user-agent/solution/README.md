# User Agent

## Procedure

A [user agent](https://en.wikipedia.org/wiki/User_agent) is something that tells a website something about who you are.
A common use for user agents is to tell websites what browser you are using, or for robots (e.x. [Googlebot](https://en.wikipedia.org/wiki/Googlebot)).

The website tells us that "All computers are set up to use your SCP-id and security clearance as user agents".
This is obtained by hovering over the phrase `user agent authentication`.
To change user agents, there are many browser extensions that should work just fine.
Or, you could use `$ curl -A "user_agent" https://website.url`.
So,, what should we change our user agent to?

SCP folklore gives us several [security clearance levels](http://www.scp-wiki.net/security-clearance-levels), the highest being "Level 5".
Persons with Level 5 Security Clearance are typically in the O5 Council.
This, alongside the banner we get first loading the website, suggests that we may want to put `O5` somewhere in our user agent.
If we then request the webpage again, we get the following line: 

```html
<div class="content-panel centered standalone"><p>Welcome O5 council member, the flag is <span style="font-size:large; color: #600;">bcactf{hey_2521_is_pretty_coo-}</span>.</p></div>
```

Cool!

> write-up by: [**@edwfeng**](https://github.com/edwfeng)