#!/usr/bin/env python3
PRINTABLES = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
PRINTABLELIST = [" !\"#$%&'()*+,-./", "0123456789", ":;<=>?@", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "[\\]^_`", "abcdefghijklmnopqrstuvwxyz", "{|}~"]
FLAG = "bcactf{L157_8453d_pR0gR4Mm1nG_15_4w3S0Me!}"

instructions = []

for i in FLAG:
    inst = ""
    for j in PRINTABLELIST:
        loc = j.find(i)
        if loc == -1:
            inst += "d"

        else:
            inst += "a"
            break
    inst += "d"*(loc) + "a"
    instructions.append("c" + inst[::-1] + "r")

for i in instructions:
    print(i, end=", ")
    