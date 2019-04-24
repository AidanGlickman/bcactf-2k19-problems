# Public Library Writeup

## Necessary Tools
* Something that can compile and run Java or any other JVM-based language

## Procedure

### Intended Method
1. Take a look at the `PublicLibrary.class` file in a Java decompiler.
  * Depending on the decompiler you use, you will either see the flag, or possibly just the names of the functions. 
  * If you see the flag, then congratulations! Otherwise, Continue with the following steps.
1. Create a new Java project and ensure that `PublicLibrary.class` is in your classpath.
1. Make a new class that instantiates a `PublicLibrary` instance and prints the result of the `getFlag()` method. [Example code](PublicLibraryTest.java)
1. Run the code, which should print out the flag.

> write-up by: [**@anli5005**](https://anli.dev) and [**@aidanglickman**](https://aidanglickman.com)
