user_input = input("Enter a password: ")

check = [100452, 101476, 99428, 101476, 118884, 104548, 126052, 106596, 103524, 110692, 110692, 113764, 97380, 118884, 106596, 103524, 116836, 103524, 128100]
output = []

for char in user_input:
    i = ord(char)
    bitwise = (((i ^ 100) | i ^ (i << 10)) ^ 134 + ((i >> 20) | i) ^ (i ** 5 + i))
    output.append(bitwise)

if output == check:
    print("Success!")
else:
    print("Wrong!")

print(output)