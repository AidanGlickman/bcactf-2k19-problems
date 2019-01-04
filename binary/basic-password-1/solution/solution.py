import subprocess
import os

NULL = open(os.devnull, "w")
result = 1
i = -1

while result == 1:
    i += 1
    result = subprocess.call(["compiled", str(i)], stdout=NULL, stderr=subprocess.STDOUT)

print(i)