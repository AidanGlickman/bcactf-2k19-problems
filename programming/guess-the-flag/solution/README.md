# Guess the Flag Writeup

## Necessary Tools
* A web browser capable of running [Scratch 3.0](https://scratch.mit.edu).

## Procedures
There are two possible procedures to solve this problem. Both of them are listed here:

### Procedure 1: Reverse Engineering
1. Run the project once by clicking the green flag, and click **See inside** to reveal the code.
1. Of each of the four scripts located in **Sprite1**, only **generate flag** seems to be generating the flag in a variable named **flag**. Therefore, begin reverse engineering the blocks located under **generate flag**.
1. The first block sets **flag** to `bcactf{`. This is expected, since most flags in BCA CTF are prefixed with `bcactf{`.
1. The next 5 blocks (including those in the loop) reverse the string `d3hct4rcs` and add the result to the **flag** variable. Therefore, our flag so far is `bcactf{scr4tch3d`.
1. The next block adds an underscore to the flag, meaning that the flag is now `bcactf{scr4tch3d_`.
1. The next block translates `why` to French and adds the result to the flag. Translating `why` to French with Google Translate yields `Pourquoi`. Thus, the flag is now `bcactf{scr4tch3d_Pourquoi`. After that, the next block adds an underscore to the flag.
1. The next block fetch the backdrop name and add it to the flag. Clicking on the **Stage** and looking at the current backdrop shows that the current backdrop is `empty`, meaning that the flag is now `bcactf{scr4tch3d_Pourquoi_empty`. An underscore is added by the next block.
1. The next block multiplies 0 by a random number and stores it in **var3**. Since 0 multiplied by anything is 0, **var3** is `0`.
1. The next block computes the expression `var3 + (12341234 / 1234) + (23412342453425 * (1000 % 3)) + 256` and adds the result to the flag. Therefore, the flag is now `bcactf{scr4tch3d_Pourquoi_empty_234123424643682`.
1. Finally, the last block finishes the flag by adding a closing bracket, resulting in the final flag:  `bcactf{scr4tch3d_Pourquoi_empty_234123424643682}`.
1. Run the project, type this flag in, and verify that it is correct.

### Procedure 2: Code Injection
1. Click **See inside** to reveal and modify the code.
1. In the blocks palette, scroll down to the **Variables** section, and check the box next to **flag**. This causes the **flag** variable to appear on the stage.
1. Run the project by clicking the green flag. It appears that every time the flag is checked, the **flag** variable is reset to `[REDACTED]`. As such, to prevent that, the code that sets **flag** to `[REDACTED]` must be removed.
1. Locate that code in the **reset variables** script. Remove it.
1. Run the project again, and type in anything when prompted. The flag, `bcactf{scr4tch3d_Pourquoi_empty_234123424643682}` should appear in the **flag** variable.
1. Run the project once more, type in the flag, and verify that it is correct.
