solutions = [9039173132, 9509805496, 8587439808, 9509805496, 21003461882,
             11040769100, 28152980408, 12166570218, 10510073076, 14693178610,
             14693178610, 16850535428, 7737763492, 23863587012, 16850535428,
             19254164252, 14693178610, 9999906026, 30517542772]
output = ""


def get_bitwise(char):
    for i in range(126):
        if (((i ^ 100) | i ^ (i << 10)) ^ 134 + ((i >> 20) | i) ^ (i ** 5 + i)) == char:
            return i


for item in solutions:
    output += chr(get_bitwise(item))

print(output)
