## Contribute to BCA CTF Problems

Thank you for your interest in BCA CTF!  We are very grateful for your help.

* [Contributing](#contributing)
* [Repository organization](#repository-organization)
* [Branches](#branches)
* [How to use Markdown to format your problems](#how-to-use-markdown-to-format-your-problems)
* [Formatting](#formatting)

>**Note**: Before submitting a pull request, please review the problem topics in the "Projects" tab and add your problem's corresponding topic to the beginning of your pull request's title in the form `[TOPIC_IN_BRACKETS] Problem name`.

## Contributing

To contribute to BCA CTF, you need to clone this repository, push your local repository to a new remote branch, and submit a pull request for the changes that you're proposing.

* [How to clone a repository](https://help.github.com/articles/cloning-a-repository/)
* [How to push to a remote branch](https://help.github.com/articles/pushing-to-a-remote/)
* [How to make a pull request](https://help.github.com/articles/creating-a-pull-request/)
* [Changing a commit message](https://help.github.com/articles/changing-a-commit-message/)
* [How to squash commits](https://help.github.com/articles/about-pull-request-merges/)

## Repository organization

The content in this repository follows an organization based on the topics listed in the "Projects" tab.

This repository contains the following folders:

* \binary
* \cryptography
* \miscellaneous
* \programming
* \reversing
* \web
* \other

Within these folders you'll find the accepted problems that will appear in our BCA CTF competition.  When creating your problem, be sure to place it within its corresponding topic folders.  Your problem should also be contained within its own folder with the problem's name as its title.  

### Branches

We recommend that you create a local working branch as you create your problem (and then submit a pull request when your changes are ready). Each branch and pull request should be limited to a single problem, both to streamline work flow, and to reduce the possibility of merge conflicts.

## How to use Markdown to format your topic

All text associated with problems in this repository use Markdown.  Here is a good overview of [Markdown basics](https://help.github.com/articles/markdown-basics/).

## Formatting

### Headings

H1 headings `#` are used at the top of your problem's prompt/solution to display the problem's name and topic (same format as the pull request title).

H2 subheadings `##` are used if you need to seperate your problem prompt/solution into additional sections.  Any heading smaller than H2 should be rarely used.

### Text formatting

Use bold for information you want to stand out to the user.

    **like Julius Caesar**
    **62 6f 6c 64 0a**

Limit the use of bold for emphasis unless it is crucial to get the user's attention. Avoid the use of italics for emphasis since italics doesn't render well on the site.

Use inline code formatting (backticks) for any code or commands.

    `print("Hello World")`
    `$ cd ..`
    `gcc -o test.c`

Use '>' to show sequence.

    **File** > **Preferences** > **Settings**
    **Downloads** > **Reverse This**

### Links

For links within your problem prompt/solution, use the following format.

For example: `[6502 tutorial](https://www.youtube.com/watch?v=dQw4w9WgXcQ)` - links to a relevant YouTube video

>**Note:** If you are creating a server-side problem, please contact an administrator about how you should proceed.

### Images

Images are important to bring the problem prompt to life.

For images you're adding to the repo, store them in an `images` subfolder of your problem folder, for example: `images\nottheflag`.

When you link to an image in your problem's prompt/solution, the path and filename are case-sensitive.  The convention is for image filenames to be all lowercase; however, you can be as creative as you'd like.

For example: `![The Flag](images\nottheflag)`

### Source Code

For longer code we use the fenced code block notation ```` ``` ````.

>**Note:** You can add an optional language identifier to enable syntax highlighting in your fenced code block. E.g. ```` ```json ```` or ```` ```javascript ````. [Read more →](https://help.github.com/articles/creating-and-highlighting-code-blocks/#syntax-highlighting)

Some JavaScript code...

```javascript
function fancyAlert(arg) {
  if (arg) {
    $.facebox({ div: foo });
  }
}
```
