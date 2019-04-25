#!/usr/bin/env python3

with open("flag.txt", "r") as text:
    lines = text.read().splitlines()

flag = ""
keys = list(map(lambda num: int(num)-1, lines[0].split()))

for line in lines[1::]:
    if len(line) % 3 == 0 and "&" not in line:
        flag += line[keys.pop(0)]

print(flag)