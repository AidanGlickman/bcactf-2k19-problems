# Compression

## Procedure

This problem is an exercise in futility.
There is no reason why you should ever compress something this many times.
Despite this, it is still useful to learn about compression, so here we go!

The following are widely used compression tools:
* [tar](https://www.gnu.org/software/tar/) is an archiving utility, and stores many files in one "tarball"
  * On any modern system, running `$ tar -xf file` will automatically detect any compression algorithms
  * Using the flag `-v` gives you visual output
* [gzip](https://www.gzip.org/) is a lossless data compression utility
  * Running `$ gunzip -c file` outputs the uncompressed contents to the terminal, so you will need to redirect it (i.e. `$ gunzip -c file > uncompressed`)
* [bzip2](http://www.bzip.org/) is another file compression utility
  * Similarly to gzip, you will need to run `$ bunzip2 -c file > uncompressed`

Typically, files are archived with tar and then compressed with either gzip or bzip2, creating files that have extensions of `name.tar.gz` or `name.tar.bz2`.

We start off with the file `999`.
We can use `$ file 999` to determine that this is compressed with bzip2.
If we try extracting this with `tar`, we get the folllowing error:
```
tar: This does not look like a tar archive
tar: Skipping to next header
tar: Exiting with failure status due to previous errors
```
This implies that this is just compressed with bzip2, and hasn't touched tar whatsoever.
This gives you two options for the following steps: you can try using tar to see if anything is a compressed tarball, or you can just use gunzip/bunzip2 until you reach a tarball.

However, we run into a bit of an error when we get to file `123`, which is labeled as `ASCII text`.
When we read the contents, we see a lot of information.
What could this possibly mean?

`123` is a [hex dump](https://en.wikipedia.org/wiki/Hex_dump), which is just a visualization of all the data you could ever want.
We can use a utility called [xxd](https://linux.die.net/man/1/xxd) to create these, and we can also use them to reverse hexdumps.
Running `$ xxd -r 123`, we see the gibberish we are more used to with compression.
Success! We can now move on.

We continue until we get to `000`.
This is another `ASCII text` file, but unlike `123` and `240`, this is the flag.

If you want to reverse the reversing (otherwise known as compressing), the commands used can be found below.
```
tar czf 858 000;
tar cjf 744 858;
gzip -c 744 > 495;
tar czf 218 495;
bzip2 -c 218 > 989;
xxd 989 > 240
tar cf 557 240;
gzip -c 557 > 474;
bzip2 -c 474 > 511;
gzip -c 511 > 674;
xxd 674 > 123;
tar cjf 628 123
gzip -c 628 > 871;
tar czf 728 871;
bzip2 -c 728 > 999;
```

> write-up by: [**@edwfeng**](https://github.com/edwfeng)