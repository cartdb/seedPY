import os
import sys
import random
if len(sys.argv) != 2:
    raise Exception("Too many or too little arguments!")
os.system("zipextract")
os.system("print " + sys.argv[1] + " " + sys.argv[1] + ".txt")
file = open(sys.argv[1] + ".txt", "r")
hashes = []
while True:
    line = file.readline()
    if not line:
        break
    line = line.split(" SHA512: ")[0]
    line = line.replace("\\n", "")
    hashes.append(line)
rom = random.choice(hashes)
print(rom)