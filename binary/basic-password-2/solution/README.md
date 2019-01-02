# Basic Password 2

## Procedure

Alright, so we can't brute force this problem like we could the previous one.
Or rather, we *could* but it would take way too long to get any meaningful results.

Instead, we can take a look at the compiled code.
There are many tools, called [disassemblers](https://en.wikipedia.org/wiki/Disassembler), which take binary machine code and try to recreate the assembly code, such as:

-   [IDA](https://www.hex-rays.com/products/ida/)
-   [Hopper](https://www.hopperapp.com/)
-   [Radare](https://rada.re/)

We can use any of these programs to peer into the code.
The following is the code when viewed through Radare2:

```
|           0x00401565      e886010000     call sym.__main
|           0x0040156a      837df002       cmp dword [local_10h], 2
|       ,=< 0x0040156e      0f8592000000   jne 0x401606
|       |   0x00401574      48b874686973.  movabs rax, 0x2073692073696874 ; 'this is '
|       |   0x0040157e      488945a0       mov qword [local_60h], rax
|       |   0x00401582      48b861206d75.  movabs rax, 0x6d206863756d2061 ; 'a much m'
|       |   0x0040158c      488945a8       mov qword [local_58h], rax
|       |   0x00401590      48b86f726520.  movabs rax, 0x756365732065726f ; 'ore secu'
|       |   0x0040159a      488945b0       mov qword [local_50h], rax
|       |   0x0040159e      48b872652070.  movabs rax, 0x7773736170206572 ; 're passw'
|       |   0x004015a8      488945b8       mov qword [local_48h], rax
|       |   0x004015ac      48b86f72642c.  movabs rax, 0x742069202c64726f ; 'ord, i t'
|       |   0x004015b6      488945c0       mov qword [local_40h], rax
|       |   0x004015ba      c745c868696e.  mov dword [local_38h], 0x6b6e6968 ; 'hink'
|       |   0x004015c1      c645cc00       mov byte [local_34h], 0
|       |   0x004015c5      488b45f8       mov rax, qword [local_8h]
|       |   0x004015c9      4883c008       add rax, 8
```
If we take a look at the lines above, we can see the passphrase, which is `this is a much more secure password, i think`.
Testing out this password in the program gives us a `Congrats!`, and the flag.

```
|      ,==< 0x004015de      7513           jne 0x4015f3
|      ||   0x004015e0      488d0d192a00.  lea rcx, str.Congrats__The_key_is_bcactf_its_another_password ; section..rdata ; 0x404000 ; "Congrats! The key is bcactf{its_another_password}"
|      ||   0x004015e7      e83c150000     call sym.puts               ; int puts(const char *s)
|      ||   0x004015ec      b800000000     mov eax, 0
```

We can also see the flag right on line 45.
