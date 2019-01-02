## Contribute to BCA CTF Problems

[![Documentation Status](https://img.shields.io/readthedocs/bca-ctf/2019.svg?logo=read%20the%20docs)](https://bca-ctf.readthedocs.io/en/2019/?badge=2019)
[![Request Writeup](https://img.shields.io/badge/request-writeup-673AB6.svg?style=flat)](https://goo.gl/forms/ZWUjr38XkOZ21HWl2)

Thank you for your interest in BCA CTF!  We are very grateful for your help.

* [Contributing](#contributing)
* [Repository organization](#repository-organization)
* [Branches](#branches)
* [Formatting](#formatting)

>**Note**: Before submitting a pull request, please review the problem topics in the "Projects" tab and add your problem's corresponding topic to the beginning of your pull request's title in the form `[TOPIC_IN_BRACKETS] Problem name`.

## Contributing

To contribute to BCA CTF, you need to clone this repository, push your local repository to a new remote branch, and submit a pull request for the changes that you're proposing.

In order to push a change/problem, you can use `git push origin master:<remote branch name>` so that you do not need multiple branches on your local machine.

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
* \other
* \programming
* \reversing
* \web
* \forensics

Within these folders you'll find the accepted problems that will appear in our BCA CTF competition.  When creating your problem, be sure to place it within its corresponding topic folders.  Your problem should also be contained within its own folder with the problem's name as its title.  

### Branches

We recommend that you create a local working branch as you create your problem (and then submit a pull request when your changes are ready). Each branch and pull request should be limited to a single problem, both to streamline work flow, and to reduce the possibility of merge conflicts.

### Pull Requests

When submitting a pull request, please do not assign any people to it.  Also, make sure you are using the correct naming convention of `[TOPIC_IN_BRACKETS] Problem name`.

### Formatting

Please read [the styleguide](STYLEGUIDE.md) before writing a problem, and make sure to follow it. Otherwise your pull request will be put on hold until you fix the formatting of the problem.