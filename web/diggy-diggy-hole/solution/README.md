# Diggy Diggy Hole Writeup

## Necessary Tools

* A tool capable of inspecting the DNS records for a given website.

## Procedure
In this procedure, we'll be using `dig`, a DNS utility that comes with most \*nix systems.

1. In the command line, run:

```shell
  $ dig hole.sketchy.dev TXT
```

2. Inspect the output. The flag, indicated by `bcactf`, should be there.
