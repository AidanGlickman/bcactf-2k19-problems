PRINTABLELIST = [" !\"#$%&'()*+,-./", "0123456789", ":;<=>?@", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "[\\]^_`", "abcdefghijklmnopqrstuvwxyz", "{|}~"]
INSTRUCTIONS = ["cadadddddr", "caddadddddr", "caadddddr", "caddadddddr", "cadddddddddddddddddddadddddr", "cadddddadddddr", "caaddddddr", "cadddddddddddadddr", "cadadr", "cadddddadr", "cadddddddadr", "caddddaddddr", "caddddddddadr", "caddddadr", "cadddddadr", "cadddadr", "cadddadddddr", "caddddaddddr", "cadddddddddddddddadddddr", "cadddddddddddddddddadddr", "caadr", "caddddddadddddr", "cadddddddddddddddddadddr", "caddddadr", "caddddddddddddadddr", "caddddddddddddadddddr", "cadadr", "cadddddddddddddadddddr", "caddddddadddr", "caddddaddddr", "cadadr", "cadddddadr", "caddddaddddr", "caddddadr", "caddddddddddddddddddddddadddddr", "cadddadr", "caddddddddddddddddddadddr", "caadr", "caddddddddddddadddr", "caddddadddddr", "cadar", "caddaddddddr"]

for i in INSTRUCTIONS:
    listnum, strnum = map(len, i[-2:1:-1].split("a"))
    print(PRINTABLELIST[listnum][strnum], end="")
